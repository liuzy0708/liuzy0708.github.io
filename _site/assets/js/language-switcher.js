// Language Switcher for Jekyll Homepage
(function() {
  'use strict';

  // 默认语言设置
  const DEFAULT_LANG = 'en';
  const LANG_KEY = 'site_language';

  // 获取当前语言
  function getCurrentLang() {
    return localStorage.getItem(LANG_KEY) || DEFAULT_LANG;
  }

  // 设置当前语言
  function setCurrentLang(lang) {
    localStorage.setItem(LANG_KEY, lang);
  }

  // 切换语言
  function switchLanguage(lang) {
    setCurrentLang(lang);
    updatePageLanguage(lang);
    updateLanguageButton(lang);
  }

  // 更新页面语言
  function updatePageLanguage(lang) {
    // 更新所有带有 data-lang 属性的元素
    document.querySelectorAll('[data-lang-en], [data-lang-zh]').forEach(function(element) {
      const enContent = element.getAttribute('data-lang-en');
      const zhContent = element.getAttribute('data-lang-zh');
      
      if (lang === 'zh' && zhContent !== null) {
        // 检查是否包含HTML标签
        if (zhContent.includes('<') || (zhContent.includes('&') && zhContent.includes(';'))) {
          // 使用innerHTML处理包含HTML的内容
          element.innerHTML = zhContent;
        } else {
          // 纯文本内容
          element.textContent = zhContent;
        }
      } else if (lang === 'en' && enContent !== null) {
        if (enContent.includes('<') || (enContent.includes('&') && enContent.includes(';'))) {
          element.innerHTML = enContent;
        } else {
          element.textContent = enContent;
        }
      }
    });

    // 更新所有带有 lang-en 和 lang-zh 类的元素
    document.querySelectorAll('.lang-en, .lang-zh').forEach(function(element) {
      if (lang === 'zh') {
        element.classList.remove('lang-en');
        element.classList.add('lang-zh');
        element.style.display = element.classList.contains('lang-zh') ? '' : 'none';
      } else {
        element.classList.remove('lang-zh');
        element.classList.add('lang-en');
        element.style.display = element.classList.contains('lang-en') ? '' : 'none';
      }
    });

    // 切换显示/隐藏
    document.querySelectorAll('.lang-en').forEach(function(element) {
      element.style.display = lang === 'en' ? '' : 'none';
    });
    
    document.querySelectorAll('.lang-zh').forEach(function(element) {
      element.style.display = lang === 'zh' ? '' : 'none';
    });

    // 更新HTML lang属性
    document.documentElement.lang = lang === 'zh' ? 'zh-CN' : 'en-US';
  }

  // 更新语言切换按钮
  function updateLanguageButton(lang) {
    const buttons = document.querySelectorAll('.lang-switcher-btn');
    buttons.forEach(function(btn) {
      if (btn.getAttribute('data-lang') === lang) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });
  }

  // 初始化
  function init() {
    const currentLang = getCurrentLang();
    updatePageLanguage(currentLang);
    updateLanguageButton(currentLang);

    // 绑定语言切换按钮事件
    document.querySelectorAll('.lang-switcher-btn').forEach(function(btn) {
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        const targetLang = this.getAttribute('data-lang');
        switchLanguage(targetLang);
      });
    });
  }

  // DOM加载完成后初始化
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // 导出函数供外部调用
  window.LanguageSwitcher = {
    switch: switchLanguage,
    getCurrent: getCurrentLang
  };
})();

