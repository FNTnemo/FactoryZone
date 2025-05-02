import pygame


from main_settings import cell_size, chunk_size, chunk_size_global

#not used

class Chunk:
    def __init__(self, pos, cells):
        self.position = pygame.math.Vector2(pos)
        self.cells = cells

        self.rect = pygame.Rect(self.position.x, self.position.y, chunk_size_global, chunk_size_global)

        self.items_in_chunk = []

    def update(self):
        from items import items
        for item in items:
            if item.rect.colliderect(self.rect):
                self.items_in_chunk += [item]

def debug_chunk_render(screen, camera):
    from map import get_map_size, loaded_map
    for y in range(get_map_size(loaded_map)[1]//cell_size//chunk_size):
        for x in range(get_map_size(loaded_map)[0]//cell_size//chunk_size):
            pygame.draw.line(screen, (0, 0, 255), (0 - camera.offset.x, y * chunk_size * cell_size - camera.offset.y), (get_map_size(loaded_map)[0] - camera.offset.x, y * chunk_size * cell_size - camera.offset.y), 1)
            pygame.draw.line(screen, (0, 0, 255), (x * chunk_size * cell_size - camera.offset.x, 0 - camera.offset.y), (x * chunk_size * cell_size - camera.offset.x, get_map_size(loaded_map)[1] - camera.offset.y), 1)