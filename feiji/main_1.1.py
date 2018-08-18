# -*- coding: utf-8 -*-
# Created on 2018年8月3日
#
#@author: Administrator
#飞机类，子弹类
import pygame
from pygame.locals import *
import random

#飞机基类
class BasePlane(object):
    def __init__(self, filepath, screen, x, y):
            self.x = x
            self.y = y
            self.image = pygame.image.load(filepath)
            self.screen = screen
            self.bullet_list = [] #子弹列表

#玩家飞机
class HeroPlane(BasePlane):
    def __init__(self, filepath, screen, x, y):
        super().__init__(filepath, screen, x, y)
        self.speed = 10
    
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            #删除窗口外的子弹
            if bullet.y < 0:
                self.bullet_list.remove(bullet)

    def move_left(self):
        self.x -= self.speed
        if self.x < 0:
            self.x = 0

    def move_right(self):
        self.x += self.speed
        if self.x > 372:
            self.x = 372

    def move_up(self):
        self.y -= self.speed
        if self.y < 0:
            self.y = 0

    def move_down(self):
        self.y += self.speed
        if self.y > 590:
            self.y = 590

    def fire(self):
        x = self.x + 140 / 2 - 11
        y = self.y - 61
        self.bullet_list.append(HeroBullet(x ,y, self.screen))
        print("x = %d, y = %d" % (x, y))

#敌人飞机
class EnemyPlane(BasePlane):
    def __init__(self, filepath, screen, x, y):
        super().__init__(filepath, screen, x, y)
        self.direction = "right"

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            #删除窗口外的子弹
            if bullet.y > 768:
                self.bullet_list.remove(bullet)

    
    def move(self):
        if self.direction == "right":
            self.x += 1
        elif self.direction == "left":
            self.x -= 1

        if self.x < 0:
            self.direction = "right"
        elif self.x > 109:
            self.direction = "left"


    def fire(self):
        x = self.x + 403 / 2 - 11
        y = self.y + 253
        r = random.randint(1, 100)
        if r == 8 or r == 88:
            self.bullet_list.append(EnemyBullet(x ,y, self.screen))

#子弹基类
class BaseBullet(object):
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.image = pygame.image.load("zidan.png")
        self.screen = screen
        
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

#玩家飞机子弹
class HeroBullet(BaseBullet):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)

    def move(self):
        self.y -= 5

#敌人飞机子弹
class EnemyBullet(BaseBullet):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)

    def move(self):
        self.y += 5

def event_key(hero):
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
                hero.move_left()
            elif event.key == K_s or event.key == K_DOWN:
                print("down")
                hero.move_down()
            elif event.key == K_d or event.key == K_RIGHT:
                print("RIGHT")    
                hero.move_right()
            elif event.key == K_w or event.key == K_UP:
                print("UP")
                hero.move_up()
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
    hero = HeroPlane("feiji.png", screen, 186, 590)
    enemy = EnemyPlane("enemy.png", screen, 0, 0)
    #初始化音乐
    pygame.mixer.init()
    #播放音乐
    music = pygame.mixer.music.load("game_music.mp3")
    
    pygame.mixer.music.play(100)
    while True:
        #3、设定需要显示的背景图
        screen.blit(background, (0,0))
        hero.display()
        #显示敌机
        enemy.display()
        enemy.move()
        enemy.fire()
        #更新显示内容
        pygame.display.update()
        #监听事件
        event_key(hero)
                    

if __name__ == "__main__":
    main()