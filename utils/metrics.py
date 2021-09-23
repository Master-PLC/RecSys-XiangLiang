#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :metrics.py
@Description  :
@Date         :2021/09/17 15:15:21
@Author       :Arctic Little Pig
@Version      :1.0
'''

import math

__all__ = ("Recall", "Precision", "Coverage", "Popularity", )


def Recall(train, test, N):
    """
    Description::
    召回率，描述有多少比例的用户-物品评分记录包含在最终的推荐列表中

    :param train: 用户-物品评分记录训练字典
    :param test: 用户-物品评分记录测试字典
    :param N: 推荐物品个数
    :return : 返回召回率

    Usage::

    """

    hit = 0
    all = 0
    for user in train.keys():
        tu = test[user]
        rank = GetRecommendation(user, N)
        for item, pui in rank:
            if item in tu:
                hit += 1
        all += len(tu)

    return hit / (all * 1.0)


def Precision(train, test, N):
    """
    Description::
    准确率，描述最终的推荐列表中有多少比例是发生过的用户-物品评分记录

    :param train: 用户-物品评分记录训练字典
    :param test: 用户-物品评分记录测试字典
    :param N: 推荐物品个数
    :return : 返回准确率

    Usage::

    """

    hit = 0
    all = 0
    for user in train.keys():
        tu = test[user]
        rank = GetRecommendation(user, N)
        for item, pui in rank:
            if item in tu:
                hit += 1
        all += N

    return hit / (all * 1.0)


def Coverage(train, test, N):
    """
    Description::
    覆盖率，表示最终的推荐列表中包含多大比例的物品

    :param train: 用户-物品评分记录训练字典
    :param test: 用户-物品评分记录测试字典
    :param N: 推荐物品个数
    :return : 返回覆盖率

    Usage::

    """

    recommend_items = set()
    all_items = set()
    for user in train.keys():
        for item in train[user].keys():
            all_items.add(item)
        rank = GetRecommendation(user, N)
        for item, pui in rank:
            recommend_items.add(item)

    return len(recommend_items) / (len(all_items) * 1.0)


def Popularity(train, test, N):
    """
    Description::
    新颖度，通过推荐列表中物品的平均流行度进行度量。其中，平均流行度的计算将对每个物品的流行度取对事，这是因为物品的流行度分布满足长尾分布

    :param train: 用户-物品评分记录训练字典
    :param test: 用户-物品评分记录测试字典
    :param N: 推荐物品个数
    :return : 返回新颖度

    Usage::

    """

    item_popularity = dict()
    for user, items in train.items():
        for item in items.keys():
            if item not in item_popularity:
                item_popularity[item] = 0
            item_popularity[item] += 1

    ret = 0
    n = 0
    for user in train.keys():
        rank = GetRecommendation(user, N)
        for item, pui in rank:
            ret += math.log(1 + item_popularity[item])
            n += 1
    ret /= n * 1.0

    return ret
