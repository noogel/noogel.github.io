---
title: Python装饰器模式
date: 2014-10-22
tags: Python
id: 1
---

装饰器模式定义：动态地给一个对象添加一些额外的职责。

在 Python 中 Decorator Mode 可以按照像其它编程语言如 C++、Java 等的样子来实现，但是 Python 在应用装饰概念方面的能力上远不止于此， Python 提供了一个语法和一个编程特性来加强这方面的功能。

首先需要了解一下 Python 中闭包的概念：如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包（closure）。

![dec1](/resource/img/Dec/dec1.png)


```
def makeblod(fn):
    def wrapped():
        return '<b>'+fn()+'</b>'
    return wrapped

def makeitalic(fn):
    def wrapped():
        return '<i>'+fn()+'</i>'
    return wrapped

@makeblod
@makeitalic
def hello():
    return 'hello world'

print hello()
```

![dec2](/resource/img/Dec/dec2.png)

```
def deco(arg):
    def _deco(func):
        def __deco():
            print "before %s called [%s]." % (func.__name__, arg)
            func()
            print "after %s called [%s]." % (func.__name__, arg)
        return __deco
    return _deco

@deco("mymodule")
def myfunc():
    print "myfunc() called."
myfunc()
```

闭包学习：

http://blog.csdn.net/marty_fu/article/details/7679297