from unittest import TestCase
from unittest.mock import patch
import game
import itertools


class TestGetMonster(TestCase):
    def test_get_monster_level_one(self):
        list_monster_dict_test = {"kerning": itertools.cycle([{"name": "Zombie Lupin 3", "desc": "It's a monkey... "
                                                                                                 "but a zombie",
                                    "level": 3, "hp": 10, "dmg": 8, "zones": ["kerning"], "exp": 100},
                                   {"name": "Zombie Lupin 2", "desc": "It's a monkey... but a zombie",
                                    "level": 2, "hp": 10, "dmg": 8, "zones": ["kerning"], "exp": 100},
                                   {"name": "Zombie Lupin 1", "desc": "It's a monkey... but a zombie",
                                    "level": 1, "hp": 10, "dmg": 8, "zones": ["kerning"], "exp": 100},
                                   ])}
        test_player = {"level": {"level": 1}, "position": [0, 0]}
        actual = game.get_monster(test_player, list_monster_dict_test).get('name')
        expected = "Zombie Lupin 1"
        self.assertEqual(expected, actual)

    def test_get_monster_level_two(self):
        list_monster_dict_test = {"kerning": itertools.cycle([{"name": "Zombie Lupin 3", "desc": "It's a monkey... "
                                                                                                 "but a zombie",
                                    "level": 3, "hp": 10, "dmg": 8, "zones": ["kerning"], "exp": 100},
                                   {"name": "Zombie Lupin 2", "desc": "It's a monkey... but a zombie",
                                    "level": 2, "hp": 10, "dmg": 8, "zones": ["kerning"], "exp": 100},
                                   {"name": "Zombie Lupin 1", "desc": "It's a monkey... but a zombie",
                                    "level": 1, "hp": 10, "dmg": 8, "zones": ["kerning"], "exp": 100},
                                   ])}
        test_player = {"level": {"level": 2}, "position": [0, 0]}
        actual = game.get_monster(test_player, list_monster_dict_test).get('name')
        expected = "Zombie Lupin 2"
        self.assertEqual(expected, actual)

    def test_get_monster_level_three(self):
        list_monster_dict_test = {"kerning": itertools.cycle([{"name": "Zombie Lupin 3", "desc": "It's a monkey... "
                                                                                                 "but a zombie",
                                    "level": 3, "hp": 10, "dmg": 8, "zones": ["kerning"], "exp": 100},
                                   {"name": "Zombie Lupin 2", "desc": "It's a monkey... but a zombie",
                                    "level": 2, "hp": 10, "dmg": 8, "zones": ["kerning"], "exp": 100},
                                   {"name": "Zombie Lupin 1", "desc": "It's a monkey... but a zombie",
                                    "level": 1, "hp": 10, "dmg": 8, "zones": ["kerning"], "exp": 100},
                                   ])}
        test_player = {"level": {"level": 3}, "position": [0, 0]}
        actual = game.get_monster(test_player, list_monster_dict_test).get('name')
        expected = "Zombie Lupin 3"
        self.assertEqual(expected, actual)
