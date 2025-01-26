import pygame.sprite

from map import conveyor_speed, build_map_layer

items = []
#type, image
item_types = {"ore-iron": ["ore-iron", pygame.image.load("images/items/ores/iron-ore.png").convert_alpha()]}

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
        for cell in build_map_layer:
            typec = cell.type.split("-")
            if (typec[0] == "conveyor" or typec[0] == "connector") and cell.rect.collidepoint(self.rect.center):
                return True, cell
        return False, None

    def collide_check(self, group):
        for i in items:
            if self.rect.colliderect(i.rect):
                print("collide")
                return True
        return False

    def despawn(self):
        items.remove(self)

def spawn(type_str, pos):
    items.append(Item(item_types[type_str], pos))