import pygame.sprite

from main_settings import *
from map import get_selected_cell, get_cell


class Player():
    def __init__(self, pos):
        super().__init__()
        self.rect = pygame.Rect(pos[0], pos[1], 10, 10)
        self.velocity = player_velocity
        self.directional = pygame.math.Vector2(0, 0)

        self.selected_structure = "empty"

        self.destroy_delay_start = 40
        self.destroy_delay = self.destroy_delay_start

        self.build_delay_start = 1
        self.build_delay = self.build_delay_start

        self.storage_inventory = []

        self.can_move = True
        self.build_flag = True
        self.P_flag = False
        self.O_flag = False
        self.remove_file_delay_start = 512
        self.remove_file_delay = self.remove_file_delay_start
        self.debug_mode = False

    def update(self, keys, k):
        if keys[pygame.K_F3]:
            self.debug_mode = True
        else: self.debug_mode = False
        self.movement(keys, k)
        self.pipette()

    def movement(self, keys, k):
        if self.can_move:
            if keys[pygame.K_w]:
                self.directional.y = 1
                self.rect.y -= self.velocity * k
                if self.map_collide_check():
                    self.rect.y += self.velocity * k
            if keys[pygame.K_s]:
                self.directional.y = -1
                self.rect.y += self.velocity * k
                if self.map_collide_check():
                    self.rect.y -= self.velocity * k
            if keys[pygame.K_a]:
                self.directional.x = 1
                self.rect.x -= self.velocity * k
                if self.map_collide_check():
                    self.rect.x += self.velocity * k
            if keys[pygame.K_d]:
                self.directional.x = -1
                self.rect.x += self.velocity * k
                if self.map_collide_check():
                    self.rect.x -= self.velocity * k

    def pipette(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q] and get_selected_cell() is not None:
            build_layer_cell = get_cell(get_selected_cell().rect.x, get_selected_cell().rect.y,2)
            if build_layer_cell is not None:
                from user_interface import ui_elements
                if build_layer_cell.type == "air":
                    if self.selected_structure != "empty":
                        self.selected_structure.put()
                    return
                for ui_el in ui_elements:
                    if ui_el.type == build_layer_cell.type:
                        if self.selected_structure != "empty":
                            self.selected_structure.put()
                        ui_el.take()
                        self.selected_structure.rotate_building(build_layer_cell.direction)


    def map_collide_check(self):
        from map import ground_map_layer
        for cell in ground_map_layer:
            if self.rect.colliderect(cell.rect) and cell.collide:
                return True
        return False

    def map_border_check(self):
        from map import get_map_size, loaded_map
        if HALF_WINDOW_HEIGHT <= self.rect.x <= get_map_size(loaded_map)[0] - HALF_WINDOW_HEIGHT:
            return True
        if HALF_WINDOW_HEIGHT <= self.rect.y <= get_map_size(loaded_map)[1] - HALF_WINDOW_HEIGHT:
            return True
        return False


class Camera:
    def __init__(self):
        self.display_serf = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.camera_box_borders = {"left": 500, "right": 500, "top": 200, "bottom": 200}

        self.left = self.camera_box_borders["left"]
        self.top = self.camera_box_borders["top"]
        self.width = WINDOW_WIDTH - (self.camera_box_borders["left"] + self.camera_box_borders["right"])
        self.height = WINDOW_HEIGHT - (self.camera_box_borders["top"] + self.camera_box_borders["bottom"])
        self.camera_box_rect = pygame.Rect(self.left, self.top, self.width, self.height)

        # camera shake
        self.camera_shake_offset = pygame.math.Vector2

    def center_camera(self, target):
        from map import loaded_map, get_map_size
        #if target.position.x - HALF_WINDOW_WIDTH >= 0 and target.position.x - get_map_size(loaded_map)[0]:
        self.offset.x = target.rect.x - HALF_WINDOW_WIDTH
        #if target.position.y - HALF_WINDOW_HEIGHT >= 0 and target.position.y - get_map_size(loaded_map)[1]:
        self.offset.y = target.rect.y - HALF_WINDOW_HEIGHT

camera = Camera()
player = Player((400, 400))