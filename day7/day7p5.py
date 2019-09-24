'''
计算指定年月日是这一年的第几天
version:0.1
author:小雨
date:2019.09.20
'''

def is_leapyear(year):
    return year % 4 == 0 and year % 100 ==0 or year % 400 == 0

def which_day(year,month,day):
    if is_leapyear(year):
        day_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        day_of_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    for index in range(month - 1):
        total += day_of_month[index]
    return total + day
print(which_day(2000,3,1))