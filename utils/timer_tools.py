from datetime import datetime, timedelta

def format_minutes(minutes: int) -> str:
    """
        Convert a duration in minutes into a human-readable string.

        Examples:
            62 minutes becomes "1h 2m".
            60 minutes becomes "1h".
            23 minutes becomes "23m".

        Args:
            minutes: The duration to convert, in minutes. Must be at least 0.

        Returns:
            str: The formatted duration.
    """
    if minutes < 0:
        raise ValueError("Must be 0 minutes or greater to convert.")

    if minutes == 0:
        return "0m"
    if minutes % 60 == 0:
        return f"{minutes // 60}h"
    if minutes < 60:
        return f"{minutes}m"
    else:
        return f"{minutes // 60}h {minutes % 60}m"

def format_seconds():
    # will format to the nearest second instead of minute
    raise NotImplementedError("Format sections has not been implemented yet.")

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