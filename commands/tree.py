from pathlib import Path
from utils.formatting_tools import print_bold
from utils.save_tools import load_json_dict, get_json_field

def show_tree(shop_data_path: Path = Path("data/shop_data.json"), tree_path: Path = Path("assets/shop_trees.json")):
    selected_tree = get_json_field("tree_selected", shop_data_path)
    progress = get_json_field("tree_progress", shop_data_path)
    tree_field = get_json_field(selected_tree, tree_path)
    
    print_bold("Currently selected tree:")
    print(tree_field["name"])
    print_bold("Progress:")
    print(f"{progress} / {tree_field["growth_time"]} minutes")