'''
选择排序
version:0.1
author:小雨
date:2019.09.22
'''

import random

def select_sort(seq):
    n = len(seq)
    for i in range(n):
        min = i
        for j in range(i + 1,n):
            if seq[j] < seq[min]:
                min = j
        if min != i:
            seq[min], seq[i] = seq[i], seq[min]
    return seq

seq = list(range(20,30))
random.shuffle(seq)
print(select_sort(seq))
