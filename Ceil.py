import random

import pygame
import Constants
import math

YScale = 700
XScale = 100
tmp = 200
MAX = math.sqrt(900**2 + 640**2)
T = 0


class Ter(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1, 1))
        self.image.fill(getcol(x, y, Constants.cols)[0])
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x, self.y = x, y
        self.t = int(15 - getcol(x, y, Constants.cols)[1]*65)

    def update(self, day_count):
        if day_count <= 45:
            self.x += random.randint(-20, 20)
            self.y -= random.randint(-20, 40)
        else:
            self.x += random.randint(-40, 30)
            self.y -= random.randint(-30, 10)
        self.image.fill(getcol(self.x, self.y, Constants.cols)[0])



def getcol(x, y, cols):
    col = []
    tmp = MAX / 5
    rx, ry = x, 640 - y
    if ry < 500:
        ry = (abs(ry ** 2) / 500) % 640
    if rx < 810:
        rx = (abs(rx ** 2) / 800) % 900
    alt = math.sqrt((ry**1.35)*math.sqrt(rx))
    for j in range(4):
        if tmp * j <= alt < tmp * (j + 1):
            for i in range(3):
                col.append(int(((alt - j * tmp)/ tmp) * (cols[j + 1][i] - cols[j][i]) + cols[j][i]))
    return col, alt/MAX


class Beach(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1, 1))
        self.image.fill(Constants.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class Sea(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1, 1))
        self.image.fill(Constants.SEA)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class ScaleLine(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((2, 20))
        try:
            self.image.fill(setcolor(x, Constants.cols, XScale, tmp))
        except:
            print('alles OK')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class Border(pygame.sprite.Sprite):

    def __init__(self, x, y, xlen, ylen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((xlen, ylen))
        self.image.fill(Constants.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x + xlen/2, y + ylen/2)

def setcolor(x: int, cols, XScale, tmp):
    alt = x - XScale
    col = []
    for j in range(4):
        if tmp * j <= alt < tmp * (j + 1):
            for i in range(3):
                col.append(int(((alt - j * tmp) / tmp) * (cols[j + 1][i] - cols[j][i]) + cols[j][i]))
        if alt == tmp * (j + 1):
            col.append(Constants.col4)
    col = tuple(col)
    return col
