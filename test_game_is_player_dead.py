from unittest import TestCase
import game


class TestIsPlayerDead(TestCase):
    def test_is_player_dead_dead_character(self):
        dead_dictionary = {"hp": 0}
        actual_value = game.is_player_dead(dead_dictionary)
        expected_value = True
        self.assertEqual(actual_value, expected_value)

    def test_is_player_dead_alive_character(self):
        dead_dictionary = {"hp": 10}
        actual_value = game.is_player_dead(dead_dictionary)
        expected_value = False
        self.assertEqual(actual_value, expected_value)
