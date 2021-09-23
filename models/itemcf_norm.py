#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :itemcf_norm.py
@Description  :
@Date         :2021/09/23 14:56:58
@Author       :Arctic Little Pig
@Version      :1.0
'''

from operator import itemgetter

__all__ = ("ItemCF", )


class ItemCF_Norm(object):
    def __init__(self, K: int = 10) -> None:
        super().__init__()
        self.K = K

    def normalize(self, W):
        W_ = dict()
        for i, wij in W.items():
            wi = max(wij.values())
            for j, wj in wij.items():
                W_[i][j] = wj / wi

        return W_

    def Recommendation(self, train, user_id, W):
        W = self.normalize(W)
        rank = dict()
        ru = train[user_id]
        for i, ri in ru.items():
            for j, wj in sorted(W[i].items(), key=itemgetter(1), reverse=True)[0:self.K]:
                if j in ru:
                    continue
                rank[j] += ri * wj

        return rank

    def RecommendationWithReason(self, train, user_id, W):
        W = self.normalize(W)
        rank = dict()
        ru = train[user_id]
        for i, ri in ru.items():
            for j, wj in sorted(W[i].items(), key=itemgetter(1), reverse=True)[0:self.K]:
                if j in ru:
                    continue
                rank[j].weight += ri * wj
                rank[j].reason[i] = ri * wj

        return rank
