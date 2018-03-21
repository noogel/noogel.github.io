---
title: 关于Java的最初了解
date: 2018-03-15
tags: Java
id: 1
---

## Apache Maven

Maven 是一个项目管理和构建自动化工具。但是对于我们程序员来说，我们最关心的是它的项目构建功能，它可以规定项目的文件结构，比如下面：


| 目录 | 目的 |
| --- | --- |
| ${basedir} | 存放 pom.xml和所有的子目录 |
| ${basedir}/src/main/java | 项目的 java源代码 |
| ${basedir}/src/main/resources | 项目的资源，比如说 property文件 |
| ${basedir}/src/test/java | 项目的测试类，比如说 JUnit代码 |
| ${basedir}/src/test/resources | 测试使用的资源 |

## Spring Boot

Spring Boot 是一个轻量级框架，Spring Boot 的目的是提供一组工具，以便快速构建容易配置的 Spring 应用程序。


