# -*- coding: utf-8 -*-
# Created on 2018年8月3日
#
#@author: Administrator
#飞机类，子弹类，游戏类，
import pygame
from pygame.locals import *

class HeroPlane(object):
    def __init__(self, filepath, screen):
        self.x = 186
        self.y = 590
        self.image = pygame.image.load(filepath)
        self.screen = screen
        self.bullet_list = [] #子弹列表
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

    def fire(self):
        x = self.x + 140 / 2 - 11
        y = self.y - 61
        self.bullet_list.append(Bullet(x ,y, self.screen))
        print("x = %d, y = %d" % (x, y))


class Bullet(object):
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.image = pygame.image.load("zidan.png")
        self.screen = screen
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 5

def event_key(hero):
    speed = 10
    global flag
    #获取事件
    for event in pygame.event.get():
        if event.type == QUIT:
            print("exit")
            exit()
        #按键按下情况
        elif event.type == KEYDOWN:
            #按下哪些按键
            if event.key == K_a or event.key == K_LEFT:
                print("left")
                hero.x -= speed
            elif event.key == K_s or event.key == K_DOWN:
                print("down")
                hero.y += speed
            elif event.key == K_d or event.key == K_RIGHT:
                print("RIGHT")
                hero.x += speed
            elif event.key == K_w or event.key == K_UP:
                print("UP")

                hero.y -= speed
            elif event.key == K_SPACE:
                print("space")
                hero.fire()
        elif event.type == KEYUP:
            print('key up')
                
                    
def main():
    max_x, max_y = 512, 768
    #1、创建窗口
    screen = pygame.display.set_mode((max_x, max_y), 0, 32)
    
    #2、背景图片
    background = pygame.image.load("background.jpg")
    #3、飞机贴图
    hero = HeroPlane("feiji.png", screen)

    #初始化音乐
    pygame.mixer.init()
    #播放音乐
    music = pygame.mixer.music.load("game_music.mp3")
    
    pygame.mixer.music.play(100)
    while True:
        #3、设定需要显示的背景图
        screen.blit(background, (0,0))
        hero.display()
        #更新显示内容
        pygame.display.update()
        #监听事件
        event_key(hero)
                    

if __name__ == "__main__":
    main()