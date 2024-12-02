import pygame

from main_settings import WINDOW_WIDTH, WINDOW_HEIGHT
from map import cell_images, cell_types
from player import camera, player

ui_images = {"vignette": pygame.image.load("images/hud/vignette.png").convert_alpha()}

ui_elements = []

class UI_element(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image

        self.rect = self.image.get_rect(topleft=pos)
        self.type = "UI"

        self.pos = pygame.math.Vector2(pos)

    def rescale(self):
        size = self.image.get_size
        k = size[0] // WINDOW_WIDTH
        if k != 0:
            pygame.transform.scale(self.image, size[0] * k, size[1] * k)

    def update(self):
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

class SelectableItemUI(pygame.sprite.Sprite):
    def __init__(self, type, pos):
        super().__init__()
        self.type = type[0]
        self.image = cell_images[self.type]
        self.rect = self.image.get_rect(topleft=pos)

        self.x0 = self.rect.x
        self.y0 = self.rect.y

        self.selected = False

    def update(self):
        m_keys = pygame.mouse.get_pressed()
        k_keys = pygame.key.get_pressed()

        if m_keys[0]:
            self.take()
        if k_keys[pygame.K_ESCAPE]:
            self.put()

        if self.selected:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.rect.x = mouse_x
            self.rect.y = mouse_y

    def take(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_x, mouse_y):
            self.selected = True
            player.selected_structure_type = self.type

    def put(self):
        self.selected = False
        player.selected_structure_type = "empty"
        self.rect.x, self.rect.y = self.x0, self.y0


def base_hud_init():
    ui_elements.append(SelectableItemUI(cell_types["drill"], (
    WINDOW_WIDTH // 4 + camera.offset.x, WINDOW_HEIGHT - WINDOW_HEIGHT // 9 + camera.offset.y)))
    ui_elements.append(UI_element(ui_images["vignette"], (0 + camera.offset.x, 0 + camera.offset.y))) #vignette
