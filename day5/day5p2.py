'''
寻找完美数
version:0.1
author:小雨
date:2019.09.19
'''

import math



for num in range(1,10000):
    sum = 0
    for i in range(1,int(math.sqrt(num)) + 1):
        if(num % i == 0):
            sum +=  i
            if i > 1 and num // i != i:
                sum += num // i
    if(num == sum):
        print(num)

for num in range(1, 10000):
    result = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            result += factor
            if factor > 1 and num // factor != factor:
                result += num // factor
    if result == num:
        print(num)