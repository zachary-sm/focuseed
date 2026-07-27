import unittest
from datetime import datetime, timedelta
from unittest.mock import patch

from commands.pomodoro import start_pomodoro


class TestPomodoro(unittest.TestCase):
    def test_invalid_long_break_interval_is_rejected(self):
        with self.assertRaises(ValueError):
            start_pomodoro(25, 5, 15, 0, "Writing")

    def test_completed_focus_uses_short_break_in_seconds(self):
        start = datetime(2026, 7, 26, 9, 0)
        end = start + timedelta(minutes=25)

        with (
            patch("commands.pomodoro.datetime") as mock_datetime,
            patch(
                "commands.pomodoro.countdown_timer",
                side_effect=[None, KeyboardInterrupt],
            ) as mock_timer,
            patch("commands.pomodoro.save_session") as mock_save,
        ):
            mock_datetime.now.side_effect = [start, end]
            start_pomodoro(25, 5, 15, 4, "Writing")

        self.assertEqual(mock_timer.call_args_list, [unittest.mock.call(1500), unittest.mock.call(300)])
        mock_save.assert_called_once_with(start, end, note="Writing - Session #1", session_type="Pomodoro")

    def test_completed_focus_uses_long_break_at_interval(self):
        with (
            patch(
                "commands.pomodoro.countdown_timer",
                side_effect=[None, KeyboardInterrupt],
            ) as mock_timer,
            patch("commands.pomodoro.save_session"),
        ):
            start_pomodoro(25, 5, 15, 1, "Writing")

        self.assertEqual(mock_timer.call_args_list, [unittest.mock.call(1500), unittest.mock.call(900)])
