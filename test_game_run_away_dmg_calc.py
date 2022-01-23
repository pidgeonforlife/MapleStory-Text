from unittest import TestCase
from unittest.mock import patch
import io
import game


class TestRunAwayDmgCalc(TestCase):
    @patch('random.randint', return_value=3)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_run_away_dmg_calc_correct_print(self, mock_output, mock_randint):
        test_monster = {"name": "Snail", "desc": "its a snail ... yeah ", "level": 1, "hp": 15, "dmg": 2,
                        "zones": ["ellinia", "henesys", "kerning", "perion"], "exp": 100}
        test_player = {"name": "Eric", "dmg": 10, "class": "magician", "hp": 20, "level": {"level": 1, "exp": 100}}
        game.run_away_dmg_calc(test_player, test_monster)
        actual_print = mock_output.getvalue()
        expected_print = f"You tried to running away but the {test_monster['name']} was too fast for you.\nYou took a" \
                         f" total of {3} damage and now have {test_player['hp']} hp left\n"
        self.assertEqual(expected_print, actual_print)

    @patch('random.randint', return_value=3)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_run_away_dmg_calc_correct_hp_update(self, mock_output, mock_randint):
        test_monster = {"name": "Snail", "desc": "its a snail ... yeah ", "level": 1, "hp": 15, "dmg": 2,
                        "zones": ["ellinia", "henesys", "kerning", "perion"], "exp": 100}
        test_player = {"name": "Eric", "dmg": 10, "class": "magician", "hp": 20, "level": {"level": 1, "exp": 100}}
        game.run_away_dmg_calc(test_player, test_monster)
        self.assertTrue(test_player['hp'] == 17)