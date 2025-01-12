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

cell_images = {"empty": [pygame.image.load("images/cells/empty_cell.png").convert_alpha()],
               "selected": [pygame.image.load("images/cells/selected_cell.png").convert_alpha()],
               "border-red": [pygame.image.load("images/cells/border_cell.png").convert_alpha()],
               "drill-electric": [pygame.transform.flip(pygame.image.load("images/cells/drill_cell.png").convert_alpha(), False, True),
                                    pygame.transform.rotate(pygame.image.load("images/cells/drill_cell.png").convert_alpha(), 90),
                                    pygame.image.load("images/cells/drill_cell.png").convert_alpha(),
                                    pygame.transform.rotate(pygame.image.load("images/cells/drill_cell.png").convert_alpha(), -90)],
               "smallter-base": [pygame.image.load("images/cells/builds/smallter.png").convert_alpha()],
               "conveyor": [pygame.image.load('images/cells/builds/conveyor.png').convert_alpha(),
                                    pygame.transform.rotate(pygame.image.load("images/cells/builds/conveyor.png").convert_alpha(), -90),
                                    pygame.transform.flip(pygame.image.load('images/cells/builds/conveyor.png').convert_alpha(),False, True),
                                    pygame.transform.rotate(pygame.image.load('images/cells/builds/conveyor.png').convert_alpha(), 90)],
               "conveyor-angular": [pygame.image.load("images/cells/builds/conveyor_rotate_up.png").convert_alpha(),
                                    pygame.transform.flip(pygame.image.load("images/cells/builds/conveyor_rotate_down.png").convert_alpha(), True, True),
                                    pygame.transform.flip(pygame.image.load("images/cells/builds/conveyor_rotate_down.png").convert_alpha(), True, False),
                                    pygame.transform.flip(pygame.image.load("images/cells/builds/conveyor_rotate_up.png").convert_alpha(), False, True),
                                    pygame.transform.flip(pygame.image.load("images/cells/builds/conveyor_rotate_up.png").convert_alpha(), True, True),
                                    pygame.image.load("images/cells/builds/conveyor_rotate_down.png").convert_alpha(),
                                    pygame.transform.flip(pygame.image.load("images/cells/builds/conveyor_rotate_down.png").convert_alpha(), False, True),
                                    pygame.transform.flip(pygame.image.load("images/cells/builds/conveyor_rotate_up.png").convert_alpha(), True, False)],
               "connector-input": [pygame.image.load("images/cells/builds/connector_input.png").convert_alpha(),
                                    pygame.transform.rotate(pygame.image.load("images/cells/builds/connector_input.png").convert_alpha(), -90),
                                    pygame.transform.flip(pygame.image.load("images/cells/builds/connector_input.png").convert_alpha(), False, True),
                                    pygame.transform.rotate(pygame.image.load("images/cells/builds/connector_input.png").convert_alpha(), 90)],
               "connector-output": [pygame.transform.flip(pygame.image.load("images/cells/builds/connector_output.png").convert_alpha(), False, True),
                                    pygame.transform.rotate(pygame.image.load("images/cells/builds/connector_output.png").convert_alpha(),90),
                                    pygame.image.load("images/cells/builds/connector_output.png").convert_alpha(),
                                    pygame.transform.rotate(pygame.image.load("images/cells/builds/connector_output.png").convert_alpha(), -90)],




               "iron-ore": [pygame.image.load("images/cells/ores/iron_ore.png").convert_alpha()]}
# type, image [can_select, can_build, player_collide, layer], [args]
cell_types = {"empty": ["empty", cell_images["empty"], [True, True, False, 1], []],
              "selected": ["selected", cell_images["selected"], [False, False, False, 3], []],
              "border-red": ["border-red", cell_images["border-red"], [False, False, True, 1], []],
              # buildings
              "drill-electric": ["drill-electric", cell_images["drill-electric"], [True, True, False, 2], [1]],
              "smallter-base": ["smallter-base", cell_images["smallter-base"], [True, False, False, 2], []],
              # conveyors args[type, direction]
              "conveyor": ["conveyor", cell_images["conveyor"], [False, False, False, 2], []],
              "conveyor-angular": ["conveyor-angular", cell_images["conveyor-angular"], [False, False, False, 2], []],
              # connectors
              "connector-input": ["connector-input", cell_images["connector-input"], [True, False, False, 2], []],
              "connector-output": ["connector-output", cell_images["connector-output"], [True, False, False, 2], []],
              # ores
              "ore-iron": ["ore-iron", cell_images["iron-ore"], [True, True, False, 1], []]}

cell_size = 64
conveyor_speed = 5

map_cells = []
build_cells = []
conveyor_cells = []

selected_cells = []


class Cell(pygame.sprite.Sprite):
    def __init__(self, typei, directional, pos):
        super().__init__()
        # argument init
        self.type = typei[0]
        self.direction = directional
        self.image0 = typei[1][self.direction] #начальное изобржение
        self.cell_arguments = typei[2]
        self.subjective_arguments = typei[3]

        #rect
        self.image = self.image0
        self.rect = self.image.get_rect(topleft=pos)

        #type
        self.can_be_selected = self.cell_arguments[0]
        self.can_build = self.cell_arguments[1]
        self.collide = self.cell_arguments[2]
        self.layer = self.cell_arguments[3]

        # booleans
        self.selected = False
        self.cell_exist = False

        # subjective parameters
        stype = self.type.split("-")

        # drill
        if stype[0] == "drill":
            self.drill_delay_start = 2
            self.drill_delay = self.drill_delay_start

        #animation

    def update(self):
        #self.update_environment()
        from player import camera, player
        mouse_keys = pygame.mouse.get_pressed()
        if not mouse_keys[0]:
            player.build_flag = True
        self.check_select(pygame.Rect(self.rect.x - camera.offset.x, self.rect.y - camera.offset.y, cell_size, cell_size))
        if self.can_build and self.selected:
            #build
            if player.selected_structure != "empty":
                if player.build_delay >= 0:
                    player.build_delay -= 1

                cell_under = None
                if mouse_keys[0] and self.layer == 1 and player.build_delay <= 0 and player.build_flag:
                    if get_cell(self.rect.x, self.rect.y, 2) is not None:
                        self.cell_exist = True
                        cell_under = get_cell(self.rect.x, self.rect.y, 2)
                    else: self.cell_exist = False

                    if not self.cell_exist:
                        self.build(player.selected_structure.type, player.selected_structure.direction)
                        player.build_delay = player.build_delay_start

                    elif self.cell_exist and (player.selected_structure.type.split("-")[0] == "conveyor" or player.selected_structure.type.split("-")[0] == "connector") and (cell_under.type.split("-")[0] == "conveyor" or cell_under.type.split("-")[0] == "connector"):
                        cell_under.destroy()
                        self.build(player.selected_structure.type, player.selected_structure.direction)
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
        if self.type == "drill-electric" and self.layer == 2:
            if get_cell(self.rect.x, self.rect.y, 1).type.split("-")[0] == "ore":
                if self.drill_delay < 0:
                    from items import spawn
                    ore_type = get_cell(self.rect.x, self.rect.y, 1).type
                    if self.direction == 0:
                        test_cell = get_cell(self.rect.x, self.rect.y - cell_size, 2)
                        if test_cell is not None and test_cell.type == "connector-output" and test_cell.direction == self.direction:
                            spawn(ore_type, self.rect.midtop)
                    if self.direction == 1:
                        test_cell = get_cell(self.rect.x + cell_size, self.rect.y, 2)
                        if test_cell is not None and test_cell.type == "connector-output" and test_cell.direction == self.direction:
                            spawn(ore_type, self.rect.midright)
                    if self.direction == 2:
                        test_cell = get_cell(self.rect.x, self.rect.y + cell_size, 2)
                        if test_cell is not None and test_cell.type == "connector-output" and test_cell.direction == self.direction:
                            spawn(ore_type, self.rect.midbottom)
                    if self.direction == 3:
                        test_cell = get_cell(self.rect.x - cell_size, self.rect.y, 2)
                        if test_cell is not None and test_cell.type == "connector-output" and test_cell.direction == self.direction:
                            spawn(ore_type, self.rect.midleft)
                    self.drill_delay = self.drill_delay_start
                else:
                    self.drill_delay -= 1

        #connector update
        if self.type == "connector-input" and self.layer == 2:
            from items import items
            if self.direction == 2:
                test_cell = get_cell(self.rect.x, self.rect.y + cell_size, 2)
                if test_cell is not None:
                    if test_cell.type == "smallter-base":
                        for item in items:
                            if item.rect.colliderect(test_cell.rect):
                                item.despawn()

        if self.selected:
            selected_cells.append(Cell(cell_types["selected"], 0,  (self.rect.x, self.rect.y)))

    def check_select(self, rect):
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        if rect.collidepoint(mouse_pos_x, mouse_pos_y) and self.can_be_selected:
            self.selected = True
            return True
        else:
            self.selected = False
            return False

    def build(self, typei, directional):
        build_cells.append(Cell(cell_types[typei], directional, (self.rect.x, self.rect.y)))
        if typei.split("-")[0] == "conveyor":
            conveyor_cells.append(Cell(cell_types[typei], directional, (self.rect.x, self.rect.y)))
        #map_cells.remove(self)

    def destroy(self):
        #map_cells.append(Cell(cell_types["empty"], cell_images["empty"], self.rect.x, self.rect.y))
        build_cells.remove(self)
        #if self.type.split("-")[0] == "conveyor":
        #    conveyor_cells.remove(self)

def get_selected_cell():
    if len(selected_cells) != 0:
        return selected_cells[0]
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
                map_cells.append(Cell(cell_types["empty"], 0, (x * cell_size, y * cell_size)))
            elif get_map_char(loaded_map, x, y) == 1:
                map_cells.append(Cell(cell_types["ore-iron"], 0,  (x * cell_size, y * cell_size)))
            elif get_map_char(loaded_map, x, y) == -1:
                map_cells.append(Cell(cell_types["border-red"], 0,  (x * cell_size, y * cell_size)))