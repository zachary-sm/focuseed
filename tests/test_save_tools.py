import unittest
from pathlib import Path
from datetime import datetime, timedelta
from utils.save_tools import count_saved_hours, save_session


class TestSaveTools(unittest.TestCase):
    def test_saving(self):
        result = count_saved_hours(Path("tests/test_data/test_save_tools_data.json"))
        self.assertEqual(result, timedelta(hours=42, minutes=20))


if __name__ == "__main__":
    unittest.main()