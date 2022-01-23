from unittest import TestCase
from unittest.mock import patch
import game


class TestCobmatInitiativeRoll(TestCase):

    @patch('game.roll_dice', side_effect=[1, 10])
    def test_combat_initiative_roll_monster_first(self, mock_dice_roll):
        actual = game.combat_initiative_roll()
        expected = "monster"
        self.assertEqual(expected, actual)

    @patch('game.roll_dice', side_effect=[10, 1])
    def test_combat_initiative_roll_player_first(self, mock_dice_roll):
        actual = game.combat_initiative_roll()
        expected = "player"
        self.assertEqual(expected, actual)

    @patch('game.roll_dice', side_effect=[5, 5, 1, 3])
    def test_combat_initiative_roll_tie(self, mock_dice_roll):
        actual = game.combat_initiative_roll()
        expected = None
        self.assertEqual(expected, actual)
