import unittest
from unittest.mock import call, patch
from utils.timer_tools import countdown_timer, format_minutes, format_seconds

class TestFormatMinutes(unittest.TestCase):
    def test_under_one_hour(self):
        self.assertEqual(format_minutes(23), "23m")

    def test_one_hour(self):
        self.assertEqual(format_minutes(60), "1h 0m")

    def test_multiple_hours(self):
        self.assertEqual(format_minutes(120), "2h 0m")

    def test_hour_and_minutes(self):
        self.assertEqual(format_minutes(62), "1h 2m")

    def test_multiple_hours_and_minutes(self):
        self.assertEqual(format_minutes(135), "2h 15m")

    def test_one_minute(self):
        self.assertEqual(format_minutes(1), "1m")

    def test_zero_minutes(self):
        self.assertEqual(format_minutes(0), "0m")

    def test_negative_minutes(self):
        with self.assertRaises(ValueError):
            format_minutes(-52)


class TestFormatSeconds(unittest.TestCase):
    def test_under_one_minute(self):
        self.assertEqual(format_seconds(23), "0m 23s")

    def test_one_minute(self):
        self.assertEqual(format_seconds(60), "1m 0s")

    def test_one_hour(self):
        self.assertEqual(format_seconds(3600), "1h 0m 0s")

    def test_over_one_hour(self):
        self.assertEqual(format_seconds(4211), "1h 10m 11s")

    def test_negative_seconds(self):
        with self.assertRaises(ValueError):
            format_seconds(-52)


class TestCountdownTimer(unittest.TestCase):
    def test_countdown_sleeps_once_per_requested_second(self):
        with (
            patch("utils.timer_tools.print_and_clear") as mock_print,
            patch("utils.timer_tools.time.sleep") as mock_sleep,
        ):
            countdown_timer(2)

        self.assertEqual(
            mock_print.call_args_list,
            [call("0m 2s"), call("0m 1s"), call("0m 0s")],
        )
        self.assertEqual(mock_sleep.call_count, 2)

    def test_negative_countdown_seconds_are_rejected(self):
        with self.assertRaises(ValueError):
            countdown_timer(-1)


if __name__ == "__main__":
    unittest.main()
