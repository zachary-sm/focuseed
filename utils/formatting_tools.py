import shutil

def print_divider(repeat_str: str, lines: int = 1):
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
    for _ in range(lines):
        print(repeat_str * (shutil.get_terminal_size().columns // len(repeat_str)))

def print_and_clear(clear_str):
    """Clears the text where the cursor is and then prints the clear_str."""
    print(f"\r{clear_str}\033[K", end="", flush=True)

def print_bold(text):
    print(f"\033[1m{text}\033[0m")