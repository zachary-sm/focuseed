import utils.save_tools
import argparse
import commands.countdown, commands.stopwatch, commands.log, commands.stats
import constants

def main():
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

    # stats command
    countdown = subparsers.add_parser("stats")

    # log command
    countdown = subparsers.add_parser("log")
    countdown.add_argument("--count", type=int, help="Amount of most recent messages to display", default=5)

    # version command
    parser.add_argument("--version", action="version",version=f"focuseed {constants.VERSION}")
    
    # The command line input
    args = parser.parse_args()

    match args.command:
        case "stopwatch":
            commands.stopwatch.start_stopwatch(args.note)
        case "countdown":
            commands.countdown.start_countdown(args.minutes, args.note)
        case "log":
            commands.log.generate_log(args.count)
        case "stats":
            commands.stats.show_stats()

if __name__ == "__main__":
    main()