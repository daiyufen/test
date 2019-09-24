'''
弹球
version:0.1
author:小雨
date:2019.09.21
'''
from pygame import *
import pygame,sys



def main():
    #初始化部分
    pygame.init()
    size = width,height = 600,400
    screen = pygame.display.set_mode(size)
    speed = [-5,-5]
    black = 0,0,0
    ball = pygame.image.load('./biqiu.jpg')
    ballreact = ball.get_rect()
    fps = 200
    flock = pygame.time.Clock()
    # name = pygame.display.set_captiobn('我的第一个游戏')

    #事件部分
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    speed[1] = speed[1] if speed[1] == 0 else ((abs(speed[1])-1) * int(abs(speed[1]) / speed[1]))
                    print(speed[1])
                elif event.key == pygame.K_LEFT:
                    speed[0] = speed[0] if speed[0] == 0 else ((abs(speed[0]) - 1) * int(speed[0]  / abs(speed[0])))
                    print(speed[0])
                elif event.key == pygame.K_RIGHT:
                    speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0]) + 1)
                elif event.key == pygame.K_UP:
                    speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1]) + 1)
        ballreact = ballreact.move(speed[0],speed[1])
        if ballreact.left < 0 or ballreact.right > width:
            speed[0] = - speed[0]
        if ballreact.top < 0 or ballreact.bottom > height:
            speed[1] = - speed[1]
        #刷新部分
        screen.fill(black)
        screen.blit(ball,ballreact)
        pygame.display.update()
        flock.tick(fps)

if __name__ == '__main__':
    main()

