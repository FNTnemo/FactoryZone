import pygame
from main_settings import *

pygame.init()
scr = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

from map import load_map, map1, map_cells, map2
from player import player, camera

stop = False

load_map(map1)

def rendering(screen):
    draw_queue = [map_cells]
    #rendering
    for arrays in draw_queue:
        for obj in arrays:
            screen.blit(obj.image, (obj.rect.x - camera.offset.x, obj.rect.y - camera.offset.y))

    draw_queue.clear()

while not stop:
    scr.fill((215,209,203))
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            stop = True

    fps = clock.get_fps()

    player.update()
    for cell in map_cells:
        cell.update()
    camera.center_camera(player)

    ###
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        load_map(map2)

    ###
    rendering(scr)

    pygame.draw.rect(scr, "green", player.rect)

    clock.tick(tps)  # тики в секунду
    pygame.display.flip()

