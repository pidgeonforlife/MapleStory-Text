from unittest import TestCase
from unittest.mock import patch
import io
import game


class TestIntro(TestCase):

    @patch('game.create_character', return_value={"name": "Eric"})
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_intro_returns_correct_value(self, mock_output, mock_create_character):
        actual = game.intro()
        expected = {"name": "Eric"}
        self.assertEqual(expected, actual)

    @patch('game.create_character', return_value={"name": "Eric"})
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_intro_returns_correct_print(self, mock_output, mock_create_character):
        game.intro()
        actual = mock_output.getvalue()
        expected = "Hello, this is Victoria Island.\nUnfortunately your family has been brutally murdered by the " \
                   "Crimson Balrog.\nAs you search for the beast you will encounter smaller monsters.\nKill them " \
                   "to become stronger before you face your nemesis.\nAs you move around the aura towards the " \
                   "beast will get stronger or weaker.\n"\
                   "Give up on your quest by using the 'quit' command as well\n"
        self.assertEqual(expected, actual)
