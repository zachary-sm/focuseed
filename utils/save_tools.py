import json
from typing import Any
from datetime import datetime, timedelta, date
from pathlib import Path
from collections import Counter
from utils.timer_tools import get_iso_date

def save_session(start: datetime, end: datetime, note: str, type: str):
    """
        Save a study session to the save file.

        It saves into a JSON list of sessions.

        Depending on the session type, different JSON formats may be used.
    
        Args:
            start_time: The time the session started.
            end_time: The time the session ended.
            note: The user's typed session note.
            type: The command type of the session.
            
            sessions: The amount of sessions (if applicable)
            session_length: The length of each session (if applicable)
    """
    if (type.lower() == "pomodoro"):
        study_data= {
            "start": start,
            "end": end,
            "note": note,
            "type": type
        }
    else:
        study_data = {
            "start": start.isoformat(),
            "end": end.isoformat(),
            "note": note,
            "type": type
        } 
    append_json_session(study_data=study_data)

def save_to_json_field(field: str, item: Any, path: Path = Path("data/focus_data.json")):
    data = load_json_dict(path)

    data[field] = item

    with open(path, "w") as file:
        json.dump(data, file, indent=4)

def get_json_field(field: str, path: Path = Path("data/focus_data.json"), default_json_path: Path = Path("data/default_shop_data.json")):
    data = load_json_dict(path)

    try:
        return data[field]
    except KeyError:
        default_data = load_json_dict(default_json_path)

        save_to_json_field(field, default_data[field], path)

        return default_data[field]

def append_json_session(study_data: dict, path: Path = Path("data/focus_data.json")):
    """
    Append a study session to the JSON data file.

    Creates the parent directory if it does not exist. If the file is
    missing or contains invalid JSON, a new list is created before the
    session is appended.

    Args:
        study_data: A dictionary representing a single study session.
        path: The path to the JSON file used to store study sessions.
    """
    
    path.parent.mkdir(parents=True, exist_ok=True)

    sessions = load_json_list(path)

    sessions.append(study_data)

    with open(path, "w") as file:
        json.dump(sessions, file, indent=4)

def load_json_list(path = Path("data/focus_data.json")) -> list[dict]:
    """
    Load all data from the JSON data file.

    Creates the parent directory if it does not exist. If the file is
    missing or contains invalid JSON, an empty list is returned.

    Args:
        path: The path to A JSON file.

    Returns:
        A list of the information in that JSON.
    """
    
    path.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        with open(path, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def load_json_dict(path = Path("data/shop_data.json"), default_json_path: Path = Path("data/default_shop_data.json")) -> dict:
    """
    Load all dict data from a JSON file. If it doesn't exist, it makes one
    with the template JSON in the `default_dict` list.

    Creates the parent directory if it does not exist. If the file is
    missing or contains invalid JSON, an empty dictionary is returned.

    Args:
        path: The path to the JSON file.

    Returns:
        A dictionary containing the loaded JSON data.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        with open(path, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        copy_json(default_json_path, path)
        return load_json_dict(path, None)

def count_saved_hours(path: Path = Path("data/focus_data.json")) -> timedelta:
    """
        Counts all elapsed study time in a json.
    
        Args:
            path: The path to the json.

        Returns:
            timedelta: The total elapsed study time across all sessions.
    """
    
    
    total_duration = timedelta()

    data = load_json_list(path)

    for session in data:
        start = datetime.fromisoformat(session["start"])
        end = datetime.fromisoformat(session["end"])

        total_duration += end - start

    return total_duration

def calculate_average_session_length(path: Path = Path("data/focus_data.json")) -> timedelta:
    total_hours = count_saved_hours(path)
    
    return total_hours / get_session_count(path)

def get_session_count(path: Path = Path("data/focus_data.json")) -> int:
    data = load_json_list(path)

    return len(data)

def get_separate_days_focused(path: Path = Path("data/focus_data.json")) -> set:
    data = load_json_list(path)

    dates = set()
    
    for item in data:
        dates.add(get_iso_date(item["start"]))

    return dates

def get_current_streak(path: Path = Path("data/focus_data.json")):
    """
    Return the user's current focus streak in consecutive days.

    A streak consists of consecutive calendar days on which the user completed
    at least one focus session. Multiple sessions on the same day count as a
    single day. A streak remains active if the user studied today or yesterday;
    otherwise, the streak is considered broken and 0 is returned.

    Args:
        path: Path to the JSON file containing saved focus session data.
    Returns:
        The number of consecutive days in the user's current focus streak.
    """
    
    dates_focused = sorted(list(get_separate_days_focused(path=path)))
    
    if not dates_focused:
        return 0
    
    # Check if it's been longer than a day since the user studied. If so, the streak is 0.
    if (datetime.now().date() - dates_focused[-1]).days > 1:
        return 0
    
    streak = 1

    # Start at the most recent day which is the last one when sorted.
    for i in reversed(range(1, len(dates_focused))):
        if (dates_focused[i] - dates_focused[i - 1]).days == 1:
            streak += 1
        else:
            break

    return streak

def copy_json(src: Path, dest: Path):
    """Overwrites the json at `dest` with the one at `src`"""

    with open(src, 'r') as file:
        data = json.load(file)

    dest.parent.mkdir(parents=True, exist_ok=True)

    with open(dest, 'w') as file:
        json.dump(data, file, indent=4)

