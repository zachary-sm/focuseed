import unittest
from commands.countdown import *
from unittest.mock import patch

class TestCountdown(unittest.TestCase):
    @patch("commands.countdown.time.sleep")
    def test_function_passes_with_25_minute_study(self, mock_sleep):
        start_countdown(25, "Test Note - Hi")

        mock_sleep.assert_called_once_with(25 * 60)


if __name__ == "__main__":
    unittest.main()