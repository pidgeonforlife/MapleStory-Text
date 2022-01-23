from unittest import TestCase
from unittest.mock import patch
import game
import io


class TestPlayerDied(TestCase):
    def test_player_died_exit_happened(self):
        with self.assertRaises(SystemExit) as cm:
            game.player_died()
        self.assertEqual(cm.exception.code, "Thanks for playing")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_player_died_correct_print(self, mock_output):
        with self.assertRaises(SystemExit):
            game.player_died()
        actual_print = mock_output.getvalue()
        expected = "Overconfidence is a slow and insidious killer ..\nAs you slowly bleed out, you look back at the " \
                   "death of your family ..\nFilled with regret our hero could not get his revenge ..\n" \
                   "You have died ..\n"
        self.assertEqual(actual_print, expected)