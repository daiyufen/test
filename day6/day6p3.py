'''
判断素数
version:0.1
author:小雨
date:2019.09.19
'''


def is_prime(num):
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True

