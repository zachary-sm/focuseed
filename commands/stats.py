from utils.save_tools import count_saved_hours, calculate_average_session_length, get_separate_days_focused, get_session_count, get_current_streak
from utils.timer_tools import format_timedelta
from pathlib import Path

def show_stats(path: Path = Path("data/focus_data.json") ):
    """
        Shows the user statistical data about their save.

        Examples:
            >>> show_stats()
                Total Focus Time: 43h 57m 12s
                Separate Days Focused: 20 days
                Current Streak: 8 days
                Total Focus Sessions: 32 sessions
                Average Focus Session Length: 1h 16m 12s
    """
    print(f"Total Focus Time: {format_timedelta(count_saved_hours(path))}")
    print(f"Separate Days Focused: {len(get_separate_days_focused(path))} days")
    print(f"Current Streak: {get_current_streak(path)}")
    print(f"Total Focus Sessions: {get_session_count(path)} sessions")
    print(f"Average Focus Session Length: {format_timedelta(calculate_average_session_length(path))}")