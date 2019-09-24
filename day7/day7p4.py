'''
返回列表中最大的两个数
version:0.1
author:小雨
date:2019.09.20
'''
def get_max(x):
    m1 = x[0]
    for index in range(len(x)):
        if x[index] > m1:
            m = x[index]
            x[index] = m1
            m1 =m
    m2 = x[1]
    for i in range(2,len(x)):
        if x[i] > m2:
            m2 = x[i]
    return m1,m2

print(get_max([1,4,5,23,67]))