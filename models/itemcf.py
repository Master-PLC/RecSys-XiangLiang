#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :itemcf.py
@Description  :
@Date         :2021/09/23 14:36:25
@Author       :Arctic Little Pig
@Version      :1.0
'''

from operator import itemgetter

__all__ = ("ItemCF", )


class ItemCF(object):
    def __init__(self, K: int = 10) -> None:
        super().__init__()
        self.K = K

    def Recommendation(self, train, user_id, W):
        rank = dict()
        ru = train[user_id]
        for i, ri in ru.items():
            for j, wj in sorted(W[i].items(), key=itemgetter(1), reverse=True)[0:self.K]:
                if j in ru:
                    continue
                rank[j] += ri * wj

        return rank

    def RecommendationWithReason(self, train, user_id, W):
        rank = dict()
        ru = train[user_id]
        for i, ri in ru.items():
            for j, wj in sorted(W[i].items(), key=itemgetter(1), reverse=True)[0:self.K]:
                if j in ru:
                    continue
                rank[j].weight += ri * wj
                rank[j].reason[i] = ri * wj

        return rank
