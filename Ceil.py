import pygame
import Constants
import math

YScale = 700
XScale = 100
tmp = 200
MAX = math.sqrt(900**2 + 640**2)



class Ter(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1, 1))
        try:
            self.image.fill(getcol(x, y, Constants.cols))
        except:
            print('err', x, y)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.t = 0

def getcol(x, y, cols):
    col = []
    tmp = MAX / 5
    rx, ry = x, 640 - y
    if rx < 800:
        rx = rx**2/800
    if ry < 300:
        ry = ry**2/300
    alt = math.sqrt((ry**1.44)*math.sqrt(rx))
    if 0 <= alt < tmp:
        for i in range(3):
            col.append(int((alt / tmp) * (cols[1][i] - cols[0][i]) + cols[0][i]))
            #print('1', (alt / tmp))
    if tmp <= alt < 2 * tmp:
        for i in range(3):
            col.append(int(((alt - tmp) / tmp) * (cols[2][i] - cols[1][i]) + cols[1][i]))
            #print('2', (alt - tmp / tmp))
    if 2 * tmp <= alt < 3 * tmp:
        for i in range(3):
            col.append(int(((alt - 2 * tmp )/ tmp) * (cols[3][i] - cols[2][i]) + cols[2][i]))
            #print('3', (alt - 2 * tmp / tmp))
    if 3 * tmp <= alt <= 4 * tmp:
        for i in range(3):
            col.append(int(((alt - 3 * tmp) / tmp) * (cols[4][i] - cols[3][i]) + cols[3][i]))
            #print('4', (alt - 3 * tmp / tmp))
    return col


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
        self.image.fill(setcolor(x, Constants.cols, XScale, tmp))
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
    realx = x - XScale
    col = []
    if realx < tmp:
        for i in range(3):
            col.append(int((realx / tmp) * (cols[1][i] - cols[0][i]) + cols[0][i]))
    if tmp <= realx < 2 * tmp:
        for i in range(3):
            col.append(int(((realx - tmp) / tmp) * (cols[2][i] - cols[1][i]) + cols[1][i]))
    if 2*tmp <= realx < 3*tmp:
        for i in range(3):
            col.append(int(((realx - 2*tmp) / tmp) * (cols[3][i] - cols[2][i]) + cols[2][i]))
    if 3*tmp <= realx <= 4*tmp:
        for i in range(3):
            col.append(int(((realx - 3*tmp) / tmp) * (cols[4][i] - cols[3][i]) + cols[3][i]))
    col = tuple(col)
    return col
