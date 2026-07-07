import shutil

def print_divider(repeat_str: str, lines: str = 1):
    """
        Prints a divider across the width of the terminal window.

        Examples:
            >> render_divider("=")
            ====..(terminal length)..====

            >> render_divider("=-=")
            =-==-==-=..(terminal length)..=-==-=

            
        Args:
            repeat_str: The string that will be repeated.
            lines: The number of divider lines that will be repeated.
    """
    
    print(repeat_str * (shutil.get_terminal_size().columns // len(repeat_str)))