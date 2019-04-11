import pygame
import time
from pygame.locals import *
import random
class Base(object):
    def __init__(self, screen_temp, x, y, image_name):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load(image_name)

class BasePlane(Base):
    def __init__(self, screen_temp, x, y, image_name):
        Base.__init__(self, screen_temp, x, y ,image_name)
        self.bullet_list = []  # 存储发射出去的子弹对象引用

    def display(self):
        self.screen.blit(self.image,(self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bullet_list.remove(bullet)

class HeroPlane(BasePlane):
    def __init__(self, screen_temp):
        BasePlane.__init__(self, screen_temp, 160, 710, "./Resources/feiji.png")

    def move_left(self):
        self.x -= 15

    def move_right(self):
        self.x += 15

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))

class EnemyPlane(BasePlane):
    def __init__(self, screen_temp):
        BasePlane.__init__(self, screen_temp, 0, 35, "./Resources/diji.png")
        self.direction = 'right'

    def move(self):
        if self.x  > 350:
            self.direction = 'left'
        elif self.x < 0:
            self.direction = 'right'

        if self.direction == 'left':
            self.x -= 5
        elif self.direction == 'right':
            self.x += 5

    def fire(self):
        random_num = random.randint(1, 100)
        if random_num == 2 or random_num == 99:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))

class BaseBullet(Base):
    def display(self):
        self.screen.blit(self.image,(self.x, self.y))

class Bullet(BaseBullet):
    def __init__(self, screen_temp, x, y):
        BaseBullet.__init__(self, screen_temp, x+70, y, "./Resources/bullet.jpg")

    def move(self):
        self.y -= 5

    def judge(self):
        if self.y < 10:
            return True
        else:
            return False

class EnemyBullet(BaseBullet):
    def __init__(self, screen_temp, x, y):
        BaseBullet.__init__(self, screen_temp, x + 55, y + 100, "./Resources/bullet.jpg")

    def move(self):
        self.y += 5

    def judge(self):
        if self.y > 810:
            return True
        else:
            return False

def key_control(hero_temp):
    # 获取事件，比如按键等
    for event in pygame.event.get():
        # 判断是否是点击了对出按钮
        if event.type == QUIT:
            print("exxit")
            exit()
        # 判断是否是按下了键
        elif event.type == KEYDOWN:
            # 检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                hero_temp.move_left()
            # 检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                hero_temp.move_right()
            # 检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                hero_temp.fire()
"""
搭建界面，主要完成窗口和背景图的显示
"""
def main():
    #1.创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480,852),0,32)
    #2.创建一个和窗口大小相同的图片，用来充当背景
    background = pygame.image.load("./Resources/background.jpg")
    #3.创建一个飞机对象
    hero = HeroPlane(screen)
    #4.创建一个敌机对象
    enemy = EnemyPlane(screen)
    #把背景图片放到窗口中显示
    while True:
        #设定需要显示的背景图
        screen.blit(background,(0,0))
        hero.display()
        enemy.display()
        enemy.move()#调用敌机的移动方法
        enemy.fire()
        #更新需要显示的内容
        pygame.display.update()
        key_control(hero)
        time.sleep(0.01)
if __name__ == "__main__":
    main()