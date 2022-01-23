from unittest import TestCase
from unittest.mock import patch
import game
import io


class TestCombat(TestCase):
    @patch('game.heal', side_effect=[''])
    @patch('game.encountered', return_value=False)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_no_enemies(self, mock_output, mock_encountered, mock_heal):
        test_character = {"hp": 20, "max_hp": 30, "position": [0, 0]}
        game.combat(test_character, game.monster_cycle_creator())
        actual_value = mock_output.getvalue()
        expected = f"There seems to be no monsters in the room, poggies!\n"
        self.assertEqual(expected, actual_value)


