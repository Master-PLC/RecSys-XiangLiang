#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :lfm.py
@Description  :
@Date         :2021/09/24 15:54:40
@Author       :Arctic Little Pig
@Version      :1.0
'''

from ..utils.data_process import RandomSelectNegativeSample


class LFM(object):
    def __init__(self, items_pool, F: int = 4) -> None:
        super().__init__()
        self.items_pool = items_pool
        self.F = F

    def train(self, user_items, N, alpha, ld):
        [P, Q] = self.InitModel(user_items, self.F)
        for step in range(0, N):
            for user, items in user_items.items():
                samples = RandomSelectNegativeSample(items, self.items_pool)
                for item, rui in samples.items():
                    eui = rui - self.Predict(user, item)
                    for f in range(0, self.F):
                            P[][f1 + alpha * (eui[item][f] -
ld P[][f])
q[item][f] + alpha * (eui Pluser][f] -
ld o[item][f1
alpha *= 0
def Recommend(user, P, Q)
rank dict(
for f, puf in Pluse]. items o fax主, 可 fi in 9[]. items()
