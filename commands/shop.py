import utils.save_tools
import utils.formatting_tools
from pathlib import Path

def view_shop(shop_tree_path: Path = Path("assets/shop_trees.json")):
    shop_data = utils.save_tools.load_json_list(shop_tree_path)

    print()
    utils.formatting_tools.print_divider("=")
    print()

    tree_types = set()


    for item in shop_data:
        utils.formatting_tools.print_bold(f"{item["name"]}")
        print(f"Description: {item["description"]}")
        print(f"Cost: {item["price"]}")
        print(f"Growth time: {item["growth_time"]}")
        print()
        tree_types.add(item["name"])

    is_buying = utils.formatting_tools.get_choice('Do you want to buy a tree?', {"Y", "N"})

    if (is_buying == "y"):
        tree_to_buy = utils.formatting_tools.get_choice('Type the name of the tree you want to buy.', tree_types)

        can_buy = True
        
        # Check if the user has enough currency
        
        # Check if the user already owns it

        # Add it to the user's save and take away the currency if all of the above is true