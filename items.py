import pygame.sprite

from map import build_map_layer, cell_size, get_cell
from main_settings import conveyor_speed

items = []
#type, image
item_types = {"ore-iron": ["ore-iron", pygame.image.load("images/items/ores/iron-ore.png").convert_alpha()],
              "plate-iron": ["plate-iron", pygame.image.load("images/items/iron-plate.png").convert_alpha()]}

# (item, count), time
recipes = {"smelter":
                [("plate-iron", 20, (("ore-iron", 1))),
                ("plate-iron", 25, ("ore-iron", 1))]
           }

class Item(pygame.sprite.Sprite):
    def __init__(self, type, pos):
        super().__init__()
        self.type = type[0]
        self.image = type[1]
        self.rect = self.image.get_rect(center=pos)

        self.velocity = pygame.math.Vector2()

    def update(self):
        #if not self.collide_check(items):
        self.movement()

    def movement(self):
        on_conveyor, conveyor = self.on_conveyor()
        if on_conveyor:
            direction = conveyor.direction
            if conveyor.type == "conveyor" or conveyor.type.split("-")[0] == "connector":
                if direction == 0: #conveyor
                    self.rect.y += -conveyor_speed
                if direction == 1:
                    self.rect.x += conveyor_speed
                if direction == 2:
                    self.rect.y += conveyor_speed
                if direction == 3:
                    self.rect.x += -conveyor_speed

    def on_conveyor(self):
        x = (self.rect.x // cell_size) * cell_size
        y = (self.rect.y // cell_size) * cell_size
        cell = get_cell(x, y, 2)
        typec = cell.type.split("-")
        if typec[0] == "conveyor" or typec[0] == "connector":
            return True, cell
        return False, None

    def on_connector(self):
        x = (self.rect.x // cell_size) * cell_size
        y = (self.rect.y // cell_size) * cell_size
        cell = get_cell(x, y, 2)
        typec = cell.type.split("-")
        if typec[0] == "connector":
            return True, cell
        return False, None

    def collide_check(self, group):
        for i in items:
            if self.rect.colliderect(i.rect):
                return True
        return False

    def despawn(self):
        items.remove(self)

def spawn(type_str, pos):
    items.append(Item(item_types[type_str], pos))