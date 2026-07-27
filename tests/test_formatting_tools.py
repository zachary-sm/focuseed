import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from utils.formatting_tools import get_choice, print_and_clear, print_bold


class TestFormattingTools(unittest.TestCase):
    def test_get_choice_retries_and_normalizes_input(self):
        with patch("builtins.input", side_effect=["wrong", "  YES  "]):
            with redirect_stdout(StringIO()):
                choice = get_choice("Continue?", {"yes", "no"})

        self.assertEqual(choice, "yes")

    def test_print_helpers_emit_terminal_sequences(self):
        output = StringIO()

        with redirect_stdout(output):
            print_bold("Heading")
            print_and_clear("00m 01s")

        self.assertEqual(output.getvalue(), "\033[1mHeading\033[0m\n\r00m 01s\033[K")


if __name__ == "__main__":
    unittest.main()