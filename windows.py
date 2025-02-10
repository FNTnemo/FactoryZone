# type, image
import pygame.image

from items import all_recipes, item_types
from main_settings import WINDOW_WIDTH, WINDOW_HEIGHT, black

window_types = {
    "smelter-window": ("smelter-window", pygame.image.load("images/hud/windows/smelter_window.png").convert_alpha()),
    "close-icon": ("close-icon", pygame.image.load("images/hud/windows/close_icon.png").convert_alpha())}

window_font = pygame.font.Font(None, 20)
opened_windows = []


def create_window(cell):
    if len(opened_windows) == 0:
        typec = cell.type.split("-")[0]
        img = window_types[f"{typec}-window"][1]
        window = Window(window_types["smelter-window"],
                        (WINDOW_WIDTH // 2 - img.get_width() // 2, WINDOW_HEIGHT // 2 - img.get_height() // 2), cell)
        opened_windows.append(window)


def close_window():
    for opened_window in opened_windows:
        if opened_window.elt == "window":
            opened_windows.remove(opened_window)


class Window: # main window class
    def __init__(self, typei, pos, cell):
        self.elt = "window"
        self.type = typei[0]
        self.image = typei[1]
        self.rect = self.image.get_rect(topleft=pos)
        self.window_size = self.image.get_size()

        self.pos = pos
        self.cell = cell
        self.window_elements = []
        self.text_window_elements = []

        self.window_elements.append(WindowBrick(window_types["close-icon"], (
            WINDOW_WIDTH - self.rect.x, WINDOW_HEIGHT - self.rect.y - self.image.get_height()), self))
        self.typec = cell.type.split("-")[0]

        # recipe cell
        if self.typec == "smelter":
            font = pygame.font.Font(None, 20)
            for i in range(len(cell.recipes)):
                self.window_elements.append(
                    WindowBrick(("recipe", item_types[all_recipes[self.typec][i][0]][1], cell.recipes[i]),
                                (self.rect.x + 200 + i * 65, self.rect.y + 50), self))
            if self.cell.selected_recipe is not None:
                self.load_recipe()

        # items in inventory

    def update(self):
        for brick in self.window_elements:
            brick.update()
        for text in self.text_window_elements:
            text.update()

    def change_recipe(self, recipe_str):
        self.cell.selected_recipe = None  # cler all elements old window
        self.cell.cell_inventory.clear()
        for el in self.window_elements:
            if el.type == "item-cell":
                self.window_elements.remove(el)
        for el in self.text_window_elements:
            self.text_window_elements.remove(el)

        for recipe in all_recipes[self.typec]:  # write new data
            if recipe[0] == recipe_str:
                self.cell.selected_recipe = recipe
        for id in range(len(self.cell.selected_recipe[2])):
            self.cell.cell_inventory.append([self.cell.selected_recipe[2][id][0], 0])
            self.window_elements.append( # adding graphics elements
                WindowBrick(("item-cell", item_types[self.cell.selected_recipe[2][id][0]][1]),
                            (self.rect.x + 33, self.rect.y + 50 + 42 * id), self))
            self.text_window_elements.append( # adding text elements
                WindowTextBrick(["item-count-text", id], self.cell.cell_inventory[id][1], window_font,
                                (self.rect.x + 85, self.rect.y + 50 + 42 * id), self))

    def load_recipe(self):
        for el in self.window_elements:
            if el.type == "item-cell":
                self.window_elements.remove(el)
        for el in self.text_window_elements:
            self.text_window_elements.remove(el)

        for id in range(len(self.cell.selected_recipe[2])):
            self.window_elements.append(
                WindowBrick(("item-cell", item_types[self.cell.selected_recipe[2][id][0]][1]),
                            (self.rect.x + 33, self.rect.y + 50 + 42 * id), self))
            self.text_window_elements.append(
                WindowTextBrick(["item-count-text", id], self.cell.cell_inventory[id][1], window_font,
                                (self.rect.x + 85, self.rect.y + 50 + 42 * id), self))


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
                self.window.change_recipe(self.typei[2][0])


class WindowTextBrick:
    def __init__(self, info, text, font, pos, window):
        self.info = info
        self.type = self.info[0]
        self.text = str(text)
        self.font = font
        self.rect = pygame.math.Vector2(pos)
        self.window = window

    def update(self):
        if self.type == "item-count-text" and len(self.window.cell.cell_inventory) - 1 >= self.info[1]:
            self.text = str(self.window.cell.cell_inventory[self.info[1]][1])

    def render(self):
        return self.font.render(self.text, True, black)
