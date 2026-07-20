import constants
from pathlib import Path
from utils.save_tools import save_to_json_field, get_json_field

SHOP_DATA_PATH = "data/shop_data.json"

def change_growbux(amount: int):
    """Changes the amount of Growbux in the user's balance. Negatives take it away."""
    save_to_json_field("growbux", get_balance() + amount, Path(SHOP_DATA_PATH))

def award_growbux(amount: int):
    """Changes the amount of Growbux in the user's balance with a message."""
    change_growbux(amount)
    print(f"You earned {amount}₲!")

def get_balance() -> int:
    """Returns the user's Growbux balance."""
    return get_json_field("growbux", Path(SHOP_DATA_PATH))

def change_tree_progress(minutes: int):
    """
    Changes the amount of progress for the user's selected tree. 
    If it reaches the growth theshold, the user is informed of that and it is added to their garden with an award.
    """

    current_progress = get_json_field(field="tree_progress", path=Path("data/shop_data.json"))
    current_tree = get_json_field(field="tree_selected", path=Path("data/shop_data.json"))
    tree_dict = get_json_field(field=current_tree, path=Path("assets/shop_trees.json"))
    growth_progress = tree_dict["growth_time"]

    if current_progress > growth_progress:
        new_progress = 0
        print(f"Your {tree_dict["name"]} has grown!")
    else:
        new_progress = minutes + current_progress
    
    save_to_json_field(field="tree_progress", item=new_progress, path=Path("data/shop_data.json"))
    

def award_progress(minutes: int):
    """Awards the user an amount of money and some tree growth for their study session."""
    award_growbux(minutes * constants.GROWBUX_PER_MINUTE)
    change_tree_progress(minutes)
