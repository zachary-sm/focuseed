import shutil

def print_divider(repeat_str: str):
    """
        Prints a divider across the width of the terminal window.

        Examples:
            >> render_divider("=")
            ====..(terminal length)..====

            >> render_divider("=-=")
            =-==-==-=..(terminal length)..=-==-=

            
        Args:
            repeat_str: The string that will be repeated.
    """
    
    print(repeat_str * shutil.get_terminal_size().columns)