import pygame

from main_settings import *

pygame.init()
pygame.display.set_caption("FactoryZone")
pygame.display.set_icon(pygame.image.load("images/smallter.ico"))
scr = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

from items import items
from map import load_map, map1, map_cells, map2, build_cells, selected_cells
from player import player, camera
from user_interface import ui_elements, base_hud_init

stop = False

#base_hud_init()
load_map(map1)

def rendering(screen):
    draw_queue = [map_cells + build_cells + items + selected_cells]
    #rendering

    for arrays in draw_queue:
        for obj in arrays:
            screen.blit(obj.image, (obj.rect.x - camera.offset.x, obj.rect.y - camera.offset.y))

    for el in ui_elements:
        screen.blit(el.image, (el.rect.x, el.rect.y))

    selected_cells.clear()
    draw_queue.clear()

while not stop:
    scr.fill((0,0,0))
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True

    fps = clock.get_fps()

    #update
    player.update()
    camera.center_camera(player)

    for ui_element in ui_elements:
        ui_element.update()
    for cell in map_cells:
        cell.update()
    for cell in build_cells:
        cell.update()
    for item in items:
        item.update()

    ###
    ###

    rendering(scr)

    clock.tick(tps)  # тики в секунду
    pygame.display.flip()

# 🙂‍↕️