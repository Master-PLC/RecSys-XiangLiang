#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :data_process.py
@Description  :
@Date         :2021/09/17 15:18:06
@Author       :Arctic Little Pig
@Version      :1.0
'''

import random

__all__ = ("SplitData", )


def SplitData(data, M, k, seed):
    """
    Description::
    将数据集随机分成训练集和测试集

    :param data: 原始用户-物品评分记录数据
    :param M: 实验总次数
    :param k: 第k次实验
    :param seed: 随机数种子
    :return : 返回用户-物品评分记录训练数据集和测试数据集

    Usage::

    """

    test = []
    train = []
    random.seed(seed)
    for user, item in data:
        if random.randint(0, M) == k:
            test.append([user, item])
        else:
            train.append([user, item])

    return train, test


def RandomSelectNegativeSample(items, items_pool):
    """
    Description::
    
    :param :
    :return :
    
    Usage::
    
    """
    
    ret = dict()
    for i in items.keys():
        ret[i] = 1
    n = 0
    for i in range(0, len(items) * 3):
        item = items_pool[random.randint(0, len(items_pool) - 1)]
        if item in ret:
            continue
        ret[item] = 0
        n += 1
        if n > len(items):
            break

    return ret
