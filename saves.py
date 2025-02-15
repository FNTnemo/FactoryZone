import yaml
import os

from map import ground_map_layer, build_map_layer, calc_map_line, Cell, cell_types, \
    load_map, get_loaded_map, auxiliary_map_layer, map1, set_storage_inventory
from player import player, camera

saves_path = "saves"
save1_path = "saves/save.fz"

def save_game():
    if not os.path.isdir(saves_path):
        os.mkdir(saves_path)

    with open(save1_path, "w+", newline="") as save:
        # cell-type; direction; position; inventory; selected-recipe
        data2save = []
        data2save.append(["map-info", get_loaded_map()])
        for gc in ground_map_layer:
            data2save.append(["ground", gc.type, gc.direction, gc.rect.topleft])
        for bc in build_map_layer:
            data2save.append(["build", bc.type, bc.direction, bc.rect.topleft, bc.cell_inventory, bc.selected_recipe])
        for ac in auxiliary_map_layer:
            data2save.append(["aux", ac.type, ac.direction, ac.rect.topleft])
        #for item in items:
            #data2save.append(["item", item.type, item.rect.topleft, item.direction, item.conveyor_queue])
        data2save.append(["player", player.rect.topleft, (camera.offset.x, camera.offset.y) , player.storage_inventory])
        yaml.dump(data2save, save)

def load_game():
    if os.path.isfile(save1_path):
        with open(save1_path) as save:
            data = yaml.full_load(save)
            if data is not None:
                try:
                    load_map(data[0][1])
                    for id in range(len(data)):
                       # typei type direction position | inventory recipe
                       typei = data[id][0]
                       if typei == "ground":
                           ground_map_layer[calc_map_line(data[id][3][0], data[id][3][1])] = Cell(cell_types[data[id][1]], data[id][2], data[id][3])
                       if typei == "build":
                           cell = Cell(cell_types[data[id][1]], data[id][2], data[id][3])
                           cell.cell_inventory = data[id][4]
                           cell.selected_recipe = data[id][5]
                           if cell.selected_recipe is not None:
                               cell.crafting_delay_start = cell.selected_recipe[1]  # crafting delay set
                               cell.crafting_delay = cell.crafting_delay_start
                           build_map_layer[calc_map_line(data[id][3][0], data[id][3][1])] = cell
                       if typei == "aux":
                           auxiliary_map_layer[calc_map_line(data[id][3][0], data[id][3][1])] = Cell(cell_types[data[id][1]], data[id][2], data[id][3])
                       # typei type position direction conveyor_queue
                       #if typei == "item":
                       #    item = Item(item_types[data[id][1]], data[id][2])
                       #    item.direction = data[id][3]
                       #    item.conveyor_queue = data[id][4]
                       #    items.append(item)

                       if typei == "player":
                           player.rect.topleft = data[id][1]
                           set_storage_inventory(data[id][3])
                           camera.offset.x, camera.offset.y = data[id][2][0], data[id][2][1]
                except Exception:
                    print("Invalid save file")
                    load_map(map1)
            else:
                print("Save file is empty")
                load_map(map1)
    else:
        print("New map created")
        load_map(map1)

def del_save_file(path, file):
    if os.path.exists(path) and os.path.isfile(path + "/" + file):
        os.remove(path + "/" + file)