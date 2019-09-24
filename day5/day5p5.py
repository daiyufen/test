'''
Craps赌博游戏
version:0.1
author:小雨
'''

from random import randint

first_num = randint(1, 6)
sec_num = randint(1, 6)
is_go_on = False
print('第一次玩家摇出了%d点' % (first_num + sec_num))
if first_num + sec_num == 7 or first_num + sec_num == 11:
    print('玩家获胜')
elif first_num + sec_num == 2 or first_num + sec_num == 3 or first_num + sec_num == 12:
    print('玩家失败')
else:
    is_go_on = True
    print('游戏继续')
    i = 2
    while is_go_on:
        first_num1 = randint(1, 6)
        sec_num1 = randint(1, 6)
        print('第%d次摇出了%d' % (i, (first_num1 + sec_num1)))
        if (first_num1 + sec_num1 == 6):
            print('玩家失败')
            is_go_on = False
        elif (first_num1 + sec_num1 == first_num + sec_num):
            print('游戏成功')
            is_go_on = False
        else:
            i += 1
            is_go_on = True
