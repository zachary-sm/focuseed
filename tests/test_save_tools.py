import json
import sys
import tempfile
import types
import unittest
from datetime import datetime, timedelta
from pathlib import Path
from unittest.mock import patch

from utils.save_tools import (
    append_json_session,
    count_saved_hours,
    calculate_average_session_length,
    get_current_streak,
    load_json_list,
    save_session,
)


class TestSaveTools(unittest.TestCase):
    def test_saving(self):
        result = count_saved_hours(Path("tests/test_data/test_save_tools_data.json"))
        self.assertEqual(result, timedelta(hours=42, minutes=20))

    def test_append_json_session_creates_file_and_preserves_sessions(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "nested" / "sessions.json"
            first = {"note": "First"}
            second = {"note": "Second"}

            append_json_session(first, path)
            append_json_session(second, path)

            self.assertEqual(load_json_list(path), [first, second])

    def test_invalid_json_loads_as_empty_list(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "sessions.json"
            path.write_text("not json", encoding="utf-8")

            self.assertEqual(load_json_list(path), [])

    def test_save_session_serializes_datetimes_and_awards_duration(self):
        start = datetime(2026, 7, 26, 9, 0)
        end = start + timedelta(minutes=42, seconds=59)
        fake_economy_tools = types.ModuleType("utils.economy_tools")
        fake_economy_tools.award_progress = unittest.mock.Mock()

        with (
            patch.dict(sys.modules, {"utils.economy_tools": fake_economy_tools}),
            patch("utils.save_tools.append_json_session") as mock_append,
        ):
            save_session(start, end, "Reading", "Countdown")

        saved_session = mock_append.call_args.kwargs["study_data"]
        self.assertEqual(saved_session["start"], start.isoformat())
        self.assertEqual(saved_session["end"], end.isoformat())
        self.assertEqual(saved_session["note"], "Reading")
        self.assertEqual(saved_session["type"], "Countdown")
        fake_economy_tools.award_progress.assert_called_once_with(42)

    def test_pomodoro_session_is_json_serializable(self):
        start = datetime(2026, 7, 26, 9, 0)
        end = start + timedelta(minutes=25)

        with (
            patch("utils.save_tools.append_json_session") as mock_append,
            patch("utils.economy_tools.award_progress"),
        ):
            save_session(start, end, "Writing", "Pomodoro")

        saved_session = mock_append.call_args.kwargs["study_data"]
        self.assertEqual(saved_session["start"], start.isoformat())
        self.assertEqual(saved_session["end"], end.isoformat())

    def test_average_session_length_is_zero_for_empty_history(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "sessions.json"
            self.assertEqual(calculate_average_session_length(path), timedelta())

    def test_current_streak_counts_consecutive_days_once(self):
        today = datetime.now().date()
        sessions = [
            {"start": f"{today.isoformat()}T09:00:00"},
            {"start": f"{today.isoformat()}T13:00:00"},
            {"start": f"{(today - timedelta(days=1)).isoformat()}T09:00:00"},
            {"start": f"{(today - timedelta(days=2)).isoformat()}T09:00:00"},
        ]

        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "sessions.json"
            path.write_text(json.dumps(sessions), encoding="utf-8")
            self.assertEqual(get_current_streak(path), 3)


if __name__ == "__main__":
    unittest.main()
