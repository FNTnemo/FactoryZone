WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
current_window_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
window_k = current_window_size[0] / WINDOW_WIDTH

HALF_WINDOW_WIDTH = WINDOW_WIDTH // 2
HALF_WINDOW_HEIGHT = WINDOW_HEIGHT // 2
cell_size = 64
chunk_size = 4
chunk_size_global = chunk_size * cell_size

tps = 60

#colors
yellow = (255, 255, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

# conveyors
conveyor_speed = 2

#buildings
max_item_stack = 512
storage_item_stack = 2048

# cell
cellular_interaction = {"interactive": ["smelter", "assembler", "storage", "drill"],
                        "crafting": ["smelter", "assembler"],
                        "conveyor": ["conveyor", "connector", "spliter"],
                        "with-window": ["smelter", "assembler", "storage"]}
