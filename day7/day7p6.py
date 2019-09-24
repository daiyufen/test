'''
打印杨辉三角形
version:0.1
author:小雨
date:2019.09.20
'''
def countdown(n):
    print('倒计时：%s' % n)
    while n > 0:
        yield n
        n -= 1
    return

for i in countdown(10):
    print(i)