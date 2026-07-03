import json
from datetime import *
from pathlib import Path

def save_session(start_time: datetime, end_time: datetime, note: str, type: str):
    """
        Save a study session to the save file.
    
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

    with open("data/focus_data.json", "w") as file:
        json.dump(study_data, file, indent=4);

    print("Session save successful - remove this")

def count_saved_hours(path: Path = Path("../data/focus_data.json")) -> timedelta:
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