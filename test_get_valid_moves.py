from unittest import TestCase
from game import get_valid_moves


class Test(TestCase):
    def test_get_valid_moves_top_left(self):
        position = [0, 0]
        expected_output = ['South', 'East']
        actual = get_valid_moves(position)
        self.assertEqual(expected_output, actual)

    def test_get_valid_moves_top_right(self):
        position = [0, 25]
        expected_output = ['South', 'West']
        actual = get_valid_moves(position)
        self.assertEqual(expected_output, actual)

    def test_get_valid_moves_bottom_left(self):
        position = [25, 0]
        expected_output = ['North', 'East']
        actual = get_valid_moves(position)
        self.assertEqual(expected_output, actual)

    def test_get_valid_moves_bottom_right(self):
        position = [25, 25]
        expected_output = ['North', 'West']
        actual = get_valid_moves(position)
        self.assertEqual(expected_output, actual)

    def test_get_valid_moves_middle(self):
        position = [12, 12]
        expected_output = ['North', 'South', 'West', 'East']
        actual = get_valid_moves(position)
        self.assertEqual(expected_output, actual)

