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