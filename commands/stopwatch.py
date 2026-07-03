import utils.timer_tools
import utils.save_tools
import time
from datetime import datetime

def start_stopwatch(note: str):
    """
        Starts a stopwatch session.

        Can be exited at any time, rewarding the user fully.

        Args:
            note: The session note.
    """
    
    seconds = 0
    start_time = datetime.now()


    print("Started stopwatch.")
    print("Press Ctrl+C to stop and save your session.")
    try:
        while True:
            mins = seconds // 60
            
            # Update current line - for now, hardcode seconds
            print(f"\rElapsed: {utils.timer_tools.format_minutes(mins)} {seconds % 60}s", end="", flush=True)

            time.sleep(1)

            seconds += 1
    except KeyboardInterrupt:
        print()
        print(f"Successfully focused for {utils.timer_tools.format_minutes(mins)}")
        
        end_time = datetime.now()
        utils.save_tools.save_session(start_time, end_time, note, "Stopwatch")
        