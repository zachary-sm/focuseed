from utils.timer_tools import countdown_timer

# TODO: Add auto start 
def start_pomodoro(focus_minutes: int, 
                   short_break_minutes: int, 
                   long_break_minutes: int, 
                   sessions_before_long_break: int,
                   note: str):
    session_number = 1
    while True:
        print(f"Starting Pomodoro session #{session_number}")

        next_break_is_long = False
        try:
            countdown_timer(focus_minutes)
        except KeyboardInterrupt:
            break
        
        print(f"Session #{session_number} complete!")
        
        # TODO: Make timer not end at 0:01 and just go away. Make the pomodoro sessions print on the current line maybe?

        # TODO: Make it run in minutes instead of the debug seconds
        session_mod = session_number % sessions_before_long_break
        try:
            if (session_mod != 0):
                print(f"Starting short break timer. Time until long break: {session_mod}")
                countdown_timer(short_break_minutes)
            else:
                print(f"Starting long break timer!")
                countdown_timer(long_break_minutes)
        except KeyboardInterrupt:
            break

        session_number += 1

    if (session_number > 1):
        print("Pomodoro session complete!")
        print(f"Completed focus sessions: {session_number}")
    
    # TODO: Save the session

    print("Exiting Pomodoro")
