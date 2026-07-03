import time
import utils.timer_tools
from datetime import datetime
import utils.save_tools

def start_countdown(minutes: int, note: str):
    start_time = datetime.now()
    
    print(f'Started a {minutes} minute session at {start_time.strftime("%H:%M")} with note "{note}"')
    print("Press Ctrl+C to stop early and forfeit the study session (it won't be saved).")

    try:
        time.sleep(60 * minutes)
    except KeyboardInterrupt:
        print()
        print("Timer exited early. No progress tracked.")
        return
    
    end_time = datetime.now()
    

    print(f"Successfuly focused for {utils.timer_tools.format_minutes(minutes)}")
    
    utils.save_tools.save_session(start_time, end_time, note)
