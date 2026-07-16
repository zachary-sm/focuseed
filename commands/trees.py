from pathlib import Path
from utils.save_tools import load_json_dict
from utils.formatting_tools import print_bold

def show_trees(path: Path = Path("data/shop_data.json")):
    """
        Shows the user a list of their owned trees.
    """

    shop_data = load_json_dict(path)

    owned_trees_list = shop_data["inventory"]

    print_bold("Owned trees:")
    for tree in owned_trees_list:
        print(tree)