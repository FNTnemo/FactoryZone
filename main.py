import time

import pygame

from main_settings import *

pygame.init()
pygame.display.set_caption("FactoryZone")
pygame.display.set_icon(pygame.image.load("images/cells/builds/smallter.png"))
scr = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

from items import items
from map import load_map, map1, map_cells, selected_cells
from player import player, camera
from user_interface import ui_elements, base_hud_init

stop = False

#time calc
start_dt = 0
end_dt = 0
delta_time = 0

start_render_dt = 0
end_render_dt = 0
render_delta_time = 0

start_update_dt = 0
end_update_dt = 0
update_delta_time = 0


base_hud_init()
load_map(map1)

debug_font = pygame.font.Font(None, 20)

def rendering(screen):
    global start_render_dt, end_render_dt, render_delta_time
    start_render_dt = time.time()
    draw_queue = [map_cells + items + selected_cells]
    for arrays in draw_queue:
        for obj in arrays:
            if obj.rect.midright[0] - camera.offset.x >= 0 and obj.rect.midbottom[1] - camera.offset.y >= 0 and obj.rect.midtop[1] - camera.offset.y <= WINDOW_HEIGHT and obj.rect.midleft[0] - camera.offset.x <= WINDOW_WIDTH:
                screen.blit(obj.image, (obj.rect.x - camera.offset.x, obj.rect.y - camera.offset.y))

    for el in ui_elements:
        screen.blit(el.image, (el.rect.x, el.rect.y))

    screen.blit(debug_font.render(f"fps: {fps}, items: {len(items)}, map_cells: {len(map_cells)}, building_cells: \"Err\", draw_queue: {len(draw_queue[0])}", True, black), (10, 10))
    screen.blit(debug_font.render(f"delta_time: all: {delta_time}",True, black), (10, 30))
    screen.blit(debug_font.render(f"delta_time: render: {render_delta_time}",True, black), (10, 50))
    screen.blit(debug_font.render(f"delta_time: update: {update_delta_time}",True, black), (10, 70))

    selected_cells.clear()
    end_render_dt = time.time()
    render_delta_time = end_render_dt - start_render_dt

def update():
    global start_update_dt, end_update_dt, update_delta_time
    start_update_dt = time.time()
    player.update()
    camera.center_camera(player)
    for ui_element in ui_elements:
        ui_element.update()
    for cell in map_cells:
        cell.update()
    for item in items:
        item.update()
    end_update_dt = time.time()
    update_delta_time = end_update_dt - start_update_dt

while not stop:
    start_dt = time.time()
    scr.fill((0,0,0))
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True

    fps = clock.get_fps()

    update()

    ###
    ###

    rendering(scr)

    clock.tick(tps)  # тики в секунду
    pygame.display.flip()

    end_dt = time.time()
    delta_time = end_dt - start_dt
# 🙂‍↕️