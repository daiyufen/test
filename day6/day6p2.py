'''
判断回文数
version:0.1
zuthor:小雨
date;2019.09.19
'''


def is_palindrome(n):
    str_n = str(n)
    leng = int(len(str_n))
    for i in range(int(leng / 2 + 1)):
        if str_n[i] == str_n[- i-1]:
            return True
    return False

