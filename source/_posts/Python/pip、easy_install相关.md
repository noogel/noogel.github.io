---
title: pip、easy_install相关
date: 2015-09-19
tags: [pip, easy_install]
id: 1
---

pip更新`python -m pip install -U pip`

## pipy国内镜像目前有：

http://pypi.douban.com/  豆瓣
http://pypi.hustunique.com/  华中理工大学
http://pypi.sdutlinux.org/  山东理工大学
http://pypi.mirrors.ustc.edu.cn/  中国科学技术大学

----------

## 指定源安装

pip可以通过指定源的方式安装`pip install web.py -i http://pypi.douban.com/simple`

也可以通过修改配置文件：
Linux的文件在`~/.pip/pip.conf`，Windows在`%HOMEPATH%\pip\pip.ini`。
文件内容：
```
[global]
index-url = http://pypi.douban.com/simple
```

easy_install指定源安装`easy_install -i http://pypi.douban.com/simple`

修改配置文件：
编辑文件`vim ~/.pydistutils.cfg`，写入文件内容如下：
```
[easy_install]
index_url = http://e.pypi.python.org/simple
```

-----------

## 安装Python安装包管理工具相关命令

安装easy_install：`apt-get install python-setuptools`
`sudo yum install python-setuptools-devel`
`esay_install pip`
pip指定版本：`pip install 'pymongo<2.8'`
升级版本：`pip install --upgrade pymongo`
查看已安装包：`pip show --files SomePackage`
查看需要更新的包：`pip list --outdated`
卸载包：`pip uninstall SomePackage`
帮助：`pip --help`
指定豆瓣源安装：`pip install -i http://pypi.douban.com/simple/ functools32`
查看已安装包：`pip list`
> http://www.cnblogs.com/taosim/articles/3288821.html

------------

## Windows安装pip
1.安装附件 `get-pip.py`就好了。
2.添加脚本路径`C:\Python27\Scripts`到系统环境变量。

------------

## easy_install查看包的版本
```
root@xyz-pc:~# easy_install tornado -v
Searching for tornado
Best match: tornado 4.0.2
tornado 4.0.2 is already the active version in easy-install.pth

Using /usr/lib/python2.7/dist-packages
Processing dependencies for tornado
Finished processing dependencies for tornado
Searching for -v
Reading https://pypi.python.org/simple/-v/
Couldn't find index page for '-v' (maybe misspelled?)
Scanning index of all packages (this may take a while)
Reading https://pypi.python.org/simple/
No local packages or download links found for -v
error: Could not find suitable distribution for Requirement.parse('-v')
```