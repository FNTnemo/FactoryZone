# type, image
import pygame.image

from items import recipes, item_types
from main_settings import WINDOW_WIDTH, WINDOW_HEIGHT

window_types = {"smelter-window": ("smelter-window", pygame.image.load("images/hud/windows/smelter_window.png").convert_alpha()),
                "close-icon": ("close-icon", pygame.image.load("images/hud/windows/close_icon.png").convert_alpha())}
opened_windows = []

def create_window(cell):
    if len(opened_windows) == 0:
        typec = cell.type.split("-")[0]
        img = window_types[f"{typec}-window"][1]
        window = Window(window_types["smelter-window"], (WINDOW_WIDTH//2 - img.get_width()//2, WINDOW_HEIGHT//2 - img.get_height()//2), cell)
        opened_windows.append(window)

def close_window():
    for opened_window in opened_windows:
        if opened_window.elt == "window":
            opened_windows.remove(opened_window)

class Window:
    def __init__(self, typei, pos, cell):
        self.elt = "window"
        self.type = typei[0]
        self.image = typei[1]
        self.rect = self.image.get_rect(topleft=pos)
        self.window_size = self.image.get_size()

        self.pos = pos
        self.cell = cell
        self.window_elements = []

        self.window_elements.append(WindowBrick(window_types["close-icon"], (WINDOW_WIDTH - self.rect.x, WINDOW_HEIGHT - self.rect.y - self.image.get_height()), self))
        self.typec = cell.type.split("-")[0]

        # recipe cell
        if self.typec == "smelter":
            font = pygame.font.Font(None, 20)
            for i in range(len(cell.recipes)):
                #typei = (type, image, recipe_type)
                self.window_elements.append(WindowBrick(("recipe", item_types[cell.recipes[i][0]][1], cell.recipes[i][0]), (100, 100 + i * 64), self))
                self.window_elements.append(WindowText())

        # items in inventory


    def update(self):
        for brick in self.window_elements:
            brick.update()




class WindowBrick:
    def __init__(self, typei, pos, window):
        self.typei = typei
        self.type = typei[0]
        self.image = typei[1]
        self.rect = self.image.get_rect(topleft=pos)
        self.window = window

    def update(self):
        mouse_keys = pygame.mouse.get_pressed()
        if self.type == "close-icon":
            if self.rect.collidepoint(pygame.mouse.get_pos()) and mouse_keys[0]:
                close_window()
        if self.type == "item-cell":
            pass
        if self.type == "recipe":
            if self.rect.collidepoint(pygame.mouse.get_pos()) and mouse_keys[0]:
                self.window.cell.selected_recipe = self.typei[2]

class WindowText:
    def __init__(self, text, font, pos, window):
        self.type = "text"
        self.text = text
        self.font = font
        self.rect = pygame.math.Vector2(pos)
        self.window = window

    def update(self):
        self.window.cell.cell_inventory