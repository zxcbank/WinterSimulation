import pygame
import COORDS
import Ceil
import Constants

WIDTH = 1000
HEIGHT = 737
FPS = 30

#COORDS
Seas = COORDS.S_CRDS
Beaches = COORDS.B_CRDS
Terrs = COORDS.T_CRDS

#Groups
SG = pygame.sprite.Group()
BG = pygame.sprite.Group()
TG = pygame.sprite.Group()
tests = pygame.sprite.Group()

#SG
for i in range(len(Seas)):
    SG.add(Ceil.Sea(Seas[i][1], Seas[i][0]))
for i in range(len(Beaches)):
    BG.add(Ceil.Beach(Beaches[i][1], Beaches[i][0]))
for i in range(len(Terrs)):
    TG.add(Ceil.Ter(Terrs[i][1], Terrs[i][0]))
tests.add(Ceil.Test(500, 100))

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Climatic")
clock = pygame.time.Clock()

# Цикл игры
running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(Constants.GREEN)
    SG.draw(screen)
    BG.draw(screen)
    TG.draw(screen)
    pygame.display.flip()

pygame.quit()
