import unittest
from datetime import datetime, timedelta
from unittest.mock import patch

from commands.countdown import start_countdown


class TestCountdown(unittest.TestCase):
    def test_completed_countdown_saves_session(self):
        start = datetime(2026, 7, 26, 9, 0)
        end = start + timedelta(minutes=25)

        with (
            patch("commands.countdown.datetime") as mock_datetime,
            patch("commands.countdown.utils.timer_tools.countdown_timer") as mock_timer,
            patch("commands.countdown.utils.save_tools.save_session") as mock_save,
        ):
            mock_datetime.now.side_effect = [start, end]
            start_countdown(25, "Test Note - Hi")

        mock_timer.assert_called_once_with(25 * 60)
        mock_save.assert_called_once_with(start, end, "Test Note - Hi", "Countdown")

    def test_interrupted_countdown_is_not_saved(self):
        with (
            patch(
                "commands.countdown.utils.timer_tools.countdown_timer",
                side_effect=KeyboardInterrupt,
            ),
            patch("commands.countdown.utils.save_tools.save_session") as mock_save,
        ):
            start_countdown(25, "Interrupted")

        mock_save.assert_not_called()

    def test_negative_minutes_are_rejected(self):
        with self.assertRaises(ValueError):
            start_countdown(-1, "Invalid")


if __name__ == "__main__":
    unittest.main()
