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
        gc_s = [[gc.type, gc.direction, gc.rect.topleft] for gc in ground_map_layer]
        bc_s = [[bc.type, bc.direction, bc.rect.topleft, bc.cell_inventory, bc.selected_recipe] for bc in build_map_layer]
        ac_s = [[ac.type, ac.direction, ac.rect.topleft] for ac in auxiliary_map_layer]
        cells = [gc_s] + [bc_s] + [ac_s]

        map_s = [get_loaded_map()]
        player_s = [[player.rect.topleft, (camera.offset.x, camera.offset.y) , player.storage_inventory]]

        data2save = [cells] + [player_s] + [map_s]
        yaml.dump(data2save, save)

def load_game():
    if os.path.isfile(save1_path):
        with open(save1_path) as save:
            data = yaml.full_load(save)
            if data is not None:
                try:
                    # cell-type; direction; position; inventory; selected-recipe
                    gc_l = data[0][0]
                    bc_l = data[0][1]
                    ac_l = data[0][2]
                    player_l = data[1][0]
                    map_l = data[2][0]

                    load_map(map_l)

                    for c in gc_l:
                        ground_map_layer[calc_map_line(c[2][0], c[2][1])] = Cell(cell_types[c[0]], c[1], c[2])
                    for c in bc_l:
                        cell = Cell(cell_types[c[0]], c[1], c[2])
                        cell.cell_inventory = c[3]
                        cell.selected_recipe = c[4]
                        if cell.selected_recipe is not None:
                            cell.crafting_delay_start = cell.selected_recipe[1]  # crafting delay set
                            cell.crafting_delay = cell.crafting_delay_start
                        build_map_layer[calc_map_line(c[2][0], c[2][1])] = cell
                    for c in ac_l:
                        auxiliary_map_layer[calc_map_line(c[2][0], c[2][1])] = Cell(cell_types[c[0]], c[1], c[2])

                    player.rect.topleft = player_l[0]
                    set_storage_inventory(player_l[2])
                    camera.offset.x, camera.offset.y = player_l[1][0], player_l[1][1]

                    print("Save loaded")

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