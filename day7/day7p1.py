'''
在屏幕s上显示跑马灯文字
version:0.1
author:小雨
date:2019.09.20
'''

import os
import time
def main():
    content = '北京欢迎你'
    while True:
        # os.system('cls')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]



if __name__ == '__main__':
    main()
