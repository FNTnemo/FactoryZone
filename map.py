from ctypes import c_char

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
               "conveyor-up": pygame.image.load('images/cells/builds/conveyor_up.png').convert_alpha(),
               "conveyor-down": pygame.transform.flip(pygame.image.load('images/cells/builds/conveyor_up.png').convert_alpha(), False, True),
               "conveyor-right": pygame.transform.rotate(pygame.image.load("images/cells/builds/conveyor_up.png").convert_alpha(), -90),
               "conveyor-left": pygame.transform.rotate(pygame.image.load('images/cells/builds/conveyor_up.png').convert_alpha(), 90),
               "conveyor-rotate-right": pygame.image.load("images/cells/builds/conveyor_right.png").convert_alpha(),
               "ore-iron": pygame.image.load("images/cells/ores/iron_ore.png").convert_alpha()}
#can_select, can_build, player_collide, layer
conveyor_speed = 4
cell_types = {"empty": ["empty", True, True, False, 1],
              "border-red": ["border-red", False, False, True, 1],
              "drill": ["drill", True, True, False, 2],
              "selected": ["selected", False, False, False, 3],
              "smallter-base": ["smallter-base", True, False, False, 2],
              "conveyor-up": ["conveyor-up", False, False, False, 2],
              "conveyor-down": ["conveyor-down", False, False, False, 2],
              "conveyor-right": ["conveyor-right", False, False, False, 2],
              "conveyor-rotate-right": ["conveyor-rotate-right", False, False, False, 2],
              "conveyor-rotate-left": ["conveyor-rotate-left", False, False, False, 2],
              "conveyor-rotate-right-down": ["conveyor-rotate-right-down", False, False, False, 2],
              "conveyor-rotate-left-down": ["conveyor-rotate-left-down", False, False, False, 2],
              "ore-iron": ["ore-iron", True, True, False, 1]}

cell_size = 64

map_cells = []
build_cells = []

selected_cells = []


class Cell(pygame.sprite.Sprite):
    def __init__(self, type, image, x, y):
        super().__init__()
        self.image0 = image #начальное изобржение
        self.image = self.image0
        self.rect = self.image.get_rect(topleft=(x, y))
        self.selected = False
        self.cell_exist = False

        #type
        self.type = type[0]
        self.can_be_selected = type[1]
        self.can_build = type[2]
        self.collide = type[3]
        self.layer = type[4]

        if self.type.split("-")[0] == "conveyor":
            typec = self.type.split("-")
            if typec[1] == "rotate":
                self.conveyor_directional = typec[2]
            else: self.conveyor_directional = typec[1]

        #animation

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

        #conveyor update
        #if self.type.split("-")[0] == "conveyor" and self.type.split("-")[1] != "rotate":
        #    right_conv = get_cell(self.rect.x + cell_size, self.rect.y, 2)
        #    left_conv = get_cell(self.rect.x + cell_size, self.rect.y, 2)
        #    up_conv = get_cell(self.rect.x + cell_size, self.rect.y, 2)
        #    down_conv = get_cell(self.rect.x + cell_size, self.rect.y, 2)
        #    if

        #drill update
        if self.type == "drill":
            if get_cell(self.rect.x, self.rect.y, 1).type.split("-")[0] == "ore":
                pass

        if self.selected:
            selected_cells.append(Cell(cell_types["selected"], cell_images["selected"], self.rect.x, self.rect.y))

    def check_select(self, rect):
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        if rect.collidepoint(mouse_pos_x, mouse_pos_y) and self.can_be_selected:
            self.selected = True
            return True
        else:
            self.selected = False
            return False

    def build(self, typei):
        build_cells.append(Cell(cell_types[typei], cell_images[typei], self.rect.x, self.rect.y))
        #map_cells.remove(self)

    def destroy(self):
        #map_cells.append(Cell(cell_types["empty"], cell_images["empty"], self.rect.x, self.rect.y))
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
        return None
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
            if get_map_char(loaded_map, x, y) == 0:
                map_cells.append(Cell(cell_types["empty"], cell_images["empty"], x * cell_size, y * cell_size))
            elif get_map_char(loaded_map, x, y) == 1:
                map_cells.append(Cell(cell_types["ore-iron"], cell_images["ore-iron"], x * cell_size, y * cell_size))
            elif get_map_char(loaded_map, x, y) == -1:
                map_cells.append(Cell(cell_types["border-red"], cell_images["border-red"], x * cell_size, y * cell_size))