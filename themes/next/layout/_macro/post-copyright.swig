{% if page.copyright %}
  <blockquote>
  <p><strong>版权声明： 本文为 {{ theme.author }} 原创文章，发表自 <a href="{{ url_for(page.path) }}" title="{{ page.title }}">{{ config.title }}</a>。转载需向 <a href="mailto:noogel@163.com">我的邮箱</a> 申请。</strong></p>
  </blockquote>
{% endif %}
