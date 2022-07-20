import pygame
pygame.font.init()
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SEA = (108, 185, 239)

col1 = (225, 206, 57)
col15 = (77, 176, 148)
col2 = (41, 30, 106)
col3 = (142, 16, 142)
col4 = (240, 173, 255)
cols = [col1, col15, col2, col3, col4]

f1 = pygame.font.Font(None, 36)
nums = [f1.render('+15', True, (0, 0, 0)), f1.render('0', True, (0, 0, 0)), f1.render('-15', True, (0, 0, 0)), f1.render('-30', True, (0, 0, 0)), f1.render('-50', True, (0, 0, 0))]

