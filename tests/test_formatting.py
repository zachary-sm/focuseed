import unittest
from utils.timer_tools import *


class TestFormatMinutes(unittest.TestCase):
    def test_under_one_hour(self):
        self.assertEqual(format_minutes(23), "23m")

    def test_one_hour(self):
        self.assertEqual(format_minutes(60), "1h")

    def test_multiple_hours(self):
        self.assertEqual(format_minutes(120), "2h")

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


if __name__ == "__main__":
    unittest.main()