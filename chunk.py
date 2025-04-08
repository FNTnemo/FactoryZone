import pygame

from main_settings import cell_size, chunk_size


class Chunk:
    def __init__(self, cells):
        self.position = pygame.math.Vector2
        self.cells = cells

        self.rect = pygame.Rect(self.position.x, self.position.y, cell_size * chunk_size, cell_size * chunk_size)

    def update(self):
        pass

    def render(self):
        pass