import utils.save_tools
import utils.formatting_tools
import utils.economy_tools
from pathlib import Path


def view_shop(shop_trees_path: Path = Path("assets/shop_trees.json"), shop_data_path: Path = Path("data/shop_data.json"), default_shop_data_path=Path("assets/shop_data_default.json")):
    """
    Displays all available trees in the shop and allows the user to purchase one.

    Shows each tree's name, description, price, and growth time. If the user
    chooses to buy a tree, the function verifies that they have enough Growbux
    and do not already own the selected tree before completing the purchase and
    saving the updated inventory.

    Args:
        shop_trees_path: Path to the JSON file containing all available trees.
        shop_data_path: Path to the user's shop data JSON file.
        default_shop_data_path: Path to the default shop data JSON file used if
            the user's shop data does not exist.
    """
    
    shop_trees = utils.save_tools.load_json_dict(shop_trees_path)
    owned_trees_dict = utils.save_tools.get_json_field(field="owned_trees", path=shop_data_path, default_json_path=default_shop_data_path)
    tree_types = set()
    tree_name_to_key = {}

    for tree_key in shop_trees:
        utils.formatting_tools.print_bold(shop_trees[tree_key]["name"])
        if tree_key in owned_trees_dict:
            print(" (OWNED)")

        print(f'Description: {shop_trees[tree_key]["description"]}')
        print(f'Cost: {shop_trees[tree_key]["price"]}')
        print(f'Growth time: {shop_trees[tree_key]["growth_time"]}')
        print()

        display_name = shop_trees[tree_key]["name"].strip().lower()
        tree_types.add(display_name)
        tree_name_to_key[display_name] = tree_key

    is_buying = utils.formatting_tools.get_choice("Do you want to buy a tree?", {"Y", "N"})

    if is_buying == "y":
        tree_to_buy = utils.formatting_tools.get_choice(
            "Type the name of the tree you want to buy:",
            tree_types
        ).strip().lower()

        tree_key = tree_name_to_key[tree_to_buy]

        growbux_balance = utils.economy_tools.get_balance()
        tree_price = shop_trees[tree_key]["price"]

        # Check if the user has enough currency
        if growbux_balance < tree_price:
            print(f"Not enough currency! You have {growbux_balance}₲ but that tree costs {tree_price}₲")
            return

        # Check if the user already owns it
        if tree_key in owned_trees_dict:
            print("You already own that tree!")
            return

        utils.economy_tools.change_growbux(-tree_price)
        owned_trees_dict[tree_key] = 0

        print(f"Successfully purchased {shop_trees[tree_key]['name']}!")

        utils.save_tools.save_to_json_field(
            "owned_trees",
            owned_trees_dict,
            Path("data/shop_data.json")
        )