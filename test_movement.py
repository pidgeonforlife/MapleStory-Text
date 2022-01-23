from unittest import TestCase
from unittest.mock import patch
import game
import io


class TestMovement(TestCase):

    @patch('game.get_valid_movement_input', return_value='North')
    def test_movement_north(self, mock_input):
        test_player = {"position": [3, 3], "distance_goal": [10, 10]}
        game.movement(test_player)
        self.assertEqual(test_player["position"], [2, 3])

    @patch('game.get_valid_movement_input', return_value='South')
    def test_movement_south(self, mock_input):
        test_player = {"position": [3, 3], "distance_goal": [10, 10]}
        game.movement(test_player)
        self.assertEqual(test_player["position"], [4, 3])

    @patch('game.get_valid_movement_input', return_value='West')
    def test_movement_west(self, mock_input):
        test_player = {"position": [3, 3], "distance_goal": [10, 10]}
        game.movement(test_player)
        self.assertEqual(test_player["position"], [3, 2])

    @patch('game.get_valid_movement_input', return_value='East')
    def test_movement_east(self, mock_input):
        test_player = {"position": [3, 3], "distance_goal": [10, 10]}
        game.movement(test_player)
        self.assertEqual(test_player["position"], [3, 4])
