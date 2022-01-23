from unittest import TestCase
from unittest.mock import patch
import io
import game


class TestChooseClass(TestCase):

    @patch('builtins.input', return_value=1)
    def test_choose_class_warrior(self, mock_input):
        actual_value = game.choose_class()
        expected_value = "warrior"
        self.assertEqual(expected_value, actual_value)

    @patch('builtins.input', return_value=2)
    def test_choose_class_mage(self, mock_input):
        actual_value = game.choose_class()
        expected_value = "magician"
        self.assertEqual(expected_value, actual_value)