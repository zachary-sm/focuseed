import unittest
from commands.stats import show_stats

class TestCountdown(unittest.TestCase):
    def test_correct_long_history(self, mock_sleep):
        show_stats()

if __name__ == "__main__":
    unittest.main()