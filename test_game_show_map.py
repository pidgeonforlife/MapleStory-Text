from unittest import TestCase
from unittest.mock import patch
import game
import io


class TestShowMap(TestCase):

    @patch('game.BOSS_POSITION', return_value=(2, 2))
    @patch('game.NUMBER_COL_CONSTANT', return_value=3)
    @patch('game.NUMBER_ROW_CONSTANT', return_value=3)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_map(self, mock_output, mock_number_row, mock_number_col, mock_boss_poss):
        player_cord = [0, 0]
        game.show_map(player_cord)
        actual_print = mock_output.getvalue()
        expected_print = " X   -   - \n -   -   - \n -   -   O \n"
        self.assertEqual(actual_print, expected_print)
