import time
import pygame
from pygame import Rect

from main_settings import *

pygame.init() # init and import
pygame.display.set_caption("FactoryZone")
pygame.display.set_icon(pygame.image.load("images/cells/builds/smallter.png"))
pygame.mouse.set_visible(False)
scr = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()

virtual_screen_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))

from saves import save_game, load_game, del_save_file, saves_path
from windows import opened_windows
from items import items
from map import ground_map_layer, selected_cells, build_map_layer, auxiliary_map_layer, chunks
from player import player, camera
from user_interface import ui_elements, base_hud_init, ui_images, clear_pointers, gui_images

stop = False
version = "Release 1.2: optimization update"

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

load_game()
#load_map(map1)
base_hud_init()

debug_font = pygame.font.Font(None, 20)

def rendering(virtual_screen, screen):
    global start_render_dt, end_render_dt, render_delta_time
    start_render_dt = time.time()
    draw_queue = ground_map_layer + build_map_layer + items + auxiliary_map_layer + selected_cells
    for obj in draw_queue:
        if ((obj.rect.midright[0] - camera.offset.x >= 0 and obj.rect.midbottom[1] - camera.offset.y >= 0 and
            obj.rect.midtop[1] - camera.offset.y <= WINDOW_HEIGHT and obj.rect.midleft[0] - camera.offset.x <= WINDOW_WIDTH)
                and obj.type != "air"):
            virtual_screen.blit(obj.image, (obj.rect.x - camera.offset.x, obj.rect.y - camera.offset.y))

    for el in ui_elements:
        virtual_screen.blit(el.image, (el.rect.x, el.rect.y))

    for wind in opened_windows:
        virtual_screen.blit(wind.image, (wind.rect.x, wind.rect.y))
        for wind_el in wind.window_elements:
            virtual_screen.blit(wind_el.image, (wind_el.rect.x, wind_el.rect.y))
        for wind_el in wind.text_window_elements:
            virtual_screen.blit(wind_el.render(), wind_el.rect)

    virtual_screen.blit(gui_images["cursor"], pygame.mouse.get_pos())
    virtual_screen.blit(ui_images["vignette"], (0, 0)) # UI_element(ui_images["vignette"], (0 + camera.offset.x, 0 + camera.offset.y))

    if player.debug_mode:
        if fps >= 59: virtual_screen.blit(debug_font.render(f"fps: {fps}", True, green), (10, 10))
        if 50 < fps < 59: virtual_screen.blit(debug_font.render(f"fps: {fps}", True, yellow), (10, 10))
        elif fps <= 50: virtual_screen.blit(debug_font.render(f"fps: {fps}", True, red), (10, 10))
        virtual_screen.blit(debug_font.render(f"items: {len(items)}, map_cells: {len(ground_map_layer + build_map_layer + auxiliary_map_layer)}, draw_queue: {len(draw_queue + ui_elements + opened_windows)}", True, black), (10, 30))
        virtual_screen.blit(debug_font.render(f"delta_time: all: {delta_time}",True, black), (10, 50))

        dtr_bar = pygame.Surface(((delta_time / 100 * render_delta_time * 100000000), 20))
        dtr_bar.fill(green)
        dtr_bar.set_alpha(128)
        virtual_screen.blit(dtr_bar, (10, 70))

        dtu_bar = pygame.Surface(((delta_time / 100 * update_delta_time * 100000000), 20))
        dtu_bar.fill(green)
        dtu_bar.set_alpha(128)
        virtual_screen.blit(dtu_bar, (10, 90))

        dt_bar = pygame.Surface(((delta_time / 100 * delta_time * 100000000), 20))
        dt_bar.fill(red)
        dt_bar.set_alpha(128)
        virtual_screen.blit(dt_bar, (10, 110))

        for c in chunks:
            pygame.draw.rect(virtual_screen, (0, 0, 255),
                             Rect(c.rect.x - camera.offset.x, c.rect.y - camera.offset.y, chunk_size_global, chunk_size_global), 1)

        virtual_screen.blit(debug_font.render(f"delta_time: render: {render_delta_time}",True, black), (render_delta_time / delta_time * 100 + 15, 70))
        virtual_screen.blit(debug_font.render(f"delta_time: update: {update_delta_time}",True, black), (update_delta_time / delta_time * 100 + 15, 90))

    if player.remove_file_delay < player.remove_file_delay_start:
        virtual_screen.blit(debug_font.render(f"There are {player.remove_file_delay * 100 // player.remove_file_delay_start}% left before the save is deleted",True, red), (WINDOW_WIDTH - 512, WINDOW_HEIGHT - 15))
    virtual_screen.blit(debug_font.render(f"Build: {version}",True, green), (WINDOW_WIDTH - 230, WINDOW_HEIGHT-15))

    #coursor

    screen.blit(pygame.transform.scale(virtual_screen, current_window_size) , (0, 0))
    selected_cells.clear()

    clear_pointers()
    end_render_dt = time.time()
    render_delta_time = end_render_dt - start_render_dt

def update(keys):
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
    #for cell in auxiliary_map_layer:
    #    pass
    for item in items:
        item.update()
    for window in opened_windows:
        window.update()

    if keys[pygame.K_p] and not player.P_flag: # save button
        save_game()
        print("game saved")
        player.P_flag = True
    if not keys[pygame.K_p]: player.P_flag = False
    if keys[pygame.K_o] and not player.O_flag: # remove save file button
        if player.remove_file_delay <= 0:
            del_save_file(saves_path, "save.fz")
            print("save file removed")
            player.O_flag = True
            player.remove_file_delay = player.remove_file_delay_start
        else:
            player.remove_file_delay -= 1
    if not keys[pygame.K_o]:
        player.O_flag = False
        player.remove_file_delay = player.remove_file_delay_start

    end_update_dt = time.time()
    update_delta_time = end_update_dt - start_update_dt

while not stop: # main
    start_dt = time.time()
    virtual_screen_surface.fill((65,105,225))
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #save_game() # autosave
            stop = True
        if event.type == pygame.VIDEORESIZE:
            current_window_size = event.size

    fps = clock.get_fps()
    update(keys)

    ###

    ###

    rendering(virtual_screen_surface, scr)
    clock.tick(tps)  # тики в секунду
    pygame.display.flip()

    end_dt = time.time()
    delta_time = end_dt - start_dt
# 🙂‍↕️