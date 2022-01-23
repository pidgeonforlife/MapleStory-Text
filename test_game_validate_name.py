from unittest import TestCase
from unittest.mock import patch
import io
import game


class TestValidateName(TestCase):

    @patch('builtins.input', return_value="Eric")
    def test_validate_name_valid_input_return(self, mock_input):
        actual_value = game.validate_name()
        expected = "Eric"
        self.assertEqual(actual_value, expected)

    @patch('builtins.input', return_value="Eric")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_validate_name_valid_input_print(self, mock_output, mock_input):
        game.validate_name()
        actual_print = mock_output.getvalue()
        expected_print = "What is your name?\n"
        self.assertEqual(actual_print, expected_print)

    @patch('builtins.input', side_effect=["@#@#", "Eric"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_validate_name_wrong_input(self, mock_output, mock_input):
        game.validate_name()
        actual_print = mock_output.getvalue()
        expected_print = "What is your name?\nPlease do not use any strange characters, we don't have the budget for " \
                         "that\nWhat is your name?\n"
        self.assertEqual(actual_print, expected_print)