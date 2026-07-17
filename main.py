import utils.save_tools
import argparse
import commands.countdown, commands.stopwatch, commands.log, commands.stats, commands.pomodoro, commands.shop, commands.trees, commands.balance
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

    # pomodoro command
    pomodoro = subparsers.add_parser("pomodoro")
    pomodoro.add_argument("--minutes", type=int, help="Length of focus in minutes", default=25)
    pomodoro.add_argument("--short-break", type=int, help="Length of the short break in minutes", default=5)
    pomodoro.add_argument("--long-break", type=int, help="Length of long break in minutes", default=15)
    pomodoro.add_argument("--long-break-interval", "--lbi", type=int, help="Amount of focus sessions before the break is a long", default=4)
    pomodoro.add_argument(
        "--note",
        type=str,
        help="A note about this study session",
        default="A focus countdown session"
    )

    # stats command
    stats = subparsers.add_parser("stats")

    # log command
    log = subparsers.add_parser("log")
    log.add_argument("--count", type=int, help="Amount of most recent messages to display", default=5)

    # shop command
    shop = subparsers.add_parser("shop")

    # trees command
    trees = subparsers.add_parser("trees")

    # balance command
    balance = subparsers.add_parser("balance")

    # version command
    parser.add_argument("--version", action="version",version=f"focuseed {constants.VERSION}")
    
    # The command line input
    args = parser.parse_args()

    match args.command:
        case "stopwatch":
            commands.stopwatch.start_stopwatch(args.note)
        case "countdown":
            commands.countdown.start_countdown(args.minutes, args.note)
        case "pomodoro":
            commands.pomodoro.start_pomodoro(args.minutes, args.short_break, args.long_break, args.long_break_interval, args.note)
        case "log":
            commands.log.generate_log(args.count)
        case "stats":
            commands.stats.show_stats()
        case "shop":
            commands.shop.view_shop()
        case "trees":
            commands.trees.show_trees()
        case "balance":
            commands.balance.show_balance()
if __name__ == "__main__":
    main()