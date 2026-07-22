from pathlib import Path
from utils.save_tools import load_json_dict
from utils.formatting_tools import print_bold

def show_trees(shop_data_path: Path = Path("data/shop_data.json"), tree_path: Path = Path("assets/shop_trees.json")):
    """
        Shows the user a list of their owned trees with a visual bar representation.
    """

    shop_data = load_json_dict(shop_data_path)
    tree_data = load_json_dict(tree_path)
    owned_trees_dict = shop_data["owned_trees"]

    print_bold("Owned trees:")
    for tree_key in owned_trees_dict:
        print(f"{tree_data[tree_key]["name"]} x{shop_data["owned_trees"][tree_key]}")