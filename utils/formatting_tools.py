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

def get_choice(prompt: str, choices: set):
    """
    Prompt the user to choose from a set of valid inputs.

    Repeatedly asks the user for input until they enter one of values in
    `choices`. The corresponding value is returned. Input and output are
    converted to lowercase.

    Args:
        prompt: The message displayed to the user when requesting input.
        choices: A set of the possible choices the user can enter.

    Returns:
        The value the user input if it's in the `choices` list.
    """
    choices = {choice.lower() for choice in choices}
    while True:
        print(f"Options: {choices}")
        
        choice = input(prompt).strip().lower()

        if choice in choices:
            return choice

        print("Invalid choice.")

        print(f"ERROR: {choice} is not in {choices}")