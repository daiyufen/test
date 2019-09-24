'''
函数生成指定长度验证码，有英文和字母组成
version:0.1
author:小雨
date:2019.09.20
'''

from random import randint

def generate_code(code_len = 4):
    all_code = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_post = len(all_code) - 1
    code = ''
    for _ in range(code_len):
        index = randint(0,last_post)
        code += all_code[index]
    return code

print(generate_code())
