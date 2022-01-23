from unittest import TestCase
from unittest.mock import patch
import io
import game


class TestValidateInputCombat(TestCase):

    @patch('game.enumerate_list_options', return_value="Fight")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_validate_player_input_combat_first_encounter(self, mock_output, mock_enumerate_list):
        test_monster = {"name": "Snail", "desc": "its a snail ... yeah ", "level": 1, "hp": 15, "dmg": 2,
                        "zones": ["ellinia", "henesys", "kerning", "perion"], "exp": 100}
        test_player = {"name": "Eric", "dmg": 10, "class": "magician", "hp": 20, "level": {"level": 1, "exp": 100}}
        game.validate_player_input_combat(test_player, test_monster, True)
        actual_print = mock_output.getvalue()
        expected_print = f"You encounter a {test_monster['name']}: {test_monster['desc']}, will you fight or run " \
                         f"away?\n"
        self.assertEqual(expected_print, actual_print)

    @patch('game.enumerate_list_options', return_value="Fight")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_validate_player_input_combat_not_first_encounter(self, mock_output, mock_enumerate_list):
        test_monster = {"name": "Snail", "desc": "its a snail ... yeah ", "level": 1, "hp": 15, "dmg": 2,
                        "zones": ["ellinia", "henesys", "kerning", "perion"], "exp": 100}
        test_player = {"name": "Eric", "dmg": 10, "class": "magician", "hp": 20, "level": {"level": 1, "exp": 100}}
        game.validate_player_input_combat(test_player, test_monster, False)
        actual_print = mock_output.getvalue()
        expected_print = f"You have {test_player['hp']} health points.\n"\
                         f"{test_monster['name']} has {test_monster['hp']} health points left.\n"\
                         f"Will you continue to fight?\n"
        self.assertEqual(expected_print, actual_print)

    @patch('game.enumerate_list_options', return_value="Fight")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_validate_player_input_combat_fight(self, mock_output, mock_enumerate_list):
        test_monster = {"name": "Snail", "desc": "its a snail ... yeah ", "level": 1, "hp": 15, "dmg": 2,
                        "zones": ["ellinia", "henesys", "kerning", "perion"], "exp": 100}
        test_player = {"name": "Eric", "dmg": 10, "class": "magician", "hp": 20, "level": {"level": 1, "exp": 100}}
        actual = game.validate_player_input_combat(test_player, test_monster, True)
        expected = "Fight"
        self.assertEqual(expected, actual)

    @patch('game.enumerate_list_options', return_value="Run away")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_validate_player_input_combat_run(self, mock_output, mock_enumerate_list):
        test_monster = {"name": "Snail", "desc": "its a snail ... yeah ", "level": 1, "hp": 15, "dmg": 2,
                        "zones": ["ellinia", "henesys", "kerning", "perion"], "exp": 100}
        test_player = {"name": "Eric", "dmg": 10, "class": "magician", "hp": 20, "level": {"level": 1, "exp": 100}}
        actual = game.validate_player_input_combat(test_player, test_monster, True)
        expected = "Run away"
        self.assertEqual(expected, actual)