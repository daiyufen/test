'''
求最大公约数和最小公倍数
version:0.1
author:小雨
date:2019..09.19
'''


def gcd(x, y):
    (x, y) = (x, y) if (x > y) else (y, x)
    for factor in range(y, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x,y):
    return x * y / gcd(x, y)
