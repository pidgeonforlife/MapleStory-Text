from unittest import TestCase
from unittest.mock import patch
import game


class TestRollDice(TestCase):

    @patch('random.randint', side_effect=[1, 2, 3])
    def test_roll_dice_one_roll(self, mock_randint):
        actual_value = game.roll_dice(1, 10)
        self.assertEqual(actual_value, 1)

    @patch('random.randint', side_effect=[1, 2, 3])
    def test_roll_dice_multiple_roll(self, mock_randint):
        actual_value = game.roll_dice(3, 10)
        self.assertEqual(actual_value, 6)

    @patch('random.randint', side_effect=[1, 2, 3])
    def test_roll_dice_no_roll(self, mock_randint):
        actual_value = game.roll_dice(0, 10)
        self.assertEqual(actual_value, 0)
