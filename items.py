import pygame.sprite

items = []
#
item_types = {"stone": []}
class Item(pygame.sprite.Sprite):
    def __init__(self, type, pos):
        super().__init__()
        self.image = ...
        self.rect = self.image.get_rect(topleft=(pos[0], pos[1]))

    def update(self):
        pass

    def on_conveyor(self):
        pass
