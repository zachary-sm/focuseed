import utils.timer_tools
import time
from datetime import datetime, timedelta, date
from utils.formatting_tools import print_and_clear
def format_minutes(minutes: int) -> str:
    """
        Convert a duration in minutes into a string with hours and minutes.

        Examples:
            62 minutes becomes "1h 2m"
            60 minutes becomes "1h"
            23 minutes becomes "23m"

        Args:
            minutes: The duration to convert, in minutes. Must be at least 0.

        Returns:
            str: The formatted duration.
    """
    if minutes < 0:
        raise ValueError("Must be 0 minutes or greater to convert.")
    if minutes < 60:
        return f"{minutes}m"
    else:
        return f"{minutes // 60}h {minutes % 60}m"

def format_seconds(seconds: int) -> str:
    """
        Convert a duration in seconds into a string with hours, minutes, and seconds.

        Examples:
            3122 seconds becomes "52m 2s".
            84232 minutes becomes "23h 23m 52s"
            3 seconds becomes "3s"

        Args:
            seconds: The duration to convert, in seconds. Must be at least 0.

        Returns:
            str: The formatted duration.
    """
    
    minutes_component = seconds // 60
    seconds_component = seconds % 60
    
    minutes_formatted = format_minutes(minutes_component)

    return f"{minutes_formatted} {seconds_component}s"

def format_timedelta(td: timedelta, show_seconds: bool = True) -> str:
    """
        Return a timedelta formatted as 'Xh Ym Zs'.
    
        If `show_seconds` is false, seconds are omitted except for durations
        shorter than one minute.
    """
    
    total_seconds = int(td.total_seconds())

    hours = total_seconds // 3600
    remainder = total_seconds % 3600

    minutes = remainder // 60
    seconds = remainder % 60

    parts = []

    if hours:
        parts.append(f"{hours}h")
    if minutes:
        parts.append(f"{minutes}m")
    if (seconds and show_seconds) or not parts:
        parts.append(f"{seconds}s")

    return " ".join(parts)

def session_duration_minutes(start_str: str, end_str: str) -> int:
    """
        Calculates the duration in minutes from two ISO 8601 datetime strings.

        Args:
            start_str: The ISO 8601 starting time.
            end_str: The ISO 8601 ending time.

        Returns:
            The duration in minutes.
    """
    
    start = datetime.fromisoformat(start_str)
    end = datetime.fromisoformat(end_str)

    duration_delta = end - start
    
    return int(duration_delta.total_seconds() / 60)

def format_iso_date(iso_time: str) -> str:

    """
    Converts an ISO 8601 datetime string to YYYY/MM/DD format.

    Args:
        iso_time: An ISO 8601 datetime string, such as
            "2026-07-03T14:10:38.048219".

    Returns:
        The date formatted as YYYY/MM/DD.

    Examples:
        >>> format_iso_date("2026-07-03T14:10:38.048219")
        '2026/07/03'
    """

    return datetime.fromisoformat(iso_time).strftime("%Y/%m/%d")

def format_iso_time(iso_time: str):
    """
        Converts an ISO 8601 datetime string into a 24-hour time format.

        Returns:
            The time formatted as HH:MM

        Examples:
        >>> format_iso_time("2026-07-03T14:10:38.048219")
        '14:10'
    """

    return datetime.fromisoformat(iso_time).strftime("%H:%M")

def countdown_timer(target_seconds: int):
    seconds = 0
    while(seconds <= target_seconds):
            print_and_clear(utils.timer_tools.format_seconds(target_seconds - seconds))
            seconds += 1
            time.sleep(1)
    print()

def get_iso_date(iso_time: str) -> date:
    return datetime.fromisoformat(iso_time).date()