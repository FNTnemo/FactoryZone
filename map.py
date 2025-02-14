from main_settings import cell_size, cellular_interaction, storage_item_stack, max_item_stack

import pygame
# 0 - nothing 1 - iron 2 - copper 3 - coal
map1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 3, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

map2 = [[-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0,]]

loaded_map = []

cell_images = {"empty": [pygame.image.load("images/cells/empty_cell.png").convert_alpha()],
               "air": [pygame.image.load("images/cells/air_cell.png").convert_alpha()],
               "selected": [pygame.image.load("images/cells/selected_cell.png").convert_alpha()],
               "border-red": [pygame.image.load("images/cells/border_cell.png").convert_alpha()],
               "drill-electric": [pygame.transform.flip(pygame.image.load("images/cells/drill_cell.png").convert_alpha(), False, True),
                                    pygame.transform.rotate(pygame.image.load("images/cells/drill_cell.png").convert_alpha(), 90),
                                    pygame.image.load("images/cells/drill_cell.png").convert_alpha(),
                                    pygame.transform.rotate(pygame.image.load("images/cells/drill_cell.png").convert_alpha(), -90)],
               "smelter-base": [pygame.image.load("images/cells/builds/smallter.png").convert_alpha(),
                                pygame.image.load("images/cells/builds/smallter.png").convert_alpha(),
                                pygame.image.load("images/cells/builds/smallter.png").convert_alpha(),
                                pygame.image.load("images/cells/builds/smallter.png").convert_alpha()],
               "assembler": [pygame.image.load('images/cells/builds/assembler.png').convert_alpha(),
                            pygame.transform.rotate(pygame.image.load("images/cells/builds/assembler.png").convert_alpha(), -90),
                            pygame.transform.rotate(pygame.image.load("images/cells/builds/assembler.png").convert_alpha(), -180),
                            pygame.transform.rotate(pygame.image.load('images/cells/builds/assembler.png').convert_alpha(), -270)],
               "storage": [pygame.image.load("images/cells/builds/storage.png").convert_alpha()],
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
               "iron-ore": [pygame.image.load("images/cells/ores/iron_ore.png").convert_alpha()],
               "copper-ore": [pygame.image.load("images/cells/ores/copper-ore.png").convert_alpha()],
               "coal-ore": [pygame.image.load("images/cells/ores/coal-ore.png").convert_alpha()],
               "green-pointer": [pygame.image.load("images/hud/auxiliary/green-pointer.png").convert_alpha(),
                                 pygame.transform.rotate(pygame.image.load("images/hud/auxiliary/green-pointer.png"), -90),
                                 pygame.transform.flip(pygame.image.load("images/hud/auxiliary/green-pointer.png").convert_alpha(), False, True),
                                 pygame.transform.rotate(pygame.image.load("images/hud/auxiliary/green-pointer.png").convert_alpha(), 90)],
               "orange-pointer": [pygame.image.load("images/hud/auxiliary/orange-pointer.png").convert_alpha(),
                                 pygame.transform.rotate(pygame.image.load("images/hud/auxiliary/orange-pointer.png").convert_alpha(), -90),
                                 pygame.transform.flip(pygame.image.load("images/hud/auxiliary/orange-pointer.png").convert_alpha(), False,True),
                                 pygame.transform.rotate(pygame.image.load("images/hud/auxiliary/orange-pointer.png").convert_alpha(), 90)]}

# type, image [can_select, can_build, player_collide, layer, interactive], [args]
cell_types = {"empty": ["empty", cell_images["empty"], [True, True, False, 1, False], []],
              "air": ["air", cell_images["air"], [True, True, False, 2, False], []],
              "selected": ["selected", cell_images["selected"], [False, False, False, 3, False], []],
              "border-red": ["border-red", cell_images["border-red"], [False, False, True, 1, False], []],
              # buildings
              "drill-electric": ["drill-electric", cell_images["drill-electric"], [True, True, False, 2, True], []],
              "smelter-base": ["smelter-base", cell_images["smelter-base"], [True, False, False, 2, True], []],
              "assembler": ["assembler", cell_images["assembler"], [True, False, False, 2, True], []],
              "storage": ["storage", cell_images["storage"], [True, False, False, 2, True], []],
              # conveyors args[type, direction]
              "conveyor": ["conveyor", cell_images["conveyor"], [True, False, False, 2, False], []],
              "conveyor-angular": ["conveyor-angular", cell_images["conveyor-angular"], [True, False, False, 2, False], []],
              # connectors
              "connector-input": ["connector-input", cell_images["connector-input"], [True, False, False, 2, False], []],
              "connector-output": ["connector-output", cell_images["connector-output"], [True, False, False, 2, False], []],
              # resources (zero ter)
              "ore-iron": ["ore-iron", cell_images["iron-ore"], [True, True, False, 1, False], []],
              "ore-copper": ["ore-copper", cell_images["copper-ore"], [True, True, False, 1, False], []],
              "ore-coal": ["ore-coal", cell_images["coal-ore"], [True, True, False, 1, False], []],
              # first ter
              "pointer-green": ["pointer-green", cell_images["green-pointer"], [False, False, False, 3, False], []],
              "pointer-orange": ["pointer-orange", cell_images["orange-pointer"], [False, False, False, 3, False], []]}



ground_map_layer = []
build_map_layer = []
auxiliary_map_layer = []

selected_cells = []

storage_inventory = [] # main inventory

storage_inventory.append(["chip", 512])
storage_inventory.append(["ore-iron", 2048])

class Cell(pygame.sprite.Sprite):
    def __init__(self, typei, direction, pos):
        super().__init__()
        # argument init
        self.type = typei[0] # type string
        self.typec = self.type.split("-")[0]
        self.direction = direction # direction
        if self.direction >= len(typei[1]):
            self.direction = 0
        self.image0 = typei[1][self.direction] #origin image
        self.cell_arguments = typei[2] # constants arguments
        self.subjective_arguments = typei[3] # subjective arguments

        #rect
        self.image = self.image0 # current image
        self.rect = self.image.get_rect(topleft=pos) # cell rect

        #type
        self.can_be_selected = self.cell_arguments[0]
        self.can_build = self.cell_arguments[1]
        self.collide = self.cell_arguments[2]
        self.layer = self.cell_arguments[3]
        self.can_interactive = self.cell_arguments[4]

        # booleans
        self.selected = False
        self.cell_exist = False

        # subjective parameters
        self.selected_recipe = None
        self.cell_inventory = []
        if self.layer == 2 and self.typec in cellular_interaction["crafting"]:
            from items import all_recipes
            self.recipes = all_recipes[self.typec] # all recipes for this building
            self.crafting_delay_start = 0
            self.crafting_delay = 0
            self.is_process_of_craft = False
        else:
            self.recipes = None
        if self.layer == 2 and self.typec in cellular_interaction["conveyor"]:
            self.items_in_conveyor = []
        if self.layer == 2 and self.typec == "storage":
            pass


        # drill
        if self.typec == "drill":
            self.drill_delay_start = 45
            self.drill_delay = self.drill_delay_start

        # connector
        self.connected_cell = None
        #animation

    def update(self):
        from player import camera, player
        from windows import opened_windows
        mouse_keys = pygame.mouse.get_pressed()
        keyboard_keys = pygame.key.get_pressed()
        # build/destroy
        if len(opened_windows) == 0:
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
                        self.build(player.selected_structure.type, player.selected_structure.direction)
                        if get_cell(self.rect.x, self.rect.y, 2) is not None:
                            self.cell_exist = True
                            cell_under = get_cell(self.rect.x, self.rect.y, 1)
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
                    cell = get_cell(self.rect.x, self.rect.y, 2)
                    if cell.type != "air":
                        if player.destroy_delay <= 0:
                            cell.destroy()
                            player.destroy_delay = player.destroy_delay_start
                            player.can_move = True
                        else: player.can_move = False
                else:
                    player.can_move = True
                    player.destroy_delay = player.destroy_delay_start

        #window
        if mouse_keys[0] and self.selected and self.layer == 2 and self.type != "air" and player.selected_structure == "empty" and self.typec in cellular_interaction["interactive"]:
            from windows import create_window
            create_window(self)
        if keyboard_keys[pygame.K_ESCAPE]:
            from windows import close_window
            close_window()

        # cell update
        # drill update
        if self.type == "drill-electric":
            if get_cell(self.rect.x, self.rect.y, 1).type.split("-")[0] == "ore":
                if self.drill_delay < 0:
                    from items import spawn
                    ore_type = get_cell(self.rect.x, self.rect.y, 1).type
                    if self.direction == 0:
                        test_cell = get_cell(self.rect.x, self.rect.y - cell_size, 2)
                        if test_cell is not None and test_cell.type == "connector-output" and test_cell.direction == self.direction:
                            spawn(ore_type, (self.rect.midtop[0], self.rect.midtop[1] - cell_size/2))
                    elif self.direction == 1:
                        test_cell = get_cell(self.rect.x + cell_size, self.rect.y, 2)
                        if test_cell is not None and test_cell.type == "connector-output" and test_cell.direction == self.direction:
                            spawn(ore_type, (self.rect.midright[0] + cell_size/2, self.rect.midright[1]))
                    elif self.direction == 2:
                        test_cell = get_cell(self.rect.x, self.rect.y + cell_size,2)
                        if test_cell is not None and test_cell.type == "connector-output" and test_cell.direction == self.direction:
                            spawn(ore_type, (self.rect.midbottom[0], self.rect.midbottom[1] + cell_size/2))
                    elif self.direction == 3:
                        test_cell = get_cell(self.rect.x - cell_size, self.rect.y, 2)
                        if test_cell is not None and test_cell.type == "connector-output" and test_cell.direction == self.direction:
                            spawn(ore_type, (self.rect.midleft[0] - cell_size/2, self.rect.midleft[1]))
                    self.drill_delay = self.drill_delay_start
                else:
                    self.drill_delay -= 1

        # craft and output
        if self.typec in cellular_interaction["crafting"]:
            output_cell = None # output cell check
            if self.direction == 0: output_cell = get_cell(self.rect.x, self.rect.y - cell_size, 2)
            elif self.direction == 1: output_cell = get_cell(self.rect.x + cell_size, self.rect.y, 2)
            elif self.direction == 2: output_cell = get_cell(self.rect.x, self.rect.y + cell_size, 2)
            elif self.direction == 3: output_cell = get_cell(self.rect.x - cell_size, self.rect.y, 2)

            if output_cell is not None and output_cell.type == "connector-output" and output_cell.direction == self.direction:
                outcomes = [self.cell_inventory[id][1] >= self.selected_recipe[2][id][1] for id in range(len(self.cell_inventory))]
                if self.selected_recipe is not None and sum(outcomes) == len(self.selected_recipe[2]):
                    if self.crafting_delay <= 0:
                        self.craft(self.selected_recipe[0])
                        self.crafting_delay = self.crafting_delay_start
                    else:
                        self.crafting_delay -= 1
                        self.is_process_of_craft = True
                else: self.is_process_of_craft = False
            else: self.is_process_of_craft = False

        #connector update
        if self.type == "connector-input":
            test_cell = None
            if self.direction == 0: test_cell = get_cell(self.rect.x, self.rect.y - cell_size, 2)
            elif self.direction == 1: test_cell = get_cell(self.rect.x + cell_size, self.rect.y, 2)
            elif self.direction == 2: test_cell = get_cell(self.rect.x, self.rect.y + cell_size, 2)
            elif self.direction == 3: test_cell = get_cell(self.rect.x - cell_size, self.rect.y, 2)

            if test_cell is not None and test_cell.typec == "storage":
                from items import items
                for item in items:
                    if item.rect.colliderect(test_cell.rect):
                        add_item_into_storage(item)
                        item.despawn()

            if test_cell is not None and test_cell.can_interactive and test_cell.selected_recipe is not None:
                from items import items
                for item in items:
                    if item.rect.colliderect(test_cell.rect):
                        for id in range(len(test_cell.selected_recipe[2])):
                            if test_cell.selected_recipe[2][id][0] == item.type:
                                add_item(test_cell, item)
                                item.despawn()


        # selection update
        if self.selected:
            selected_cells.append(Cell(cell_types["selected"], 0,  (self.rect.x, self.rect.y)))

    def craft(self, item_str):
        from items import spawn
        for id in range(len(self.cell_inventory)):
            self.cell_inventory[id][1] -= self.selected_recipe[2][id][1]
        item_pos = ()
        if self.direction == 0: item_pos = self.rect.midtop
        if self.direction == 1: item_pos = (self.rect.midright[0] + 32, self.rect.midright[1])
        if self.direction == 2: item_pos = (self.rect.midbottom[0], self.rect.midbottom[1] + 32)
        if self.direction == 3: item_pos = self.rect.midleft
        spawn(item_str, item_pos)

    def check_select(self, rect):
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        if rect.collidepoint(mouse_pos_x, mouse_pos_y) and self.can_be_selected:
            self.selected = True
            return True
        else:
            self.selected = False
            return False

    def build(self, typei, direction): # build cell
        build_map_layer[calc_map_line(self.rect.x, self.rect.y)] = Cell(cell_types[typei], direction, (self.rect.x, self.rect.y))

    def destroy(self): # destroy this cell
        build_map_layer[calc_map_line(self.rect.x, self.rect.y)] = Cell(cell_types["air"], 0, (self.rect.x, self.rect.y))

def add_item(building, item): #add item in this cell
    for inv in building.cell_inventory:
        if inv[0] == item.type and inv[1] < max_item_stack:
            inv[1] += 1

def add_item_into_storage(item):
    for inv in storage_inventory:
        if inv[0] == item.type:
            if inv[1] < storage_item_stack: inv[1] += 1
            return
    storage_inventory.append([item.type, 1])

def get_selected_cell():
    for cell in build_map_layer:
        if cell.selected: return cell
    return None

def get_cell(x, y, layer):
    if layer == 1: return ground_map_layer[calc_map_line(x, y)]
    if layer == 2: return build_map_layer[calc_map_line(x, y)]
    if layer == 3: return auxiliary_map_layer[calc_map_line(x, y)]

def get_cell_id(x, y):
    return calc_map_line(x, y)

def load_map(mapi):
    global loaded_map
    loaded_map = mapi
    write_map_sells()

def calc_map_line(x, y):
    mc = get_map_size(loaded_map)
    x //= cell_size
    y //= cell_size
    id = x + y * mc[0] // cell_size
    if x < mc[0] // cell_size and y < mc[1] // cell_size: return id
    else: return 0

def get_map_size(mapi):
    return len(mapi[0]) * cell_size, len(mapi) * cell_size

def get_loaded_map():
    return loaded_map

def get_map_char(mapi, x, y):
    return mapi[y][x]

def write_map_sells():
    ground_map_layer.clear()
    for y in range(len(loaded_map)):
        for x in range(len(loaded_map[y])):
            if get_map_char(loaded_map, x, y) == 0:
                ground_map_layer.append(Cell(cell_types["empty"], 0, (x * cell_size, y * cell_size)))
            elif get_map_char(loaded_map, x, y) == 1:
                ground_map_layer.append(Cell(cell_types["ore-iron"], 0, (x * cell_size, y * cell_size)))
            elif get_map_char(loaded_map, x, y) == 2:
                ground_map_layer.append(Cell(cell_types["ore-copper"], 0, (x * cell_size, y * cell_size)))
            elif get_map_char(loaded_map, x, y) == 3:
                ground_map_layer.append(Cell(cell_types["ore-coal"], 0, (x * cell_size, y * cell_size)))
            elif get_map_char(loaded_map, x, y) == -1:
                ground_map_layer.append(Cell(cell_types["border-red"], 0, (x * cell_size, y * cell_size)))
            build_map_layer.append(Cell(cell_types["air"], 0, (x * cell_size, y * cell_size)))
            auxiliary_map_layer.append(Cell(cell_types["air"], 0, (x * cell_size, y * cell_size)))