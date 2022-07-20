import pygame
import COORDS
import Ceil
import Constants
pygame.font.init()

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
Scale = pygame.sprite.Group()
Borders = pygame.sprite.Group()

#MAP RENDER
for i in range(len(Seas)):
    SG.add(Ceil.Sea(Seas[i][1], Seas[i][0]))
for i in range(len(Beaches)):
    BG.add(Ceil.Beach(Beaches[i][1], Beaches[i][0]))
for i in range(len(Terrs)):
    TG.add(Ceil.Ter(Terrs[i][1], Terrs[i][0]))
for i in range(1, 401):
    Scale.add(Ceil.ScaleLine(Ceil.XScale + i * 2, Ceil.YScale))
Borders.add(Ceil.Border(0, 628, 910, 10))
Borders.add(Ceil.Border(900, 0, 10, 638))

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

    screen.fill(Constants.WHITE)
    Scale.draw(screen)
    SG.draw(screen)
    BG.draw(screen)
    TG.draw(screen)
    Borders.draw(screen)
    for i in range(len(Constants.nums)):
        screen.blit(Constants.nums[i], (Ceil.XScale - 10 + i * 200, Ceil.YScale - 35))

    pygame.display.flip()

pygame.quit()
