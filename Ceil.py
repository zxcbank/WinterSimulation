import pygame
import Constants


class Ter(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1, 1))
        self.image.fill(Constants.WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


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

class Test(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(Constants.GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
