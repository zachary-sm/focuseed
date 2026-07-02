import utils.save_tools
import argparse
import commands.countdown
from datetime import *

def main():
    print("Welcome to Focuseed")
    
    parser = argparse.ArgumentParser(prog="focuseed")
    
    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    # ARGPARSES:
    # stopwatch command
    stopwatch = subparsers.add_parser("stopwatch")
    stopwatch.add_argument("--minutes", type=int, help="Minumum study time in minutes", default=30)
    stopwatch.add_argument(
        "--note",
        type=str,
        help="A note about this study session",
        default="A focus stopwatch session"
    )
    
    # countdown command
    countdown = subparsers.add_parser("countdown")
    countdown.add_argument("--minutes", type=int, help="Length of countdown in minutes", default=30)
    countdown.add_argument(
        "--note",
        type=str,
        help="A note about this study session",
        default="A focus countdown session"
    )

    # The command line input
    args = parser.parse_args()

    match args.command:
        case "stopwatch":
            pass
        case "countdown":
            commands.countdown.start_countdown(args.minutes, args.note)
    
    print("focuseed finished executing successfully")

if __name__ == "__main__":
    main()