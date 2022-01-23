from unittest import TestCase
from unittest.mock import patch
import game
import io


class TestHeal(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_heal_print_full_heal(self, mock_output):
        test_player = {"name": "Eric", "dmg": 10, "class": "magician",
                       "hp": 20, "max_hp":30, "level": {"level": 1, "exp": 100}}
        game.heal(test_player)
        actual_value = mock_output.getvalue()
        expected = f"You have healed 4, you now have 24 hp!\n"
        self.assertEqual(expected, actual_value)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_heal_print_part_heal(self, mock_output):
        test_player = {"name": "Eric", "dmg": 10, "class": "magician",
                       "hp": 20, "max_hp": 22, "level": {"level": 1, "exp": 100}}
        game.heal(test_player)
        actual_value = mock_output.getvalue()
        expected = f"You have healed 2, you now have 22 hp!\n"
        self.assertEqual(expected, actual_value)
