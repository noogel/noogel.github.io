---
title: 业务流程模型和标记法（BPMN）
date: 2021-01-27
tags: 效率
id: 1
---

BPMN 有什么优势呢，用了一段时间主要使用在业务流程表达上，表达符号比较多，相比流程图可以更清楚的表达业务流程，同步、异步，异常中断、事件消息等等，如果看图的人都对这些符号有概念，可以比较轻松的看懂业务流程。缺点就是符号太多，学习成本相对高一些。学会了就会对业务表达上有很好的助力。

## 范围

BPMN仅限于支持对业务流程有用的建模概念。这意味着组织所做的非业务目的其他类型建模将排除在BPMN之外。例如，以下方面的建模不属于BPMN的一部分：

* 组织结构
* 职能分解
* 数据模型

此外，虽然BPMN会显示数据的流（消息）以及活动与数据器物的关联，但它并非数据流图（data flow diagram）。

<!--more-->

## 要素

BPMN用很小一套图形要素做简单的图来建模，这将令业务用户与开发者一样容易理解其中的过程和流。它的四种基本要素如下：

1. 流对象（Flow Object）：事件（Events），活动（Activities），关口（Gateways）
2. 连接对象（Connecting Objects）：顺序流（Sequence Flow），消息流（Message Flow），关联（Association）
3. 泳道（Swimlanes）：池（Pool），道（Lane）
4. 器物（Artifacts/Artefacts）：数据对象（Data Object），组（Group），注释（Annotation）

这四大类对象令我们有机会做出简单的业务流程图（BPD, business process diagram）。同时，BPMN也允许在BPD中创建你自己的流对象、器物类型，使图更好理解。

## 流对象与连接对象

![](/resource/img/2021-01-31-14-03-31.png)

## 泳道与器物

![](/resource/img/2021-01-31-14-03-36.png)

## 业务流程图的类型

![](/resource/img/2021-01-31-14-03-43.png)

## 常用符号

![](/resource/img/2021-01-31-14-03-48.png)

![](/resource/img/2021-01-31-14-03-54.png)

## 免费画 BPMN 流程图的工具

https://app.diagrams.net/

![](/resource/img/2021-01-31-14-04-00.png)

![](/resource/img/2021-01-31-14-04-07.png)

## 参考

https://github.com/Pingren/bpmn-dataflow-diagram-editor
https://github.com/zhangqiangboss/WorkflowAndCamunda/blob/master/docs/camunda/CamundaProEngine.md
https://www.edrawsoft.cn/bpmn-symbols/


