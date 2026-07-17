from datetime import datetime
from utils.timer_tools import countdown_timer
from utils.save_tools import save_session

# TODO: Add auto start 
def start_pomodoro(focus_minutes: int, 
                   short_break_minutes: int, 
                   long_break_minutes: int, 
                   sessions_before_long_break: int,
                   note: str):
    
    session_number = 1
    while True:
        print(f"Started Pomodoro session #{session_number}")

        next_break_is_long = False
        start_time = datetime.now()
        try:
            countdown_timer(focus_minutes * 60)
        except KeyboardInterrupt:
            break
        
        print(f"Session #{session_number} complete!")
        
        end_time = datetime.now()
        save_session(start_time, end_time, note=f"{note} - Session #{session_number}", session_type="Pomodoro")
        
        session_mod = session_number % sessions_before_long_break
        
        try:
            if (session_mod != 0):
                print(f"Started short break timer. Focus sessions until long break: {sessions_before_long_break - session_mod}")
                countdown_timer(short_break_minutes)
            else:
                print(f"Started long break timer!")
                countdown_timer(long_break_minutes)
        except KeyboardInterrupt:
            break

        session_number += 1

    if (session_number > 1):
        print("Pomodoro session complete!")
        print(f"Completed focus sessions: {session_number - 1}")
    
    print()
    print("Exiting Pomodoro")
