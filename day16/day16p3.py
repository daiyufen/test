'''
插入排序
version:0.1
author:小雨
date:2019.09.22
'''
import random

def insert_sort(seq):
    n = len(seq)
    for i in range(1,n):
        value = seq[i]
        post = i
        while post > 0 and value < seq[post - 1]:
            seq[post] = seq[post - 1]
            post -= 1
        seq[post] = value
    return seq


seq = list(range(20,30))
random.shuffle(seq)
print(insert_sort(seq))
