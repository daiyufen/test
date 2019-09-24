'''
冒泡排序
version:0.1
author:小雨
date:2019.09.22
'''

import random


def bubble_sort(seq ):
    n = len(seq)
    for i in range(n - 1):
        for j in range(n-i-1):
            if seq[j] > seq[j+1]:
                seq[j+1],seq[j] = seq[j],seq[j+1]
    return seq

seq = list(range(10,20))
random.shuffle(seq)
print(type(seq))
print(bubble_sort(seq))

