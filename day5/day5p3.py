'''
百钱百鸡
version:0.1
author:小雨
date:2019.09.19
'''

for i in range(1,20):
    for j in range(1,33):
        k = 100 - i - j
        if(k % 3 == 0 and (5 * i +3 * j + k / 3) == 100):
            print('公鸡%d只,母鸡%d只,小鸡%d只' % (i,j,k))
           