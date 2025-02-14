import time

import pygame
from distlib.wheel import cache

from main_settings import *

pygame.init() # init and import
pygame.display.set_caption("FactoryZone")
pygame.display.set_icon(pygame.image.load("images/cells/builds/smallter.png"))
scr = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

from saves import save_game, load_game
from windows import opened_windows
from items import items
from map import load_map, map1, ground_map_layer, selected_cells, build_map_layer, auxiliary_map_layer
from player import player, camera
from user_interface import ui_elements, base_hud_init, ui_images, UI_element, clear_pointers

stop = False
version = "pr 1.0"

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

#try:
#    load_game()
#except ValueError:
#    print("load map error")

load_map(map1)
base_hud_init()

debug_font = pygame.font.Font(None, 20)

def rendering(screen):
    global start_render_dt, end_render_dt, render_delta_time
    start_render_dt = time.time()
    draw_queue = ground_map_layer + build_map_layer + items + auxiliary_map_layer + selected_cells
    for obj in draw_queue:
        if obj.rect.midright[0] - camera.offset.x >= 0 and obj.rect.midbottom[1] - camera.offset.y >= 0 and obj.rect.midtop[1] - camera.offset.y <= WINDOW_HEIGHT and obj.rect.midleft[0] - camera.offset.x <= WINDOW_WIDTH:
            screen.blit(obj.image, (obj.rect.x - camera.offset.x, obj.rect.y - camera.offset.y))

    for el in ui_elements:
        screen.blit(el.image, (el.rect.x, el.rect.y))

    for wind in opened_windows:
        screen.blit(wind.image, (wind.rect.x, wind.rect.y))
        for wind_el in wind.window_elements:
            screen.blit(wind_el.image, (wind_el.rect.x, wind_el.rect.y))
        for wind_el in wind.text_window_elements:
            screen.blit(wind_el.render(), wind_el.rect)

    screen.blit(ui_images["vignette"], (0, 0)) # UI_element(ui_images["vignette"], (0 + camera.offset.x, 0 + camera.offset.y))

    if player.debug_mode:
        if fps >= 59: screen.blit(debug_font.render(f"fps: {fps}", True, green), (10, 10))
        if 50 < fps < 59: screen.blit(debug_font.render(f"fps: {fps}", True, yellow), (10, 10))
        elif fps <= 50: screen.blit(debug_font.render(f"fps: {fps}", True, red), (10, 10))
        screen.blit(debug_font.render(f"items: {len(items)}, map_cells: {len(ground_map_layer + build_map_layer + auxiliary_map_layer)}, draw_queue: {len(draw_queue + ui_elements + opened_windows)}", True, black), (10, 30))
        screen.blit(debug_font.render(f"delta_time: all: {delta_time}",True, black), (10, 50))
        screen.blit(debug_font.render(f"delta_time: render: {render_delta_time}",True, black), (10, 70))
        screen.blit(debug_font.render(f"delta_time: update: {update_delta_time}",True, black), (10, 90))

    screen.blit(debug_font.render(f"Pre-release build: {version}",True, red), (WINDOW_WIDTH - 256, WINDOW_HEIGHT-15))

    selected_cells.clear()
    clear_pointers()
    end_render_dt = time.time()
    render_delta_time = end_render_dt - start_render_dt

def update():
    global start_update_dt, end_update_dt, update_delta_time
    start_update_dt = time.time()

    player.update()
    camera.center_camera(player)
    for ui_element in ui_elements:
        ui_element.update()
    for cell in ground_map_layer:
        cell.update()
    for cell in build_map_layer:
        cell.update()
    for cell in auxiliary_map_layer:
        pass
    for item in items:
        item.update()
    for window in opened_windows:
        window.update()

    end_update_dt = time.time()
    update_delta_time = end_update_dt - start_update_dt

while not stop: # main
    start_dt = time.time()
    scr.fill((65,105,225))
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True

    fps = clock.get_fps()

    update()
    if keys[pygame.K_p]:
        save_game()
        print("game saved")

    ###
    ###

    rendering(scr)

    clock.tick(tps)  # тики в секунду
    pygame.display.flip()

    end_dt = time.time()
    delta_time = end_dt - start_dt
# 🙂‍↕️