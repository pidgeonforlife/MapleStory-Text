from unittest import TestCase
from game import calculate_distance_to_goal


class Test(TestCase):
    def test_calculate_distance_to_goal_from_start(self):
        position_array = [0, 0]
        expected_output = 15.556349186104045
        actual = calculate_distance_to_goal(position_array)
        self.assertEqual(expected_output, actual)

    def test_calculate_distance_to_goal_from_whole_number(self):
        position_array = [11, 0]
        expected_output = 11.0
        actual = calculate_distance_to_goal(position_array)
        self.assertEqual(expected_output, actual)

    def test_calculate_distance_to_goal_from_end(self):
        position_array = [11, 11]
        expected_output = 0
        actual = calculate_distance_to_goal(position_array)
        self.assertEqual(expected_output, actual)

