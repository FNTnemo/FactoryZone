import pygame

from main_settings import WINDOW_WIDTH, WINDOW_HEIGHT
from map import cell_images, cell_types, cell_size
from player import camera, player
from windows import Window, window_types

ui_images = {"vignette": pygame.image.load("images/hud/vignette.png").convert_alpha()}

ui_elements = []

open_structures = ["drill-electric", "smelter-base", "conveyor", "conveyor-angular", "connector-input", "connector-output"]

class UI_element(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.elt = "ui"

        self.rect = self.image.get_rect(topleft=pos)
        self.type = "UI"

        self.pos = pygame.math.Vector2(pos)

    def rescale(self):
        size = self.image.get_size
        k = size[0] // WINDOW_WIDTH
        if k != 0:
            pygame.transform.scale(self.image, size[0] * k, size[1] * k)

    def update(self):
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

class SelectableItemUI(pygame.sprite.Sprite):
    def __init__(self, typei, pos):
        super().__init__()
        self.elt = "item"
        self.type0 = typei[0]
        self.type = self.type0
        self.building_type = self.type0.split("-")[0]

        self.direction = 0
        self.last_direction = self.direction

        self.image0 = cell_types[self.type0][1][0]
        self.image = self.image0

        self.rect = self.image.get_rect(topleft=pos)

        self.x0 = self.rect.x
        self.y0 = self.rect.y

        self.selected = False
        self.r_pressed = False

    def update(self):
        m_keys = pygame.mouse.get_pressed()
        k_keys = pygame.key.get_pressed()

        if m_keys[0] and player.selected_structure == "empty":
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_x, mouse_y):
                player.build_flag = False
                self.take()
        if k_keys[pygame.K_ESCAPE]:
            self.put()

        if self.selected:
            #rotate
            if not k_keys[pygame.K_r]:
                self.r_pressed = False
            if k_keys[pygame.K_r] and not self.r_pressed:
                self.r_pressed = True

                if self.type == "conveyor" or self.building_type == "connector" or self.building_type == "drill": # 4 states
                    self.direction += 1
                    if self.direction > 3:
                        self.direction = 0

                    self.rotate_building(self.direction)

                elif self.building_type == "conveyor" and self.type.split("-")[1] == "angular": # angular conveyor
                    self.direction += 1
                    if self.direction > 7:
                        self.direction = 0

                    self.rotate_building(self.direction)

            self.last_direction = self.direction

        if self.selected:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.rect.center = mouse_x, mouse_y

    def take(self):
        self.selected = True
        self.rotate_building(self.last_direction)
        player.selected_structure = self

    def put(self):
        self.selected = False
        player.selected_structure = "empty"
        self.rect.x, self.rect.y = self.x0, self.y0
        self.rotate_building(0)

    def rotate_building(self, direction):
        self.image = cell_images[self.type][direction]
        self.direction = direction


def base_hud_init():
    for i in range(len(open_structures)):
        ui_elements.append(SelectableItemUI(cell_types[open_structures[i]],
                                            (10 + i * (cell_size + cell_size // 10), WINDOW_HEIGHT - WINDOW_HEIGHT // 9)))
