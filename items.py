import pygame.sprite

from map import build_map_layer, cell_size, get_cell
from main_settings import conveyor_speed

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

    def update(self):
        self.movement()

    def movement(self):
        self.on_conveyor, self.conveyor = self.on_conveyor_check()
        if self.on_conveyor:
            self.direction = self.conveyor.direction
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
        if cell.typec == "conveyor" or cell.typec == "connector":
            cell.items_in_conveyor.append(self)
            return True, cell
        return False, None

    def despawn(self):
        items.remove(self)


def spawn(type_str, pos):
    item = Item(item_types[type_str], pos)
    items.append(item)
