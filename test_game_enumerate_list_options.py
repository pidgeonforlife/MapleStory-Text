from unittest import TestCase
from unittest.mock import patch
import io
import game


class TestEnumerateListOptions(TestCase):

    @patch('builtins.input', side_effect=[1])
    def test_enumerate_list_options_picks_option(self, mock_input):
        test_list_choices = ["north", "south", "east", "west"]
        actual_value = game.enumerate_list_options(test_list_choices)
        expected_value = test_list_choices[0]
        self.assertEqual(actual_value, expected_value)

    @patch('builtins.input', side_effect=[3])
    def test_enumerate_list_options_picks_option_third(self, mock_input):
        test_list_choices = ["north", "south", "east", "west"]
        actual_value = game.enumerate_list_options(test_list_choices)
        expected_value = test_list_choices[2]
        self.assertEqual(actual_value, expected_value)

    @patch('builtins.input', side_effect=[10, 2])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enumerate_list_options_correct_prints(self, mock_output, mock_input):
        test_list_choices = ["north", "south"]
        game.enumerate_list_options(test_list_choices)
        actual_value = mock_output.getvalue()
        expected_output = "Pick an option!\n1.  north\n2.  south\nPlease pick a valid number from below :/\nPick an " \
                          "option!\n1.  north\n2.  south\n"
        self.assertEqual(actual_value, expected_output)