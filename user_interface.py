import pygame

from main_settings import WINDOW_WIDTH, WINDOW_HEIGHT, cellular_interaction
from map import cell_images, cell_types, cell_size, auxiliary_map_layer, get_cell_id, Cell, get_selected_cell, \
    get_map_size, get_loaded_map
from player import player

ui_images = {"vignette": pygame.image.load("images/hud/vignette.png").convert_alpha()}

ui_elements = []

open_structures = ["drill-electric", "smelter-base", "assembler", "storage", "conveyor", "connector-input", "connector-output"]

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

                if self.type == "conveyor" or self.building_type == "connector" or self.building_type == "drill" or self.building_type == "smelter" or self.building_type == "assembler": # 4 states
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

            # mouse follow
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.rect.center = mouse_x, mouse_y

            # pointers
            under_cell = get_selected_cell()
            if under_cell is not None and self.building_type in cellular_interaction["interactive"]:
                ms = get_map_size(get_loaded_map())
                if self.building_type == "smelter" or self.building_type == "assembler":
                    green_pos, orange_pos, orange_pos2, orange_pos3 = (), (), (), ()
                    if self.direction == 0:
                        green_pos = (under_cell.rect.x, under_cell.rect.y - cell_size)
                        orange_pos = (under_cell.rect.x, under_cell.rect.y + cell_size)
                        orange_pos2 = (under_cell.rect.x + cell_size, under_cell.rect.y)
                        orange_pos3 = (under_cell.rect.x - cell_size, under_cell.rect.y)
                    elif self.direction == 1:
                        green_pos = (under_cell.rect.x + cell_size, under_cell.rect.y)
                        orange_pos = (under_cell.rect.x - cell_size, under_cell.rect.y)
                        orange_pos2 = (under_cell.rect.x, under_cell.rect.y + cell_size)
                        orange_pos3 = (under_cell.rect.x, under_cell.rect.y - cell_size)
                    elif self.direction == 2:
                        green_pos = (under_cell.rect.x, under_cell.rect.y +cell_size)
                        orange_pos = (under_cell.rect.x, under_cell.rect.y - cell_size)
                        orange_pos2 = (under_cell.rect.x - cell_size, under_cell.rect.y)
                        orange_pos3 = (under_cell.rect.x + cell_size, under_cell.rect.y)
                    elif self.direction == 3:
                        green_pos = (under_cell.rect.x - cell_size, under_cell.rect.y)
                        orange_pos = (under_cell.rect.x + cell_size, under_cell.rect.y)
                        orange_pos2 = (under_cell.rect.x, under_cell.rect.y - cell_size)
                        orange_pos3 = (under_cell.rect.x, under_cell.rect.y + cell_size)
                    if ms[0] > green_pos[0] >= 0 and ms[1] > green_pos[1] >= 0:
                        auxiliary_map_layer[get_cell_id(green_pos[0], green_pos[1])] = Cell(cell_types["pointer-green"], self.direction, green_pos)
                    if ms[0] > orange_pos[0] >= 0 and ms[1] > orange_pos[1] >= 0:
                        auxiliary_map_layer[get_cell_id(orange_pos[0], orange_pos[1])] = Cell(cell_types["pointer-orange"], self.direction,orange_pos)
                    if ms[0] > orange_pos2[0] >= 0 and ms[1] > orange_pos2[1] >= 0:
                        auxiliary_map_layer[get_cell_id(orange_pos2[0], orange_pos2[1])] = Cell(cell_types["pointer-orange"], self.direction - 1, orange_pos2)
                    if ms[0] > orange_pos3[0] >= 0 and ms[1] > orange_pos3[1] >= 0:
                        auxiliary_map_layer[get_cell_id(orange_pos3[0], orange_pos3[1])] = Cell(cell_types["pointer-orange"], self.direction + 1, orange_pos3)

                if self.building_type == "drill":
                    green_pos = ()
                    if self.direction == 0:
                        green_pos = (under_cell.rect.x, under_cell.rect.y - cell_size)
                    elif self.direction == 1:
                        green_pos = (under_cell.rect.x + cell_size, under_cell.rect.y)
                    elif self.direction == 2:
                        green_pos = (under_cell.rect.x, under_cell.rect.y + cell_size)
                    elif self.direction == 3:
                        green_pos = (under_cell.rect.x - cell_size, under_cell.rect.y)
                    if ms[0] > green_pos[0] >= 0 and ms[1] > green_pos[1] >= 0:
                        auxiliary_map_layer[get_cell_id(green_pos[0], green_pos[1])] = Cell(cell_types["pointer-green"], self.direction, green_pos)

                if self.building_type == "storage":
                    orange_pos1 = (under_cell.rect.x, under_cell.rect.y - cell_size)
                    orange_pos2 = (under_cell.rect.x, under_cell.rect.y + cell_size)
                    orange_pos3 = (under_cell.rect.x + cell_size, under_cell.rect.y)
                    orange_pos4 = (under_cell.rect.x - cell_size, under_cell.rect.y)
                    if ms[0] > orange_pos1[0] >= 0 and ms[1] > orange_pos1[1] >= 0:
                        auxiliary_map_layer[get_cell_id(orange_pos1[0], orange_pos1[1])] = Cell(cell_types["pointer-orange"], 2, orange_pos1)
                    if ms[0] > orange_pos2[0] >= 0 and ms[1] > orange_pos2[1] >= 0:
                        auxiliary_map_layer[get_cell_id(orange_pos2[0], orange_pos2[1])] = Cell(cell_types["pointer-orange"], 0, orange_pos2)
                    if ms[0] > orange_pos3[0] >= 0 and ms[1] > orange_pos3[1] >= 0:
                        auxiliary_map_layer[get_cell_id(orange_pos3[0], orange_pos3[1])] = Cell(cell_types["pointer-orange"], 3, orange_pos3)
                    if ms[0] > orange_pos4[0] >= 0 and ms[1] > orange_pos4[1] >= 0:
                        auxiliary_map_layer[get_cell_id(orange_pos4[0], orange_pos4[1])] = Cell(cell_types["pointer-orange"], 1, orange_pos4)
                print(self.building_type)

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

def clear_pointers():
    for cell in auxiliary_map_layer:
        if cell.typec == "pointer":
            auxiliary_map_layer[get_cell_id(cell.rect.x, cell.rect.y)] = Cell(cell_types["air"], 0, (cell.rect.x, cell.rect.y))

def base_hud_init():
    for i in range(len(open_structures)):
        ui_elements.append(SelectableItemUI(cell_types[open_structures[i]],
                                            (10 + i * (cell_size + cell_size // 10), WINDOW_HEIGHT - WINDOW_HEIGHT // 9)))
