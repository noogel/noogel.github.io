---
title: k近邻算法
date: 2016-05-30
tags: [分类算法, KNN]
---

简单解释：采用测量不同特征值之间距离的方法进行分类的算法。
主要优点是精度高，缺点是计算和空间负责度高，适用于数值型和标称型。
已下是通过Python实现的k-近邻算法，大致思路是计算样本数据`data_set`中的点与待分类点的距离，按距离递增排序，然后取出前K个点，计算这些点所属标签的数量，计数最高的标签为分类结果。

``` python
#! /data/server/python/bin/python
# -*- coding:utf-8 -*-
"""
k-近邻算法
"""
import math
import operator
from collections import Counter


def knn(position, data_set, labels, k):
    """
    k-近邻算法
    :param position: 待分类点
    :param data_set: 数据样本
    :param labels: 标签集合
    :param k: 取值
    :return: 所属标签
    """
    distance_list = []
    for index, item in enumerate(data_set):
        distance_list.append((
            labels[index],
            math.sqrt(reduce(operator.add, [(v - position[i]) ** 2 for i, v in enumerate(item)]))
        ))
    distance_list = sorted(distance_list, key=lambda x: x, reverse=True)
    result = Counter([val[0] for val in distance_list[:k]])
    result_labels = sorted(result.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
    return result_labels[0][0]


if __name__ == "__main__":
    point = [0.2, 0.3]
    data_set = [[1, 1.1], [1, 1], [0, 0], [0, 0.1]]
    labels = ['A', 'A', 'B', 'B']
    k = 3
    print knn(point, data_set, labels, k)
```

### k-d tree算法
> http://www.cnblogs.com/eyeszjwang/articles/2429382.html
