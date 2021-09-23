#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :similarity.py
@Description  :
@Date         :2021/09/20 20:46:02
@Author       :Arctic Little Pig
@Version      :1.0
'''

import math

__all__ = ("UserSimilarity", )


# 时间复杂度为O(|U|*|U|)，计算资源较多地浪费在计算用户u和用户v的物品交集上，而这个交集|N(u)∩N(v)|通常为0
# def UserSimilarity(train):
#     """
#     Description::

#     :param :
#     :return :

#     Usage::

#     """

#     W = dict()
#     for u in train.keys():
#         for v in train.keys():
#             if u == v:
#                 continue
#             W[u][v] = len(train[u] & train[v])
#     W[u][v] /= math.sqrt(len(train[u]) * len(train[v]) * 1.0)

#     return W


# 两个用户UI热门物品采取过相同的行为不能说明他们的兴趣相似
# def UserSimilarity(train):
#     # build inverse table for item users
#     item_users = dict()
#     for u, items in train.items():
#         for i in items.keys():
#             if i not in item_users:
#                 item_users[i] = set()
#             item_users[i].add(u)
#     # calculate co-rated items between users
#     C = dict()
#     N = dict()
#     for i, users in item_users.items():
#         for u in users:
#             N[u] += 1
#             for v in users:
#                 if u == v:
#                     continue
#                 C[u][v] += 1
#     # calculate finial similarity matrix W
#     W = dict()
#     for u, related_users in C.items():
#         for v, cuv in related_users.items():
#             W[u][v] = cuv / math.sqrt(N[u] * N[v])

#     return W


def UserSimilarity(train):
    """
    Description::
    
    :param train: 用户-物品评分记录训练字典
    :return : 用户之间的相似度矩阵
    
    Usage::
    
    """
    
    # build inverse table for item_users
    item_users = dict()
    for u, items in train.items():
        for i in items.keys():
            if i not in item_users:
                item_users[i] = set()
            item_users[i].add(u)
    # calculate co-rated items between users
    C = dict()
    N = dict()
    for i, users in item_users.items():
        for u in users:
            N[u] += 1
            for v in users:
                if u == v:
                    continue
                C[u][v] += 1 / math.log(1 + len(users))
    # calculate finial similarity matrix
    W = dict()
    for u, related_users in C.items():
        for v, cuv in related_users.items():
            W[u][v] = cuv / math.sqrt(N[u] * N[v])
    
    return W
