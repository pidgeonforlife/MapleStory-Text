from unittest import TestCase
from unittest.mock import patch
import io
import game


class TestCongrats(TestCase):

    def test_congrats(self):
        test_dictionary = {'level': {'level': 2, "exp": 41}}
        with self.assertRaises(SystemExit) as cm:
            game.congrats(test_dictionary)
        self.assertEqual(cm.exception.code, "See you next time!")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_congrats_correct_print(self, mock_output):
        test_dictionary = {'level': {'level': 2, "exp": 41}}
        with self.assertRaises(SystemExit):
            game.congrats(test_dictionary)
        actual_print = mock_output.getvalue()
        expected = f"congrats you finished the game poggies\nYou finished the game at level "\
                   f"{test_dictionary['level']['level']}\n"
        self.assertEqual(actual_print, expected)
