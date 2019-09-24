'''
寻找水仙花数
version:0.1
author:小雨
date:2019.0.19
'''

#
for  value in range(100,1000):
    a = int(value / 100)
    b = int(value / 10 % 10)
    c = int(value % 10)
    if(value == a ** 3 + b ** 3 + c ** 3):
        print(value)

