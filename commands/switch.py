from pathlib import Path
from utils.save_tools import load_json_dict, get_json_field, save_to_json_field
from utils.formatting_tools import get_choice

def switch_tree(shop_data_path: Path = Path("data/shop_data.json"), tree_path: Path = Path("assets/shop_trees.json")):
    """
        Allows the user to switch to a tree to plant
    """
    tree_data = load_json_dict(tree_path)
    owned_trees_set = set(get_json_field(field="owned_trees", path=shop_data_path))

    choice = get_choice(prompt="Which tree would you like to plant?", choices=owned_trees_set)
    print(f"Chosen {tree_data[choice]["name"]}")
    save_to_json_field(field="tree_selected", item=choice, path=Path("data/shop_data.json"))