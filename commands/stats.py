from utils.save_tools import count_saved_hours, calculate_average_session_length
from utils.timer_tools import format_timedelta

def show_stats():
    """
        Shows the user statistical data about their save.

        Examples:
            >>> show_stats()
                Total Focus Time: 43h 57m
                Separate Days Focused: 20 days
                Current Streak: 8 days
                Total Focus Sessions: 32 sessions
                Average Session Length: 82.42 minutes
    """
    print(f"Total Focus Time: {format_timedelta(count_saved_hours())}")
    print(f"Separate Days Focused: NOT IMPLEMENTED")
    print(f"Average Session Length: {format_timedelta(calculate_average_session_length())}")