import pygame


from main_settings import cell_size, chunk_size, chunk_size_global


class Chunk:
    def __init__(self, pos, ground_cells, building_cells, aux_cells):
        self.position = pygame.math.Vector2(pos)
        self.rect = pygame.Rect(self.position.x, self.position.y, chunk_size_global, chunk_size_global)

        self.ground_cells = ground_cells
        self.building_cells = building_cells
        self.aux_cells = aux_cells

        self.items = []


    def update(self):
        pass