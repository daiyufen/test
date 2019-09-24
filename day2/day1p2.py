'''
输入半径计算圆的周长和面积
version:0.1
author:xiaoyu
'''
import math
r = float(input('请输入半径：'))
perimeter = 2 * math.pi * r
area = math.pi * r ** 2
print('圆的周长是：%.2f' % perimeter)
print('圆的面积是：%.2f' % area)
