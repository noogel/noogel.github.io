---
title: Xpath总结
date: 2017-01-31
tags: Xpath
---

1. Firefox + Firepath、Chrome + XPath Helper
2. 常用xpath例子

-----------

## Firefox + Firepath、Chrome + XPath Helper

Mark

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