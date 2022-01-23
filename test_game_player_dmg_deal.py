from unittest import TestCase
from unittest.mock import patch
import game
import io


class TestPlayerDmgDeal(TestCase):

    @patch('game.player_dmg_line', return_value="BLA")
    @patch('game.roll_dice', return_value=10)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_player_dmg_deal_print(self, mock_output, mock_roll_dice, mock_player_dmg_line):
        test_monster = {"name": "Snail", "desc": "its a snail ... yeah ", "level": 1, "hp": 15, "dmg": 2,
                        "zones": ["ellinia", "henesys", "kerning", "perion"], "exp": 100}
        test_player = {"name": "Eric", "dmg": 10, "class": "magician", "hp": 20, "level": {"level": 1, "exp": 100}}
        game.player_dmg_deal(test_monster, test_player)
        actual_print = mock_output.getvalue()
        expected = f"{test_player['name']} BLA\nYou dealt 10 to the monster, it has 5 hp left\n"
        self.assertEqual(expected, actual_print)

    @patch('game.player_dmg_line', return_value="BLA")
    @patch('game.roll_dice', return_value=10)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_player_dmg_deal_hp_update(self, mock_output, mock_roll_dice, mock_player_dmg_line):
        test_monster = {"name": "Snail", "desc": "its a snail ... yeah ", "level": 1, "hp": 15, "dmg": 2,
                        "zones": ["ellinia", "henesys", "kerning", "perion"], "exp": 100}
        test_player = {"name": "Eric", "dmg": 10, "class": "magician", "hp": 20, "level": {"level": 1, "exp": 100}}
        game.player_dmg_deal(test_monster, test_player)
        self.assertTrue(test_monster['hp'] < 15)