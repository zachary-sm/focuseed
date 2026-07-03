import json
from pathlib import Path
from utils.timer_tools import format_minutes, session_duration_minutes
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

    with open(path, "r") as file:
        data = json.load(file) 

    for session in reversed(data[-count:]):
        note = session["info"]
        date = "NOT IMPLEMENTED"
        # Get the duration in a readable minutes format
        duration = format_minutes(session_duration_minutes(session["start"], session["end"]))
        type = session["type"]

        print(f"-{note}-")
        print("Date: " + date)
        print("Duration: " + duration)
        print("Session type: " + type)



