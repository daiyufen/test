'''
返回文件后缀名
version:0.1
author:小雨
date:2019.09.20
'''



def get_suffix(filename,is_pos = False):
    pos = filename.rfind('.')
    if 0 < pos < len(filename) -1:
        index = pos if is_pos else pos + 1
        return filename[index:]
    else:
        return '  0'


print(get_suffix('daiyufen'))