---
title: Xpath总结
date: 2017-01-31
tags: Xpath
---

1. Firefox + Firepath、Chrome + XPath Helper
2. 常用xpath例子

-----------

## Firefox + Firepath、Chrome + XPath Helper

如下图 Firefox下，XPath需要通过Firebug + Firepath来方便的获取。
![firefox xpath](/resource/img/firefox_xpath.png)

Chrome下，通过XPath Helper插件实现，开启和关闭快捷键`Ctrl + Shift + X`,按住`Shift`键获取。
![chrome xpath heloer](/resource/img/chrome_xpathhelper.png)

以上两种方式还是Firefox下使用比较方便，更多用法自行发掘。

## 常用xpath例子

根据字符串匹配节点，通过`contains()`、`text()`匹配
`.//*[@id='detail_all']/div[1]/ul/li[contains(text(), '字 数：')]/text()`

节点属性不包含**字符串，通过`not()`、`contains()`匹配
`.//*[@id='con_ListStyleTab4A_1']/p[not(contains(@class, 'title'))]/a[@class='Author']/text()`

截取字符串匹配
`substring-before(//div[@class='content']/ul/li[6],',')`
`substring(.//h2/../p/span[contains(text(), '字数：')]/text(), '4')`

索引匹配末尾节点，通过`last()`匹配
`.//div[last()]/div[@class='show_info_right max_width']/text()`

通过`..`向上级查找匹配
`.//h1/../div[@class='booksub']/span/span/text()`

--------

## 参考
> http://www.cnblogs.com/barney/archive/2009/04/17/1438062.html
> http://www.w3school.com.cn/xpath/xpath_functions.asp