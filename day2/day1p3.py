'''
判断是否是闰年
version:0,1
author:小雨
'''

year = int(input('请输入年份:'))
is_leap = (year % 4 == 0 & year % 100 != 0 or year % 400 == 0)
print(is_leap)