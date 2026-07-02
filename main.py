import utils.save_tools
import argparse
import commands.countdown
from datetime import *

def main():
    print("Welcome to Focuseed")
    
    parser = argparse.ArgumentParser()

    parser.add_argument("minutes", type=int)
    parser.add_argument("--tag")

    args = parser.parse_args()

    commands.countdown(args.minutes, args.tag)

    print("Program successfully executed.")

if __name__ == "__main__":
    main()