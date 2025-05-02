from random import random

import pygame.sprite

from map import cell_size, get_cell
from main_settings import conveyor_speed, cellular_interaction

items = []
#type, image
item_types = {"ore-iron": ["ore-iron", pygame.image.load("images/items/ores/iron-ore.png").convert_alpha()],
              "ore-copper": ["ore-copper", pygame.image.load("images/items/ores/copper-ore.png").convert_alpha()],
              "ore-coal": ["ore-coal", pygame.image.load("images/items/ores/coal-ore.png").convert_alpha()],
              "plate-iron": ["plate-iron", pygame.image.load("images/items/plates/iron-plate.png").convert_alpha()],
              "plate-copper": ["plate-copper", pygame.image.load("images/items/plates/copper-plate.png").convert_alpha()],
              "steel": ["steel", pygame.image.load("images/items/plates/steel-plate.png").convert_alpha()],
              "road-copper": ["road-copper", pygame.image.load("images/items/roads/copper-road.png").convert_alpha()],
              "road-iron": ["road-iron", pygame.image.load("images/items/roads/iron-road.png").convert_alpha()],
              "chip": ["chip", pygame.image.load("images/items/chip.png").convert_alpha()]}

# (item, count)
# recipes["building"][recipe id][0] <- 0 - type str; 1 - crafting time; 2 - ingredients
all_recipes = {
    "smelter": (["plate-iron", 64, [("ore-iron", 1)]],
                ["plate-copper", 64, [("ore-copper", 1)]],
                ["steel", 81, [("ore-iron", 3), ("ore-coal", 2)]]),
    "assembler": (["road-copper", 64, [("plate-copper", 1)]],
                  ["road-iron", 42, [("plate-iron", 1)]],
                  ["chip", 256, [("plate-iron", 1), ("plate-copper", 1), ("road-copper", 3)]])
           }

def get_recipe(building, recipei):
    for recipe in all_recipes[building]:
        if recipe[0] == recipei: return recipe

class Item(pygame.sprite.Sprite):
    def __init__(self, type, pos):
        super().__init__()
        self.type = type[0]
        self.image = type[1]
        self.rect = self.image.get_rect(center=pos)

        # movement
        self.direction = None
        self.conveyor = self.on_conveyor_check()[1]
        self.conveyor_queue = []
        self.on_conveyor = self.on_conveyor_check()[0]
        self.is_move = False

        self.owner_cell = get_cell(self.rect.x, self.rect.y, 1)

    def update(self):
        self.movement()
        cell = get_cell(self.rect.center[0], self.rect.center[1], 1)

        if self.owner_cell != cell:
            if self in self.owner_cell.items:
                self.owner_cell.items.remove(self)
            self.owner_cell = cell

        if self not in cell.items:
            cell.items.append(self)



    def movement(self):
        self.on_conveyor, self.conveyor = self.on_conveyor_check()
        if self.on_conveyor:
            self.direction = self.conveyor.conveyor_direction
            if self.conveyor not in self.conveyor_queue and self.conveyor is not None:
                self.conveyor_queue = self.conveyor_queue + [self.conveyor]

            if len(self.conveyor_queue) != 0:
                if self.conveyor_queue[0].direction == 0:
                    self.rect.y -= conveyor_speed
                    if self.rect.midbottom[1] == self.conveyor_queue[0].rect.midtop[1]:
                        self.conveyor_queue.remove(self.conveyor_queue[0])

                elif self.conveyor_queue[0].direction == 1:
                    self.rect.x += conveyor_speed
                    if self.rect.midleft[0] == self.conveyor_queue[0].rect.midright[0]:
                        self.conveyor_queue.remove(self.conveyor_queue[0])

                elif self.conveyor_queue[0].direction == 2:
                    self.rect.y += conveyor_speed
                    if self.rect.midtop[1] == self.conveyor_queue[0].rect.midbottom[1]:
                        self.conveyor_queue.remove(self.conveyor_queue[0])

                elif self.conveyor_queue[0].direction == 3:
                    self.rect.x -= conveyor_speed
                    if self.rect.midright[0] == self.conveyor_queue[0].rect.midleft[0]:
                        self.conveyor_queue.remove(self.conveyor_queue[0])
        else: self.despawn()

    def on_conveyor_check(self):
        x = (self.rect.x // cell_size) * cell_size
        y = (self.rect.y // cell_size) * cell_size
        cell = get_cell(x, y, 2)
        if cell.typec in cellular_interaction["conveyor"]:
            cell.items_in_conveyor.append(self)
            return True, cell
        return False, None

    def despawn(self):
        if self in items:
            items.remove(self)
        if self in get_cell(self.rect.center[0], self.rect.center[1], 1).items:
            get_cell(self.rect.center[0], self.rect.center[1], 1).items.remove(self)

def spawn(type_str, pos):
    item = Item(item_types[type_str], pos)
    items.append(item)
