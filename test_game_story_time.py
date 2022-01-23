from unittest import TestCase
from unittest.mock import patch
import io
import game


class TestStoryTime(TestCase):

    @patch('game.STORY_LINES_CONSTANT', return_value={"kerning": ["You see the abandoned sky scrapers of Kerning City "
                                                                  "in the distance."]})
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_story_time(self, mock_output, mock_story_lines):
        test_character = {"distance_goal": [10, 1], "position": [0, 0], "active": True}
        game.story_time(test_character)
        actual = mock_output.getvalue()
        expected_value = "You see the abandoned sky scrapers of Kerning City in the distance.\nI feel the power " \
                         "drawing me get weaker\n"
        self.assertEqual(expected_value, actual)

    @patch('game.STORY_LINES_CONSTANT', return_value={"kerning": ["You see the abandoned sky scrapers of Kerning City "
                                                                  "in the distance."]})
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_story_time_same_distance(self, mock_output, mock_story_lines):
        test_character = {"distance_goal": [1, 1], "position": [0, 0], "active": True}
        game.story_time(test_character)
        actual = mock_output.getvalue()
        expected_value = "You see the abandoned sky scrapers of Kerning City in the distance.\nThe aura feels the " \
                         "same.\n"
        self.assertEqual(expected_value, actual)

    @patch('game.STORY_LINES_CONSTANT', return_value={"kerning": ["You see the abandoned sky scrapers of Kerning City "
                                                                  "in the distance."]})
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_story_time_went_further(self, mock_output, mock_story_lines):
        test_character = {"distance_goal": [10, 1], "position": [0, 0], "active": True}
        game.story_time(test_character)
        actual = mock_output.getvalue()
        expected_value = "You see the abandoned sky scrapers of Kerning City in the distance.\nI feel the power " \
                         "drawing me get weaker\n"
        self.assertEqual(expected_value, actual)

    @patch('game.STORY_LINES_CONSTANT', return_value={"kerning": ["You see the abandoned sky scrapers of Kerning City "
                                                                  "in the distance."]})
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_story_time_went_closer(self, mock_output, mock_story_lines):
        test_character = {"distance_goal": [1, 10], "position": [0, 0], "active": True}
        game.story_time(test_character)
        actual = mock_output.getvalue()
        expected_value = "You see the abandoned sky scrapers of Kerning City in the distance.\nThe aura is getting " \
                         "stronger\n"
        self.assertEqual(expected_value, actual)
