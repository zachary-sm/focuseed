import json
import utils.formatting_tools
from pathlib import Path
from utils.timer_tools import format_minutes, session_duration_minutes, format_iso_date, format_iso_time
from utils.save_tools import load_data
from datetime import datetime, timedelta

def generate_log(count: int = 5, path: Path = Path("data/focus_data.json")):
    """
        Prints a log of recent study sessions.

        Includes the date, start time, type, and duration in a easy to read way for the user.

        Example:
            -Java Programming 101-
            Date: 10/26/2026
            Start Time: 11:11 AM
            Duration: 1h 26m
            Session Type: Stopwatch

        Args:
            count: The number of most recent sessions that will have their info printed.
    """
    print()
    utils.formatting_tools.print_divider("=")
    print()

    data = load_data(path)

    if len(data) > 0:
        print(f"The {count} most recent focus sessions:")
    else:
        print(f"There are no focus sessions yet.")

    print()

    for session in reversed(data[-count:]):
        note = session["note"]
        date = format_iso_date(session["start"])
        start_time = format_iso_time(session["start"])
        duration = format_minutes(session_duration_minutes(session["start"], session["end"]))
        type = session["type"]

        utils.formatting_tools.print_bold(f"{note}")
        print("Date: " + date)
        print("Start Time: " + start_time)
        print("Duration: " + duration)
        print("Session type: " + type)
        print()
        utils.formatting_tools.print_divider("=")
        print()
        
        



