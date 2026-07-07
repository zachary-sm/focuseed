import json
from datetime import *
from pathlib import Path

def save_session(start_time: datetime, end_time: datetime, note: str, type: str):
    """
        Save a study session to the save file.

        It saves into a JSON list of sessions.
    
        Args:
            start_time: The time the session started.
            end_time: The time the session ended.
            note: The user's typed session note.
    """
    

    study_data = {
        "start": start_time.isoformat(),
        "end": end_time.isoformat(),
        "note": note,
        "type": type
    }
    
    append_session(study_data=study_data)

def append_session(study_data: dict, path: Path = Path("data/focus_data.json")):
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

    sessions = load_sessions(path)

    sessions.append(study_data)

    with open(path, "w") as file:
        json.dump(sessions, file, indent=4)

def load_sessions(path = Path("data/focus_data.json")) -> list:
    """
    Load all study sessions from the JSON data file.

    Creates the parent directory if it does not exist. If the file is
    missing or contains invalid JSON, an empty list is returned.

    Args:
        path: The path to the JSON file containing study sessions.

    Returns:
        A list of study session dictionaries.
    """
    
    path.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        with open(path, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def count_saved_hours(path: Path = Path("data/focus_data.json")) -> timedelta:
    """
        Counts all elapsed study time in a json.
    
        Args:
            path: The path to the json.

        Returns:
            timedelta: The total elapsed study time across all sessions.
    """
    
    
    total_duration = timedelta()

    data = load_sessions(path)

    for session in data:
        start = datetime.fromisoformat(session["start"])
        end = datetime.fromisoformat(session["end"])

        total_duration += end - start

    return total_duration

def calculate_average_session_length(path: Path = Path("data/focus_data.json")) -> timedelta:
    total_hours = count_saved_hours(path)
    
    return total_hours / get_session_count(path)

def get_session_count(path: Path = Path("data/focus_data.json")) -> int:
    data = load_sessions(path)

    return len(data)