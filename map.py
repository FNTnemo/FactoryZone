from ctypes import c_char
from enum import Enum

import pygame

map1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

map2 = [[-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0,]]

loaded_map = []

cell_images = {"empty": pygame.image.load("images/cells/empty_cell.png").convert_alpha(),
               "selected": pygame.image.load("images/cells/selected_cell.png").convert_alpha(),
               "border-red": pygame.image.load("images/cells/border_cell.png").convert_alpha(),
               "drill": pygame.image.load("images/cells/drill_cell.png").convert_alpha(),
               "smallter-base": pygame.image.load("images/cells/builds/smallter.png").convert_alpha(),
               "conveyor-up": pygame.image.load('images/cells/builds/conveyor.png').convert_alpha(),
               "conveyor-down": pygame.transform.flip(pygame.image.load('images/cells/builds/conveyor.png').convert_alpha(), False, True),
               "conveyor-right": pygame.transform.rotate(pygame.image.load("images/cells/builds/conveyor.png").convert_alpha(), -90),
               "conveyor-left": pygame.transform.rotate(pygame.image.load('images/cells/builds/conveyor.png').convert_alpha(), 90),
               "conveyor-rotate-up-right": pygame.image.load("images/cells/builds/conveyor_rotate_up.png").convert_alpha(),
               "conveyor-rotate-right-up": pygame.transform.flip(pygame.image.load("images/cells/builds/conveyor_rotate_down.png").convert_alpha(), True, True),
               "conveyor-rotate-right-down": pygame.transform.flip(pygame.image.load("images/cells/builds/conveyor_rotate_down.png").convert_alpha(), True, False),
               "conveyor-rotate-down-right": pygame.transform.flip(pygame.image.load("images/cells/builds/conveyor_rotate_up.png").convert_alpha(), False, True),
               "conveyor-rotate-down-left": pygame.transform.flip(pygame.image.load("images/cells/builds/conveyor_rotate_up.png").convert_alpha(), True, True),
               "conveyor-rotate-left-down": pygame.image.load("images/cells/builds/conveyor_rotate_down.png").convert_alpha(),
               "conveyor-rotate-left-up": pygame.transform.flip(pygame.image.load("images/cells/builds/conveyor_rotate_down.png").convert_alpha(), False, True),
               "conveyor-rotate-up-left": pygame.transform.flip(pygame.image.load("images/cells/builds/conveyor_rotate_up.png").convert_alpha(), True, False),
               "connector-input-up": pygame.image.load("images/cells/builds/connector_input.png").convert_alpha(),
               "connector-input-right": pygame.transform.rotate(pygame.image.load("images/cells/builds/connector_input.png").convert_alpha(), -90),
               "connector-input-down": pygame.transform.flip(pygame.image.load("images/cells/builds/connector_input.png").convert_alpha(), False, True),
               "connector-input-left": pygame.transform.rotate(pygame.image.load("images/cells/builds/connector_input.png").convert_alpha(), 90),
               "connector-output-up": pygame.image.load("images/cells/builds/connector_output.png").convert_alpha(),
               "connector-output-right": pygame.transform.rotate(pygame.image.load("images/cells/builds/connector_output.png").convert_alpha(), -90),
               "connector-output-down": pygame.transform.flip(pygame.image.load("images/cells/builds/connector_output.png").convert_alpha(), False, True),
               "connector-output-left": pygame.transform.rotate(pygame.image.load("images/cells/builds/connector_output.png").convert_alpha(), 90),
               "ore-iron": pygame.image.load("images/cells/ores/iron_ore.png").convert_alpha(),}
cell_size = 64
conveyor_speed = 2

map_cells = []
build_cells = []

selected_cells = []


class Cell(pygame.sprite.Sprite, Enum):
    # can_select, can_build_here, player_collide, layer
    #map cells
    empty = cell_images["empty"], "empty", True, True, False, 1
    selected_cell = cell_images["selected"], "selected", False, False, False, 3
    border_red = cell_images["border-red"], "border-red", False, False, True, 1
    #buildings
    drill = cell_images["drill"], "drill", True, False, False, 2
    smallter_base = cell_images["smallter-base"], "smallter_base", True, False, False, 2
    conveyor_up = cell_images["conveyor-up"], "conveyor-up", True, False, False, 2
    conveyor_down = cell_images["conveyor-down"], "conveyor-down", True, False, False, 2
    conveyor_left = cell_images["conveyor-left"], "conveyor-left", True, False, False, 2
    conveyor_right = cell_images["conveyor-right"], "conveyor-right", True, False, False, 2
    #ores
    iron_ore = cell_images["ore-iron"], "ore_iron", True, False, False, 2

    def __init__(self, image, type, *args):
        super().__init__()
        self.image0 = image #начальное изобржение
        self.image = self.image0
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.selected = False
        self.cell_exist = False

        #type
        self.type = type
        self.can_be_selected = args[0]
        self.can_build = args[1]
        self.collide = args[2]
        self.layer = args[3]

        if self.type.split("-")[0] == "conveyor":
            typec = self.type.split("-")
            if typec[1] == "rotate":
                self.conveyor_directional = typec[2]
            else: self.conveyor_directional = typec[1]

        #animation

    def set_position(self, x, y):
        self.rect.x, self.rect.y = x, y

    def update(self):
        from player import camera, player
        mouse_keys = pygame.mouse.get_pressed()
        if not mouse_keys[0]:
            player.build_flag = True
        self.check_select(pygame.Rect(self.rect.x - camera.offset.x, self.rect.y - camera.offset.y, cell_size, cell_size))
        if self.can_build and self.selected:
            #build
            if player.selected_structure_type != "empty":
                if player.build_delay >= 0:
                    player.build_delay -= 1
                if mouse_keys[0] and self.layer == 1 and player.build_delay <= 0 and player.build_flag:
                    for cell in build_cells:
                        if cell.rect.x == self.rect.x and cell.rect.y == self.rect.y and cell.type.split("-")[0] != "conveyor":
                            self.cell_exist = True
                    if not self.cell_exist:
                        self.build(player.selected_structure_type.type)
                        player.build_flag = False
                        player.selected_structure_type.put()
                        player.build_delay = player.build_delay_start
            else:
                player.build_delay = player.build_delay_start

            #destroy
            if player.destroy_delay >= 0:
                player.destroy_delay -= 1
            if mouse_keys[2]:
                for cell in build_cells:
                    if cell.rect.x == self.rect.x and cell.rect.y == self.rect.y:
                        if player.destroy_delay <= 0:
                            cell.destroy()
                            player.destroy_delay = player.destroy_delay_start
                            player.can_move = True
                        else: player.can_move = False
            else:
                player.can_move = True
                player.destroy_delay = player.destroy_delay_start

        #drill update
        if self.type == "drill" and self.layer == 2:
            if get_cell(self.rect.x, self.rect.y, 1).type.split("-")[0] == "ore":
                from items import spawn
                ore_type = get_cell(self.rect.x, self.rect.y, 1).type.split("-")[1]
                cell_yp = get_cell(self.rect.x, self.rect.y - cell_size, 2)
                cell_ym = get_cell(self.rect.x, self.rect.y + cell_size, 2)
                cell_xp = get_cell(self.rect.x + cell_size, self.rect.y, 2)
                cell_xm = get_cell(self.rect.x - cell_size, self.rect.y - cell_size, 2)
                if cell_yp is not None and cell_yp.type.split("-")[0] + "-" + cell_yp.type.split("-")[1] == "connector-output":
                    spawn("ore-" + ore_type, (self.rect.center[0], self.rect.center[1] - cell_size))
                if cell_ym is not None and cell_ym.type.split("-")[0] + "-" + cell_ym.type.split("-")[1] == "connector-output":
                    spawn("ore-" + ore_type, (self.rect.center[0], self.rect.center[1] + cell_size))
                if cell_xp is not None and cell_xp.type.split("-")[0] + "-" + cell_xp.type.split("-")[1] == "connector-output":
                    spawn("ore-" + ore_type, (self.rect.center[0] + cell_size, self.rect.center[1]))
                if cell_xm is not None and cell_xm.type.split("-")[0] + "-" + cell_xm.type.split("-")[1] == "connector-output":
                    spawn("ore-" + ore_type, (self.rect.center[0] - cell_size, self.rect.center[1]))

        if self.selected:
            cell = Cell.selected_cell
            cell.set_position(self.rect.x, self.rect.y)
            selected_cells.append(Cell.selected_cell)

    def check_select(self, rect):
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        if rect.collidepoint(mouse_pos_x, mouse_pos_y) and self.can_be_selected:
            self.selected = True
            return True
        else:
            self.selected = False
            return False

    def build(self, cell):
        cell.set_position(self.rect.x, self.rect.y)
        build_cells.append(cell)
        #map_cells.remove(self)

    def destroy(self):
        build_cells.remove(self)


def get_selected_cell():
    for cell in map_cells:
        if cell.selected:
            return cell
    return None

def get_cell(x, y, layer):
    if layer == 2:
        for cell in build_cells:
            if cell.rect.x == x and cell.rect.y == y:
                return cell
    elif layer == 1:
        for cell in map_cells:
            if cell.rect.x == x and cell.rect.y == y:
                return cell
    return None

def load_map(mapi):
    global loaded_map
    loaded_map = mapi
    write_map_sells()

def get_map_size(mapi):
    return len(mapi[0]) * cell_size, len(mapi) * cell_size

def get_map_char(mapi, x, y):
    return mapi[y][x]

def write_map_sells():
    map_cells.clear()
    for y in range(len(loaded_map)):
        for x in range(len(loaded_map[y])):
            #cell = Cell.empty
            #if get_map_char(loaded_map, x, y) == 1:
            #    cell = Cell.iron_ore
            #elif get_map_char(loaded_map, x, y) == -1:
            #    cell = Cell.border_red
            #cell.set_position(x * cell_size, y * cell_size)
            map_cells.append(Cell.empty)
