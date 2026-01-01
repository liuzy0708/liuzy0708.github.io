{% for link in site.data.navigation.main %}
  {% if link.right %}
    <a class="normal right" href="{{ link.url }}" data-lang-en="{{ link.title }}" data-lang-zh="{{ link.title_zh }}">{{ link.title }}</a>
    {% else %}
    <a class="normal" href="{{ link.url }}" data-lang-en="{{ link.title }}" data-lang-zh="{{ link.title_zh }}">{{ link.title }}</a>
  {% endif %}
{% endfor %}

<div class="lang-switcher">
  <a href="#" class="lang-switcher-btn" data-lang="en" title="English">EN</a>
  <span class="lang-separator">|</span>
  <a href="#" class="lang-switcher-btn" data-lang="zh" title="中文">中文</a>
</div>

