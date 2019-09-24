'''
摇色子决定干啥
version:0.1
author:小雨
'''
from random import randint

face = randint(1,6)
if face == 1:
    result = '睡觉'
elif face == 2:
    result = '吃饭'
elif face == 3:
    result = '学习'
elif face == 4:
    result ='看小说'
elif face == 5:
    result = '打游戏'
else:
    result ='继续睡觉觉'
print(result)