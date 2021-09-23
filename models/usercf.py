#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :UserCF.py
@Description  :
@Date         :2021/09/22 14:27:23
@Author       :Arctic Little Pig
@Version      :1.0
'''

from operator import itemgetter

__all__ = ("UserCF", )


class UserCF(object):
    def __init__(self, K: int = 80) -> None:
        super().__init__()
        self.K = K

    def Recommend(self, user, train, W):
        rank = dict()
        interacted_items = train[user]
        for v, wuv in sorted(W[user].items(), key=itemgetter(1), reverse=True)[0:self.K]:
            for i, rvi in train[v].items():
                if i in interacted_items:
                    # we should filter items user interacted before
                    continue
                rank[i] += wuv * rvi

        return rank
