'''
打印三角形图案
version:0.1
author:小雨
date:2019/9/19
'''

row = int(input('请输入行数:'))
for i in range(row):
    for j in range(i+1):
        print('*',end = '')


print()
for i in range(row):
    for j in range(row):
        if j < row - (i + 1):
            print(' ',end = '')
        else:
            print('*',end = '')
    print()
print()
for i in range(row):
    for j in range(row - i - 1):
        print(' ',end='')
    for k in range(2 * i + 1):
        print('*',end='')
    print()
