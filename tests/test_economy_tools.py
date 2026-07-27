import unittest
from unittest.mock import call, patch

from utils.economy_tools import award_progress, change_tree_progress


class TestTreeProgress(unittest.TestCase):
    def test_progress_below_growth_threshold_is_saved(self):
        with (
            patch("utils.economy_tools.get_json_field") as mock_get,
            patch("utils.economy_tools.save_to_json_field") as mock_save,
        ):
            mock_get.side_effect = [10, "oak", {"name": "Oak", "growth_time": 30}]
            change_tree_progress(15)

        mock_save.assert_called_once_with(
            field="tree_progress", item=25, path=unittest.mock.ANY
        )

    def test_completed_tree_resets_progress_and_preserves_inventory(self):
        owned_trees = {"oak": 2, "pine": 1}

        with (
            patch("utils.economy_tools.get_json_field") as mock_get,
            patch("utils.economy_tools.save_to_json_field") as mock_save,
        ):
            mock_get.side_effect = [25, "oak", {"name": "Oak", "growth_time": 30}, owned_trees]
            change_tree_progress(5)

        self.assertEqual(
            mock_save.call_args_list,
            [
                call(field="tree_progress", item=0, path=unittest.mock.ANY),
                call(field="owned_trees", item={"oak": 3, "pine": 1}, path=unittest.mock.ANY),
            ],
        )

    def test_award_progress_awards_currency_and_tree_progress(self):
        with (
            patch("utils.economy_tools.award_growbux") as mock_award_growbux,
            patch("utils.economy_tools.change_tree_progress") as mock_tree_progress,
        ):
            award_progress(12)

        mock_award_growbux.assert_called_once_with(180)
        mock_tree_progress.assert_called_once_with(12)
