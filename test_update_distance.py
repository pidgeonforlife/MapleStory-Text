from unittest import TestCase
from unittest.mock import patch
import game


class TestUpdateDistance(TestCase):

    def test_update_distance(self):
        test_player = {"position": [3, 3], "distance_goal": [10, 10]}
        game.update_distance(test_player)
        expected = [0, 0]
        self.assertTrue(test_player["distance_goal"][0] - 11.313, 0.01)

    def test_update_distance_correct_value_shift(self):
        test_player = {"position": [3, 3], "distance_goal": [3, 4]}
        game.update_distance(test_player)
        expected = [0, 0]
        self.assertEqual(test_player["distance_goal"][1], 3)
