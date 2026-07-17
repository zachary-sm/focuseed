from utils.formatting_tools import print_bold
from utils.economy_tools import get_balance
def show_balance():
    print_bold("Growbux Balance:")
    print(f"{get_balance()}₲")
