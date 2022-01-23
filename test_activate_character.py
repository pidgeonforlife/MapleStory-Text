from unittest import TestCase
from game import activate_character


class TestActivateCharacter(TestCase):

    def test_activate_character(self):
        test_dictionary = {'active': False}
        activate_character(test_dictionary)
        self.assertTrue(test_dictionary.get('active'))
