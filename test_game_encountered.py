from unittest import TestCase
from unittest.mock import patch
import game


class TestEncountered(TestCase):

    @patch('random.random', return_value=0.1)
    def test_encountered_true(self, mock_random):
        self.assertTrue(game.encountered())

    @patch('random.random', return_value=0.99)
    def test_encountered_false(self, mock_random):
        self.assertFalse(game.encountered())