from unittest import TestCase
from unittest.mock import patch
import game
import io


class TestMonsterDmgDeal(TestCase):

    @patch('random.random', return_value=-11111)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_monster_dmg_deal_dodged(self, mock_output, mock_random):
        test_monster = {"name": "Snail", "desc": "its a snail ... yeah ", "level": 1, "hp": 15, "dmg": 2,
                        "zones": ["ellinia", "henesys", "kerning", "perion"], "exp": 100}
        test_player = {"class": "magician", "hp": 20, "level": {"level": 1, "exp": 100}}
        game.monster_dmg_deal(test_monster, test_player)
        actual_print = mock_output.getvalue()
        expected = f"You avoided the {test_monster['name']}'s attack!\n"
        self.assertEqual(expected, actual_print)

    @patch('random.random', return_value=100000)
    @patch('game.roll_dice', side_effect=[5, 10])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_monster_dmg_deal_not_dodge_print(self, mock_output, mock_roll_dice, mock_random):
        test_monster = {"name": "Snail", "desc": "its a snail ... yeah ", "level": 1, "hp": 15, "dmg": 2,
                        "zones": ["ellinia", "henesys", "kerning", "perion"], "exp": 100}
        test_player = {"class": "magician", "hp": 20, "level": {"level": 1, "exp": 100}}
        game.monster_dmg_deal(test_monster, test_player)
        actual_print = mock_output.getvalue()
        expected = f"You blocked 5 of damage!\n" + f"The {test_monster['name']} deals 5 to you with one swipe, you" \
                   + f" have {test_player['hp']} hp left\n"
        self.assertEqual(expected, actual_print)

    @patch('random.random', return_value=100000)
    @patch('game.roll_dice', side_effect=[5, 10])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_monster_dmg_deal_not_dodged_hp_update(self, mock_output, mock_roll_dice, mock_random):
        test_monster = {"name": "Snail", "desc": "its a snail ... yeah ", "level": 1, "hp": 15, "dmg": 2,
                        "zones": ["ellinia", "henesys", "kerning", "perion"], "exp": 100}
        test_player = {"class": "magician", "hp": 20, "level": {"level": 1, "exp": 100}}
        game.monster_dmg_deal(test_monster, test_player)
        self.assertTrue(test_player['hp'] < 20)
