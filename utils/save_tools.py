import json
from datetime import *

def save_session(start_time: datetime, end_time: datetime, tag):
    """
        Save a study session to the save file.
    
        Args:
            start_time: The time the session started.
            end_time: The time the session ended.
            tag: The user's typed session tag.
    """
    

    study_data = {
        "start": start_time.isoformat(),
        "end": end_time.isoformat(),
        "tag": tag
    }

    with open("data/focus_data.json", "w") as file:
        json.dump(study_data, file, indent=4);

    print("Session save successful - remove this")