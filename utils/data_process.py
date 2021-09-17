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


def SplitData(data, M, k, seed):
    """
    Description::

    :param :
    :return :

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
