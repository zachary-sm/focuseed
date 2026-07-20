from pathlib import Path
from utils.save_tools import load_json_dict
from utils.formatting_tools import get_choice

def switch_tree(shop_data_path: Path = Path("data/shop_data.json"), tree_path: Path = Path("assets/shop_trees.json")):
    """
        Allows the user to switch to a tree to plant
    """
    tree_data = load_json_dict(tree_path)
    shop_data = load_json_dict(shop_data_path)
    owned_trees_list = shop_data["inventory"]
    owned_trees_set = set(owned_trees_list)

    choice = get_choice(prompt="Which tree would you like to plant?", choices=owned_trees_set)
    print(f"Chosen {tree_data[choice]["name"]}")