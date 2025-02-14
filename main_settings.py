WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
#WINDOW_WIDTH = 1920
#WINDOW_HEIGHT = 1080

HALF_WINDOW_WIDTH = WINDOW_WIDTH // 2
HALF_WINDOW_HEIGHT = WINDOW_HEIGHT // 2
cell_size = 64

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
cellular_interaction = {"interactive": ["smelter", "assembler", "storage"],
                        "crafting": ["smelter", "assembler"],
                        "conveyor": ["conveyor", "connector"]}
