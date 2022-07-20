import pygame
import COORDS
import Ceil
import Constants
import time

pygame.font.init()

WIDTH = 1000
HEIGHT = 737
FPS = 12

f2 = pygame.font.Font(None, 36)

# COORDS
Seas = COORDS.S_CRDS
Beaches = COORDS.B_CRDS
Terrs = COORDS.T_CRDS

# Groups
SG = pygame.sprite.Group()
BG = pygame.sprite.Group()
TG = pygame.sprite.Group()
Scale = pygame.sprite.Group()
Borders = pygame.sprite.Group()

# MAP RENDER
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
t_in_point = ""

mon = 'DEC'
day_count = 1
day = 1

start = time.time()
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # time update
    TG.update(day_count)
    if day_count == 31:
        mon = 'JAN'
        day -= 31
        print('jan')
    if day_count == 62:
        mon = 'FEB'
        day -= 31
        print('feb')
    day_count += 1
    day += 1
    print(day_count)

    date = str(day) + mon
    # temperature in point
    x, y = pygame.mouse.get_pos()
    for _ in TG:
        if _.rect.x == x and _.rect.y == y:
            t_in_point = f2.render(str(_.t) + ", " + date, True, (0, 0, 0))
    # RENDER
    screen.fill(Constants.WHITE)
    Scale.draw(screen)
    SG.draw(screen)
    BG.draw(screen)
    TG.draw(screen)
    Borders.draw(screen)

    if t_in_point:
        screen.blit(t_in_point, (25, 25))
    for i in range(len(Constants.nums)):
        screen.blit(Constants.nums[i], (Ceil.XScale - 10 + i * 200, Ceil.YScale - 35))

    pygame.display.flip()

pygame.quit()
