---
title: InnoDB中的事务隔离级别与锁
date: 2019-05-22
tags: 数据库
id: 1
---

## 基本概念

一个事务在进行数据变更时对另一个事务产生的可见性影响描述，表达为 脏读、幻读、不可重复读三个概念。下面具体解释下对应概念。
* 脏读：当前事务能够读取其它事务未提交的数据。
* 幻读：当前事务中在前后两次相同查询中读取的数据不一致，原因在第一次查询后第二次查询前提交了数据产生的。（侧重于插入了新的数据）
* 不可重复读：当前事务中查询相同的范围数据，同一数据的内容发生了变化。（侧重于数据的更新）
基于这三个现象描述，主要因为 MySQL 设置的隔离级别不同导致的。


### ACID特性

* 原子性(Atomicity)，一个事务中的所有操作要么全部成功，要么全部失败，不能只成功一部分。
* 一致性(Consistency)，从一个一致性状态到另一个一致性状态的转换。（一致性和隔离性保证了数据的一致性）
* 隔离性(Isolation)，一个事务在提交之前对其它事务是不可见的。
* 持久性(Durability)，一个事务一旦被提交就会永久的保存到数据库中。


## InnoDB中的事务隔离级别

* 未提交读(Read Uncommitted)，允许脏读，也就是可能读取到其他会话中未提交事务修改的数据。
* 已提交读(Read Committed)，只能读取到已经提交的数据。Oracle等多数数据库默认都是该级别。
* 可重复读(Repeated Read)，在同一个事务内的查询都是事务开始时刻一致的，InnoDB默认级别。在SQL标准中，该隔离级别消除了不可重复读，但是还存在幻读。
* 串行化(Serializable)，完全串行化的读，每次读都需要获得表级共享锁，读写相互都会阻塞。

| 隔离级别 | 脏读（Dirty Read） | 不可重复读（NonRepeatable Read） | 幻读（Phantom Read） |
| --- | --- | --- | --- |
| 未提交读（Read uncommitted） | 可能 | 可能 | 可能 |
| 已提交读（Read committed） | 不可能 | 可能 | 可能 |
| 可重复读（Repeatable read） | 不可能 | 不可能 | 可能 |
| 可串行化（Serializable ） | 不可能 | 不可能 | 不可能 |


```
SELECT @@tx_isolation; 
```
![](/resource/img/15588467880791.jpg)


查询 InnoDB 的默认隔离级别是 RR，按照四种隔离级别的关系来看是会出现幻读情况，但实际上 InnoDB 引擎下的两次查询是一致的，那么它是帮我们解决幻读了吗？

```
//设置read uncommitted级别：
set session transaction isolation level read uncommitted;

//设置read committed级别：
set session transaction isolation level read committed;

//设置repeatable read级别：
set session transaction isolation level repeatable read;

//设置serializable级别：
set session transaction isolation level serializable;
```


### MySQL是如何解决幻读的？


1. 在可重复读隔离级别下,普通的查询是快照读,是不会看到别的事务插入的数据的。因此,幻读在 “ 当前读 ” 下才会出现。
2. update 语句的修改结果,被之后的 select 语句用 “ 当前读 ” 看到,不能称为幻读。幻读仅专指 “ 新插入的行 ” 。

产生幻读的原因是,行锁只能锁住行,但是新插入记录这个动作,要更新的是记录之间的 “ 间隙 ” 。因此,为了解决幻读问题, InnoDB 只好引入新的锁,也就是间隙锁 (Gap Lock) 。间隙锁和行锁合称 next-key lock ,每个 next-key lock 是前开后闭区间。next-key lock 可能会导致同样的语句锁住更大的范围,这其实是影响了并发度的，在 RR 隔离级别下，两个是事务同时锁住一个不存在的值，之后进行插入操作会引发死锁，因为间隙锁之间并不会冲突。如果设置成 RC 隔离级别的话间隙锁就不存在了，同时需要解决对应的数据和日志不一致问题，需要把 binlog 格式设置为 row 。



参考：

> https://www.cnblogs.com/likui360/p/9632641.html
> https://en.wikipedia.org/wiki/Isolation_(database_systems)#Phantom_reads
