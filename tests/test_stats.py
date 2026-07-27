import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

from commands.stats import show_stats


class TestStats(unittest.TestCase):
    def test_correct_long_history(self):
        fixture_path = Path("tests/test_data/test_save_tools_data.json")
        output = StringIO()

        with redirect_stdout(output):
            show_stats(fixture_path)

        self.assertEqual(
            output.getvalue(),
            "Total Focus Time: 42h 20m\n"
            "Separate Days Focused: 4 days\n"
            "Current Streak: 0\n"
            "Total Focus Sessions: 4 sessions\n"
            "Average Focus Session Length: 10h 35m\n",
        )


if __name__ == "__main__":
    unittest.main()
