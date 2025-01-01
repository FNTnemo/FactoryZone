import pygame

from main_settings import WINDOW_WIDTH, WINDOW_HEIGHT
from map import cell_images, cell_types, cell_size
from player import camera, player

ui_images = {"vignette": pygame.image.load("images/hud/vignette.png").convert_alpha()}

ui_elements = []

open_structures = ["drill", "smallter-base", "conveyor-up", "conveyor-rotate-up-right", "connector-input-up", "connector-output-up"]

class UI_element(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image

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
    def __init__(self, type, pos):
        super().__init__()
        self.type0 = type[0]
        self.type = self.type0
        self.last_type = self.type0

        self.building_type = self.type.split("-")[0]
        if self.building_type == "conveyor" or self.building_type == "connector":
            self.directional = 1
        self.image0 = cell_images[self.type]
        self.image = self.image0

        self.rect = self.image.get_rect(topleft=pos)

        self.x0 = self.rect.x
        self.y0 = self.rect.y

        self.selected = False
        self.r_pressed = False

    def update(self):
        m_keys = pygame.mouse.get_pressed()
        k_keys = pygame.key.get_pressed()

        if m_keys[0] and player.selected_structure_type == "empty":
            self.take()
        if k_keys[pygame.K_ESCAPE]:
            self.put()

        if self.selected:
            #rotate
            if not k_keys[pygame.K_r]:
                self.r_pressed = False
            if k_keys[pygame.K_r] and not self.r_pressed:
                self.r_pressed = True
                if self.type.split("-")[0] == "conveyor" and self.type.split("-")[1] != "rotate":
                    self.directional += 1
                    if self.directional > 4:
                        self.directional = 1

                    if self.directional == 1:
                        self.change_type("conveyor-up")
                    elif self.directional == 2:
                        self.change_type("conveyor-right")
                    elif self.directional == 3:
                        self.change_type("conveyor-down")
                    elif self.directional == 4:
                        self.change_type("conveyor-left")

                if self.type.split("-")[0] == "conveyor" and self.type.split("-")[1] == "rotate":
                    self.directional += 1
                    if self.directional > 8:
                        self.directional = 1

                    if self.directional == 1:
                        self.change_type("conveyor-rotate-up-right")
                    elif self.directional == 2:
                        self.change_type("conveyor-rotate-right-up")
                    elif self.directional == 3:
                        self.change_type("conveyor-rotate-right-down")
                    elif self.directional == 4:
                        self.change_type("conveyor-rotate-down-right")
                    elif self.directional == 5:
                        self.change_type("conveyor-rotate-down-left")
                    elif self.directional == 6:
                        self.change_type("conveyor-rotate-left-down")
                    elif self.directional == 7:
                        self.change_type("conveyor-rotate-left-up")
                    elif self.directional == 8:
                        self.change_type("conveyor-rotate-up-left")

                if self.type.split("-")[0] == "connector" and self.type.split("-")[1] == "input":
                    self.directional += 1
                    if self.directional > 4:
                        self.directional = 1

                    if self.directional == 1:
                        self.change_type("connector-input-up")
                    elif self.directional == 2:
                        self.change_type("connector-input-right")
                    elif self.directional == 3:
                        self.change_type("connector-input-down")
                    elif self.directional == 4:
                        self.change_type("connector-input-left")

                if self.type.split("-")[0] == "connector" and self.type.split("-")[1] == "output":
                    self.directional += 1
                    if self.directional > 4:
                        self.directional = 1

                    if self.directional == 1:
                        self.change_type("connector-output-up")
                    elif self.directional == 2:
                        self.change_type("connector-output-right")
                    elif self.directional == 3:
                        self.change_type("connector-output-down")
                    elif self.directional == 4:
                        self.change_type("connector-output-left")

        if self.selected:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.rect.center = mouse_x, mouse_y

    def take(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_x, mouse_y):
            self.selected = True
            self.change_type(self.last_type)
            player.selected_structure_type = self

    def put(self):
        self.selected = False
        player.selected_structure_type = "empty"
        self.rect.x, self.rect.y = self.x0, self.y0
        self.last_type = self.type
        self.change_type(self.type0)

    def change_type(self, type_str):
        self.image = cell_images[type_str]
        self.type = type_str


def base_hud_init():
    for i in range(len(open_structures)):
        ui_elements.append(SelectableItemUI(cell_types[open_structures[i]],
                                            (10 + i * (cell_size + cell_size // 10), WINDOW_HEIGHT - WINDOW_HEIGHT // 9)))
    ui_elements.append(UI_element(ui_images["vignette"], (0 + camera.offset.x, 0 + camera.offset.y))) #vignette
