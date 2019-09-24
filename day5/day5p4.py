'''
生成斐波拉切数列
version:0.1
author:小雨
date:2019.09.19
'''
def fib(n):
    assert n > 0
    if(n <= 2):
        return n
    else:
        return fib(n - 1) + fib(n - 2)
for i in range(1,20):
    print(fib(i),end='\t')