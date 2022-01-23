from unittest import TestCase
from unittest.mock import patch
import io
import game


class TestGiveExp(TestCase):

    @patch('game.upgrade_character', side_effect=[""])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_give_exp_level_one(self, mock_output, mock_upgrade_character):
        test_character = {"level": {"level": 1, "exp": 0}, "class": "warrior"}
        test_monster = {"level": 1}
        game.give_exp(test_character, test_monster)
        actual_print = mock_output.getvalue()
        self.assertEqual(test_character["level"]["exp"], 100)
        self.assertEqual(actual_print, "You have gained 100 exp\n")

    @patch('game.upgrade_character', side_effect=[""])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_give_exp_level_two(self, mock_output, mock_upgrade_character):
        test_character = {"level": {"level": 1, "exp": 0}, "class": "warrior"}
        test_monster = {"level": 2}
        game.give_exp(test_character, test_monster)
        actual_print = mock_output.getvalue()
        self.assertEqual(test_character["level"]["exp"], 150)
        self.assertEqual(actual_print, "You have gained 150 exp\n")

    @patch('game.upgrade_character', side_effect=[""])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_give_exp_level_three(self, mock_output, mock_upgrade_character):
        test_character = {"level": {"level": 1, "exp": 0}, "class": "warrior"}
        test_monster = {"level": 3}
        game.give_exp(test_character, test_monster)
        actual_print = mock_output.getvalue()
        self.assertEqual(test_character["level"]["exp"], 200)
        self.assertEqual(actual_print, "You have gained 200 exp\n")