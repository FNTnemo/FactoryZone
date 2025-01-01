import pygame.sprite

from map import build_cells, conveyor_speed

items = []
#type, image
item_types = {"ore-iron": ["ore-iron", pygame.image.load("images/items/ores/iron-ore.png").convert_alpha()]}

class Item(pygame.sprite.Sprite):
    def __init__(self, type, pos):
        super().__init__()
        self.type = type[0]
        self.image = type[1]
        self.rect = self.image.get_rect(center=(pos[0], pos[1]))

        self.velocity = pygame.math.Vector2()

    def update(self):
        self.movement()

    def movement(self):
        self.velocity.x = 0
        self.velocity.y = 0
        if self.on_conveyor()[0]:
            conveyor_type = self.on_conveyor()[1].split("-")
            directional = ""
            if conveyor_type[0] == "conveyor" and conveyor_type[1] != "rotate":
                directional = conveyor_type[1]
            elif conveyor_type[0] == "conveyor" and conveyor_type[1] == "rotate":
                directional = conveyor_type[2] + "-" + conveyor_type[3]
            elif conveyor_type[0] == "connector":
                directional = conveyor_type[1] + "-" + conveyor_type[2]

            if directional == "up": #conveyor
                self.velocity.y = -conveyor_speed
            if directional == "down":
                self.velocity.y = conveyor_speed
            if directional == "right":
                self.velocity.x = conveyor_speed
            if directional == "left":
                self.velocity.x = -conveyor_speed
            elif directional == "output-up": #connectors
                self.velocity.y = conveyor_speed
            elif directional == "output-down":
                self.velocity.y = -conveyor_speed
            elif directional == "output-right":
                self.velocity.x = -conveyor_speed
            elif directional == "output-left":
                self.velocity.x = conveyor_speed
            elif directional == "input-up":
                self.velocity.y = -conveyor_speed
            elif directional == "input-down":
                self.velocity.y = conveyor_speed
            elif directional == "input-right":
                self.velocity.y = -conveyor_speed
            elif directional == "input-left":
                self.velocity.y = conveyor_speed

            #rotate
            if directional == "up-left":
                self.velocity.x = -conveyor_speed
            if directional == "up-left":
                self.velocity.x = -conveyor_speed
            if directional == "up-left":
                self.velocity.x = -conveyor_speed
            if directional == "up-left":
                self.velocity.x = -conveyor_speed

        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

    def on_conveyor(self):
        for cell in build_cells:
            if (cell.type.split("-")[0] == "conveyor" or cell.type.split("-")[0] == "connector") and cell.rect.colliderect(self.rect):
                return True, cell.type
        return False, None

def spawn(type_str, pos):
    items.append(Item(item_types[type_str], pos))