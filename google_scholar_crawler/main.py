import argparse
import json
import logging
import os
from datetime import datetime
from pathlib import Path
from tempfile import NamedTemporaryFile
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from scholarly import MaxTriesExceededException, ProxyGenerator, scholarly


AUTHOR_ID = 'sRkvMF8AAAAJ'
MTL_PUBLICATION_ID = f'{AUTHOR_ID}:zYLM7Y9cAGgC'
RESULTS_DIR = Path(__file__).resolve().parent / 'results'
PROFILE_URL = f'https://scholar.google.com/citations?hl=en&user={AUTHOR_ID}&pagesize=100'


class FetchError(Exception):
    """An actionable error fetching or parsing the Scholar profile."""


def check_connection(session, timeout):
    """Detect blocking before scholarly tries to launch a CAPTCHA browser."""
    logging.info('正在检查 Google Scholar 访问情况……')
    try:
        response = session.get(PROFILE_URL, timeout=timeout)
    except requests.exceptions.ProxyError as exc:
        raise FetchError(
            '代理连接失败，请检查代理软件和节点，或用 --proxy 指定可用的代理地址。'
        ) from exc
    except requests.exceptions.Timeout as exc:
        raise FetchError('连接 Google Scholar 超时，请检查网络或代理后重试。') from exc
    except requests.exceptions.RequestException as exc:
        raise FetchError('无法连接 Google Scholar，请检查网络、代理和 HTTPS 证书。') from exc

    soup = BeautifulSoup(response.text, 'html.parser')
    captcha = soup.select_one('#gs_captcha_ccl, #recaptcha, #captcha-form, .rc-doscaptcha-body')
    if response.status_code in (403, 429) or captcha or '/sorry/' in response.url:
        raise FetchError(
            f'Google Scholar 拒绝了请求或要求验证码（HTTP {response.status_code}）。'
            '请检查代理节点是否能访问 Scholar，稍后重试或换用可用节点。'
            '浏览器通过验证码后的会话不会自动共享给 Python。'
        )
    if response.status_code != 200:
        raise FetchError(f'Google Scholar 返回 HTTP {response.status_code}，请稍后重试。')
    if soup.find(id='gsc_prf_in') is None:
        raise FetchError('返回内容不是作者主页，请检查是否需要登录或页面结构是否发生变化。')


def fetch_author(timeout):
    proxy = ProxyGenerator()
    # Reuse the checked session, including its User-Agent and cookies. Supplying
    # both managers also avoids scholarly automatically trying free proxies.
    check_connection(proxy.get_session(), timeout)
    scholarly.use_proxy(proxy, proxy)
    scholarly.set_timeout(timeout)
    scholarly.set_retries(2)

    logging.info('正在获取作者资料和论文引用数据……')
    try:
        author = scholarly.search_author_id(AUTHOR_ID)
        scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
    except MaxTriesExceededException as exc:
        raise FetchError(
            '抓取过程中无法继续访问 Google Scholar，可能再次触发验证码或代理连接失败。'
            '请稍后重试；可加 --verbose 查看详细日志。'
        ) from exc
    except (AttributeError, KeyError, TypeError, ValueError) as exc:
        raise FetchError(
            '无法解析 Scholar 数据，可能返回了验证页面或页面结构已变化。'
            '可加 --verbose 查看详细日志。'
        ) from exc
    return author


def badge(citations):
    return {'schemaVersion': 1, 'label': 'citations', 'message': str(citations)}


def prepare_outputs(author):
    """Prepare every payload before touching existing website data."""
    author = dict(author)
    author['publications'] = {
        publication['author_pub_id']: publication
        for publication in author['publications']
    }
    author['updated'] = str(datetime.now())
    outputs = {
        'gs_data.json': author,
        'gs_data_shieldsio.json': badge(author['citedby']),
    }
    publication = author['publications'].get(MTL_PUBLICATION_ID)
    if publication is not None and 'num_citations' in publication:
        outputs['gs_data_shieldsio_mtl.json'] = badge(publication['num_citations'])
    else:
        logging.warning('未找到论文 %s 的引用数据，保留现有 MTL 徽章。', MTL_PUBLICATION_ID)
    return outputs


def save_outputs(outputs, results_dir=RESULTS_DIR):
    # Serialize and stage all files first; replace each destination atomically.
    payloads = {
        filename: json.dumps(value, ensure_ascii=False)
        for filename, value in outputs.items()
    }
    results_dir.mkdir(parents=True, exist_ok=True)
    staged = []
    try:
        for filename, payload in payloads.items():
            with NamedTemporaryFile('w', encoding='utf-8', dir=results_dir,
                                    prefix='.', suffix='.tmp', delete=False) as outfile:
                temporary = Path(outfile.name)
                staged.append((temporary, results_dir / filename))
                outfile.write(payload)
        for temporary, destination in staged:
            os.replace(temporary, destination)
    finally:
        for temporary, _ in staged:
            if temporary.exists():
                temporary.unlink()


def main(argv=None):
    parser = argparse.ArgumentParser(description='更新 Google Scholar 引用数据和网站徽章。')
    parser.add_argument('--proxy', default=os.environ.get('SCHOLAR_PROXY'),
                        help='代理地址，例如 http://127.0.0.1:7897；默认使用系统代理。')
    parser.add_argument('--timeout', type=int, default=15, help='单次请求超时秒数（默认 15）。')
    parser.add_argument('--verbose', action='store_true', help='显示详细抓取日志。')
    args = parser.parse_args(argv)
    if args.timeout <= 0:
        parser.error('--timeout 必须大于 0')
    if args.proxy:
        parsed = urlparse(args.proxy)
        if parsed.scheme not in ('http', 'https', 'socks5', 'socks5h') or not parsed.hostname:
            parser.error('--proxy 应为完整地址，例如 http://127.0.0.1:7897')
        for name in ('HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy'):
            os.environ[name] = args.proxy

    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO,
                        format='%(levelname)s: %(message)s')
    scholarly.set_logger(args.verbose)
    try:
        author = fetch_author(args.timeout)
        outputs = prepare_outputs(author)
    except FetchError as exc:
        logging.error('%s 原有 results 数据未修改。', exc, exc_info=args.verbose)
        return 1
    except (KeyError, TypeError, ValueError):
        logging.error('抓取结果缺少必要字段，原有 results 数据未修改。', exc_info=args.verbose)
        return 1
    except KeyboardInterrupt:
        logging.error('已取消抓取，原有 results 数据未修改。')
        return 130

    try:
        save_outputs(outputs)
    except (OSError, TypeError, ValueError):
        logging.error('保存结果失败，请检查 results 目录权限或磁盘空间。', exc_info=args.verbose)
        return 1
    logging.info('已更新 %s 的引用数据：%s 次引用，%s 篇论文。',
                 author.get('name', AUTHOR_ID), author['citedby'], len(outputs['gs_data.json']['publications']))
    logging.info('结果目录：%s', RESULTS_DIR)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
