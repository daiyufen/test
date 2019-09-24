'''
判断是否为素数
version:0.1
author:小雨
'''

from math import sqrt

value = int(input('请输入一个正整数：'))
end = int(sqrt(value))
is_prime = True
for x in range(2,end + 1):
    if value % x == 0:
        is_prime = False
        break
if is_prime and value != 1:
    print('%d是素数' % value)
else:
    print('不是素数')

