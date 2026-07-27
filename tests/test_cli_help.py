import subprocess
import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


class TestCliHelp(unittest.TestCase):
    def run_cli(self, *arguments: str) -> str:
        result = subprocess.run(
            [sys.executable, "main.py", *arguments],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout

    def test_general_help_lists_commands(self):
        output = self.run_cli("help")

        self.assertIn("Show help for all commands", output)
        self.assertIn("countdown", output)
        self.assertIn("pomodoro", output)

    def test_command_help_lists_arguments(self):
        output = self.run_cli("help", "countdown")

        self.assertIn("--minutes", output)
        self.assertIn("--note", output)


if __name__ == "__main__":
    unittest.main()
