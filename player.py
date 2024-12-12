import pygame.sprite

from main_settings import *
from map import get_selected_cell, build_cells, Cell, cell_types, cell_images, cell_size


class Player():
    def __init__(self, pos):
        super().__init__()
        self.rect = pygame.Rect(pos[0], pos[1], 10, 10)
        self.velocity = 6
        self.directional = pygame.math.Vector2(0, 0)

        self.selected_structure_type = "empty"

        self.destroy_delay_start = 40
        self.destroy_delay = self.destroy_delay_start

        self.build_delay_start = 10
        self.build_delay = self.build_delay_start

        self.can_move = True
        self.build_flag = True

    def update(self):
        self.movement()

    def movement(self):
        keys = pygame.key.get_pressed()
        if self.can_move:
            if keys[pygame.K_w]:
                self.directional.y = 1
                self.rect.y -= self.velocity
                if self.map_collide_check():
                    self.rect.y += self.velocity
            if keys[pygame.K_s]:
                self.directional.y = -1
                self.rect.y += self.velocity
                if self.map_collide_check():
                    self.rect.y -= self.velocity
            if keys[pygame.K_a]:
                self.directional.x = 1
                self.rect.x -= self.velocity
                if self.map_collide_check():
                    self.rect.x += self.velocity
            if keys[pygame.K_d]:
                self.directional.x = -1
                self.rect.x += self.velocity
                if self.map_collide_check():
                    self.rect.x -= self.velocity

    def map_collide_check(self):
        from map import map_cells
        for cell in map_cells:
            if self.rect.colliderect(cell.rect) and cell.collide:
                return True
        return False

    def map_border_check(self):
        from map import get_map_size, loaded_map
        if self.rect.x >= HALF_WINDOW_HEIGHT and self.rect.x <= get_map_size(loaded_map)[0] - HALF_WINDOW_HEIGHT:
            return True
        if self.rect.y >= HALF_WINDOW_HEIGHT and self.rect.y <= get_map_size(loaded_map)[1] - HALF_WINDOW_HEIGHT:
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