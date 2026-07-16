import utils.save_tools
import utils.formatting_tools
from pathlib import Path

def view_shop(shop_trees_path: Path = Path("assets/shop_trees.json"), shop_data_path: Path = Path("data/shop_data.json")):
    shop_trees = utils.save_tools.load_json_dict(shop_trees_path)
    shop_data = utils.save_tools.load_json_dict(shop_data_path)

    tree_types = set()


    for tree_key in shop_trees:
        utils.formatting_tools.print_bold(f'{shop_trees[tree_key]["name"]}')
        print(f'Description: {shop_trees[tree_key]["description"]}')
        print(f'Cost: {shop_trees[tree_key]["price"]}')
        print(f'Growth time: {shop_trees[tree_key]["growth_time"]}')
        print()
        tree_types.add(shop_trees[tree_key]["name"])

    is_buying = utils.formatting_tools.get_choice('Do you want to buy a tree?', {"Y", "N"})

    if (is_buying == "y"):
        tree_to_buy = utils.formatting_tools.get_choice('Type the name of the tree you want to buy:', tree_types)
        
        # Check if the user has enough currency
        if (shop_data["currency"]["growbux"] < shop_trees[tree_to_buy]["price"]):
            print(f"Not enough currency! You have {shop_data["currency"]["growbux"]}₲ but that tree costs {shop_trees[tree_to_buy]["price"]}₲")
            return

        owned_trees_list = shop_data["inventory"]

        # Check if the user already owns it
        if (tree_to_buy in owned_trees_list):
            print(f"You already own that tree!")
            return

        owned_trees_list.append(tree_to_buy)

        print(f"Successfully purchased {tree_to_buy}!")
        
        utils.save_tools.save_to_json_field("inventory", owned_trees_list, Path("data/shop_data.json"))
