import utils.save_tools
import utils.formatting_tools
from pathlib import Path

def view_shop(shop_tree_path: Path = Path("assets/shop_trees.json")):
    shop_data = utils.save_tools.load_data(shop_tree_path)

    print()
    utils.formatting_tools.print_divider("=")
    print()

    for item in shop_data:
        utils.formatting_tools.print_bold(f"{item["name"]}")
        print(f"Description: {item["description"]}")
        print(f"Cost: {item["price"]}")
        print(f"Growth time: {item["growth_time"]}")
        print()