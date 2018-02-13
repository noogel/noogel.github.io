---
title: Git操作场景化实践
date: 2018-02-10
tags: git
id: 1
---

小明（是一个虚构人物）作为一名开发工程师（认真脸），平时经常用 Git 提交代码，觉得有些操作姿势还是很不舒服的，于是专门研究了一下各种场景下如果操作更优雅。

注意摆好姿势向下看！！！

(额，好吧，虽然开题很短，不过你们可以想象的很长。)


## git merge 场景

### 场景一：分支 merge

有时候开发一个稍微大一些的需求持续个几天，搞一个分支去提交吧，于是有了 `git checkout -b mywork`，在 mywork 分支 commit C4、C5，然后主分支被 commit C3，最后我要将分支 merge 到之分支之上 `git merge mywork`。

![](/resource/img/15182443948597.jpg)

流程示意图如上面，使用 merge 的好处就是多人维护一个项目仓库的时候，要任何时候保证主分支代码是可用的，任何人不应该直接在 master 上提交代码。

### 场景二：merge request

fork \ merge request

![](/resource/img/15182456532437.jpg)



## rebase

![](/resource/img/15182459869424.jpg)

![](/resource/img/15184903464515.jpg)








![](/resource/img/15182392077656.jpg)

![](/resource/img/15182392205290.jpg)

![](/resource/img/15182392609263.jpg)



## blame

`git blame __init__.py`

![](/resource/img/15184912683256.jpg)


## grep


## revert 


## patch


## hooks


## stash


## 

