import pygame
from main_settings import *

pygame.init()
scr = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

stop = False

while not stop:
    scr.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True



    clock.tick(tps)  # тики в секунду
    pygame.display.flip()
