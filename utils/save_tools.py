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
    
    # Load the JSON file and append the python list before converting it back
    try:
        with open("data/focus_data.json", "r") as file:
            save_json = json.load(file)
    except json.JSONDecodeError:
        save_json = []

    save_json.append(study_data)

    with open("data/focus_data.json", "w") as file:
        json.dump(save_json, file, indent=4);

def count_saved_hours(path: Path = Path("data/focus_data.json")) -> timedelta:
    """
        Counts all elapsed study time in a json.
    
        Args:
            path: The path to the json.

        Returns:
            timedelta: The total elapsed study time across all sessions.
    """
    
    
    total_duration = timedelta()

    with open(path, "r") as f:
        data = json.load(f)

    for session in data:
        start = datetime.fromisoformat(session["start"])
        end = datetime.fromisoformat(session["end"])

        total_duration += end - start

    return total_duration

def calculate_average_session_length(path: Path = Path("data/focus_data.json")) -> timedelta:
    total_hours = count_saved_hours(path)
    
    return total_hours / get_session_count(path)

def get_session_count(path: Path = Path("data/focus_data.json")) -> int:
    with open(path, "r") as f:
        data = json.load(f)

    return len(data)