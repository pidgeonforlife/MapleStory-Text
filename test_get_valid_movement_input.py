from unittest import TestCase
from unittest.mock import patch
import game


class TestGetValidMovement(TestCase):
    @patch('game.get_valid_moves', return_value=["North", "South"])
    @patch('game.enumerate_list_options', return_value="North")
    def test_get_valid_movement_input(self, mock_enumerate, mock_valid_moves):
        actual = game.get_valid_movement_input({"position": [0, 0]})
        self.assertEqual(actual, "North")
