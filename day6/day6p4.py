'''
判断素数
version:0.1
author:小雨
date:2019.09.19
'''


from day6p3 import is_prime
from day6p2 import is_palindrome


if __name__ == '__main__':
    num = int(input('请输入一个整数'))
    if is_prime(num) and is_palindrome(num):
        print('%d是回文素数' % num)
