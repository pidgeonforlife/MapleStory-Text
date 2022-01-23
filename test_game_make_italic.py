from unittest import TestCase
import game


class TestMakeItalic(TestCase):
    def test_make_italic(self):
        expected_value = f"\x1B[3mHello\x1B[23m"
        actual_value = game.make_italic("Hello")
        self.assertEqual(actual_value, expected_value)
