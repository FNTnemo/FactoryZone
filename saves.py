import csv
import os
import json

from items import items
from map import ground_map_layer, build_map_layer, auxiliary_map_layer, storage_inventory, calc_map_line, Cell, \
    cell_types
from player import player

saves_path = "saves"
save1_path = "saves/save1.csv"

def save_game():
    if not os.path.isdir(saves_path):
        os.mkdir(saves_path)

    with open(save1_path, "w+", newline="") as save:
        writer = csv.writer(save, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["cell-type", "direction", "selected-recipe-type", "position_x", "position_y", "inventory"])
        writer.writerow(["ground-cells"])

        for cell in ground_map_layer:
            writer.writerow(json.dumps([cell.type, cell.direction, "None", cell.rect.x, cell.rect.y, "None"]) )

        writer.writerow(["build-cells"])
        for cell in build_map_layer:
            if cell.selected_recipe is not None:
                writer.writerow([cell.type, cell.direction, cell.selected_recipe[0], cell.rect.x, cell.rect.y, cell.cell_inventory])
            else: writer.writerow([cell.type, cell.direction, "None", cell.rect.x, cell.rect.y, cell.cell_inventory])

        writer.writerow(["auxiliary-cells"])
        for cell in auxiliary_map_layer:
            writer.writerow([cell.type, cell.direction, "None", cell.rect.x, cell.rect.y, "None"])

        writer.writerow(["item-type", "direction", "position_x", "position_y", "cell-queue"])
        for item in items:
            writer.writerow([item.type, item.direction, item.rect.x, item.rect.y, *item.conveyor_queue])

        writer.writerow(["player", "position", "storage-inventory"])
        writer.writerow(["player", player.rect.topleft, storage_inventory])

def load_game():
    if os.path.isfile(save1_path):
        with open(save1_path) as save:
            reader = csv.reader(save, delimiter=';', quotechar='"')
            data = [x for x in reader]
            id = 0
            while data[id][0] != "build-cells":
                id += 1
                if len(data[id]) > 1:
                    load_ground_cell(data, id)
            id += 1
            while data[id][0] != "auxiliary-cells":
                id += 1
                if len(data[id]) > 1:
                    #load_building_cell(data, id)
                    pass
            id += 1

            #while data[id][0] != "item-type":
            #    id += 1
            #    if len(data[id]) > 1:
            #        load_auxiliary_cell(data, id)
            #while data[id][0] != "player":
            #    id += 1
            #    if len(data[id]) > 1:
            #        pass

def clear_save():
    pass

def load_ground_cell(data, id):
    typec = str(data[id][0])
    direction = int(data[id][1])
    pos = (int(data[id][3]), int(data[id][4]))
    ground_map_layer[calc_map_line(pos[0], pos[1])] = Cell(cell_types[typec], direction, pos)

def load_building_cell(data, id):
    typec = str(data[id][0])
    direction = int(data[id][1])
    pos = (int(data[id][3]), int(data[id][4]))
    cell_inventory = json.loads(data[id][4])

    if data[id][2] != "None":
        selected_recipe = json.loads(data[id][2])
        cell = Cell(cell_types[typec], direction, pos)
        cell.selected_recipe = selected_recipe
        cell.crafting_delay_start = cell.selected_recipe[1]
        cell.crafting_delay = cell.crafting_delay_start
        for id in range(len(cell.selected_recipe[2])):
            cell.cell_inventory.append([cell.selected_recipe[2][id][0], 0])

    else:
        selected_recipe = None
        cell = Cell(cell_types[typec], direction, pos)
        cell.selected_recipe = selected_recipe

    build_map_layer[calc_map_line(pos[0], pos[1])] = cell

def load_auxiliary_cell(data, id):
    typec = str(data[id][0])
    direction = int(data[id][1])
    pos = (int(data[id][3]), int(data[id][4]))
    ground_map_layer[calc_map_line(pos[0], pos[1])] = Cell(cell_types[typec], direction, pos)