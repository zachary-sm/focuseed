def format_minutes(minutes: int) -> str:
    """
        Convert a number (1 or greater) of minutes into a nicely formatted hours + minutes.
        62 minutes becomes "1h 2m"
        60 minutes becomes "1h"
        23 minutes becomes "23m"    

        args:
            minutes: The minutes to convert
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
    pass
