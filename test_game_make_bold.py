from unittest import TestCase
import game


class TestMakeBold(TestCase):
    def test_make_bold_string(self):
        expected_value = f"\033[1mHello\033[0m"
        actual_value = game.make_bold("Hello")
        self.assertEquals(actual_value, expected_value)
