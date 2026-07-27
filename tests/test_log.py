import json
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch

from commands.log import generate_log


class TestGenerateLog(unittest.TestCase):
    def test_empty_history_reports_no_sessions(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "sessions.json"
            path.write_text("[]", encoding="utf-8")
            output = StringIO()

            with redirect_stdout(output):
                generate_log(path=path)

        self.assertEqual(output.getvalue(), "There are no focus sessions yet.\n\n")

    def test_zero_count_displays_no_session_entries(self):
        sessions = [
            {"start": "2026-07-26T10:00:00", "end": "2026-07-26T10:45:00", "note": "Newest", "type": "Stopwatch"},
        ]

        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "sessions.json"
            path.write_text(json.dumps(sessions), encoding="utf-8")
            output = StringIO()

            with redirect_stdout(output):
                generate_log(count=0, path=path)

        self.assertEqual(output.getvalue(), "The 0 most recent focus sessions:\n\n")

    def test_log_shows_most_recent_session_first(self):
        sessions = [
            {"start": "2026-07-25T09:00:00", "end": "2026-07-25T09:30:00", "note": "Older", "type": "Countdown"},
            {"start": "2026-07-26T10:00:00", "end": "2026-07-26T10:45:00", "note": "Newest", "type": "Stopwatch"},
        ]

        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "sessions.json"
            path.write_text(json.dumps(sessions), encoding="utf-8")
            output = StringIO()

            with patch("commands.log.utils.formatting_tools.print_divider") as mock_divider:
                with redirect_stdout(output):
                    generate_log(count=1, path=path)

        self.assertIn("The 1 most recent focus sessions:", output.getvalue())
        self.assertIn("Newest", output.getvalue())
        self.assertNotIn("Older", output.getvalue())
        self.assertIn("Date: 2026/07/26", output.getvalue())
        self.assertIn("Duration: 45m", output.getvalue())
        mock_divider.assert_called_once_with("=")


if __name__ == "__main__":
    unittest.main()

