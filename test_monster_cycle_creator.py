from unittest import TestCase
from unittest.mock import patch
import game


class TestMonsterCycleCreator(TestCase):

    @patch('game.LIST_OF_DICTIONARY_MONSTERS_CONSTANT',
           return_value=[
               {"name": "Ellinia Lupin", "desc": "its a monkey... but a zombie",
                 "level": 1, "hp": 10, "dmg": 8, "zones": ["ellinia"]},
                {"name": "Henesys Lupin", "desc": "its a monkey... but a zombie",
                 "level": 1, "hp": 10, "dmg": 8, "zones": ["henesys"]},
                {"name": "Sleepy Wood Lupin", "desc": "its a monkey... but a zombie",
                 "level": 1, "hp": 10, "dmg": 8, "zones": ["sleepy wood"]},
                {"name": "Perion Lupin", "desc": "its a monkey... but a zombie",
                 "level": 1, "hp": 10, "dmg": 8, "zones": ["perion"]},
                {"name": "Kerning Lupin", "desc": "its a monkey... but a zombie",
                 "level": 1, "hp": 10, "dmg": 8, "zones": ["kerning"]},
                {"name": "All region Lupin", "desc": "its a monkey... but a zombie",
                 "level": 1, "hp": 10, "dmg": 8, "zones": ["ellinia", "kerning", "henesys", "sleepy wood", "perion"]}

           ])
    def test_monster_cycle_creator_ellinia(self, mock_list_of_monster_dictionary):
        actual_value = game.monster_cycle_creator()
        expected_key = "ellinia"
        expected_value = [{"name": "Ellinia Lupin", "desc": "its a monkey... but a zombie",
                           "level": 1, "hp": 10, "dmg": 8, "zones": ["ellinia"]},
                          {"name": "All region Lupin", "desc": "its a monkey... but a zombie",
                           "level": 1, "hp": 10, "dmg": 8,
                           "zones": ["ellinia", "kerning", "henesys", "sleepy wood", "perion"]}
                          ]
        self.assertTrue(expected_key in actual_value.keys())
        self.assertEqual(expected_value[0], next(actual_value.get(expected_key)))
        self.assertEqual(expected_value[1], next(actual_value.get(expected_key)))


    @patch('game.LIST_OF_DICTIONARY_MONSTERS_CONSTANT',
           return_value=[
               {"name": "Ellinia Lupin", "desc": "its a monkey... but a zombie",
                "level": 1, "hp": 10, "dmg": 8, "zones": ["ellinia"]},
               {"name": "Henesys Lupin", "desc": "its a monkey... but a zombie",
                "level": 1, "hp": 10, "dmg": 8, "zones": ["henesys"]},
               {"name": "Sleepy Wood Lupin", "desc": "its a monkey... but a zombie",
                "level": 1, "hp": 10, "dmg": 8, "zones": ["sleepy wood"]},
               {"name": "Perion Lupin", "desc": "its a monkey... but a zombie",
                "level": 1, "hp": 10, "dmg": 8, "zones": ["perion"]},
               {"name": "Kerning Lupin", "desc": "its a monkey... but a zombie",
                "level": 1, "hp": 10, "dmg": 8, "zones": ["kerning"]},
               {"name": "All region Lupin", "desc": "its a monkey... but a zombie",
                "level": 1, "hp": 10, "dmg": 8, "zones": ["ellinia", "kerning", "henesys", "sleepy wood", "perion"]}

           ])
    def test_monster_cycle_creator_perion(self, mock_list_of_monster_dictionary):
        actual_value = game.monster_cycle_creator()
        expected_key = "perion"
        expected_value = [{"name": "Perion Lupin", "desc": "its a monkey... but a zombie",
                           "level": 1, "hp": 10, "dmg": 8, "zones": ["perion"]},
                          {"name": "All region Lupin", "desc": "its a monkey... but a zombie",
                           "level": 1, "hp": 10, "dmg": 8,
                           "zones": ["ellinia", "kerning", "henesys", "sleepy wood", "perion"]}
                          ]
        self.assertTrue(expected_key in actual_value.keys())
        self.assertEqual(expected_value[0], next(actual_value.get(expected_key)))
        self.assertEqual(expected_value[1], next(actual_value.get(expected_key)))

    @patch('game.LIST_OF_DICTIONARY_MONSTERS_CONSTANT',
           return_value=[
               {"name": "Ellinia Lupin", "desc": "its a monkey... but a zombie",
                "level": 1, "hp": 10, "dmg": 8, "zones": ["ellinia"]},
               {"name": "Henesys Lupin", "desc": "its a monkey... but a zombie",
                "level": 1, "hp": 10, "dmg": 8, "zones": ["henesys"]},
               {"name": "Sleepy Wood Lupin", "desc": "its a monkey... but a zombie",
                "level": 1, "hp": 10, "dmg": 8, "zones": ["sleepy wood"]},
               {"name": "Perion Lupin", "desc": "its a monkey... but a zombie",
                "level": 1, "hp": 10, "dmg": 8, "zones": ["perion"]},
               {"name": "Kerning Lupin", "desc": "its a monkey... but a zombie",
                "level": 1, "hp": 10, "dmg": 8, "zones": ["kerning"]},
               {"name": "All region Lupin", "desc": "its a monkey... but a zombie",
                "level": 1, "hp": 10, "dmg": 8, "zones": ["ellinia", "kerning", "henesys", "sleepy wood", "perion"]}

           ])
    def test_monster_cycle_creator_henesys(self, mock_list_of_monster_dictionary):
        actual_value = game.monster_cycle_creator()
        expected_key = "henesys"
        expected_value = [{"name": "Henesys Lupin", "desc": "its a monkey... but a zombie",
                           "level": 1, "hp": 10, "dmg": 8, "zones": ["henesys"]},
                          {"name": "All region Lupin", "desc": "its a monkey... but a zombie",
                           "level": 1, "hp": 10, "dmg": 8,
                           "zones": ["ellinia", "kerning", "henesys", "sleepy wood", "perion"]}
                          ]
        self.assertTrue(expected_key in actual_value.keys())
        self.assertEqual(expected_value[0], next(actual_value.get(expected_key)))
        self.assertEqual(expected_value[1], next(actual_value.get(expected_key)))

    @patch('game.LIST_OF_DICTIONARY_MONSTERS_CONSTANT',
           return_value=[
               {"name": "Ellinia Lupin", "desc": "its a monkey... but a zombie",
                "level": 1, "hp": 10, "dmg": 8, "zones": ["ellinia"]},
               {"name": "Henesys Lupin", "desc": "its a monkey... but a zombie",
                "level": 1, "hp": 10, "dmg": 8, "zones": ["henesys"]},
               {"name": "Sleepy Wood Lupin", "desc": "its a monkey... but a zombie",
                "level": 1, "hp": 10, "dmg": 8, "zones": ["sleepy wood"]},
               {"name": "Perion Lupin", "desc": "its a monkey... but a zombie",
                "level": 1, "hp": 10, "dmg": 8, "zones": ["perion"]},
               {"name": "Kerning Lupin", "desc": "its a monkey... but a zombie",
                "level": 1, "hp": 10, "dmg": 8, "zones": ["kerning"]},
               {"name": "All region Lupin", "desc": "its a monkey... but a zombie",
                "level": 1, "hp": 10, "dmg": 8,
                "zones": ["ellinia", "kerning", "henesys", "sleepy wood", "perion"]}

           ])
    def test_monster_cycle_creator_sleepy(self, mock_list_of_monster_dictionary):
        actual_value = game.monster_cycle_creator()
        expected_key = "sleepy wood"
        expected_value = [{"name": "Sleepy Wood Lupin", "desc": "its a monkey... but a zombie",
                           "level": 1, "hp": 10, "dmg": 8, "zones": ["sleepy wood"]},
                          {"name": "All region Lupin", "desc": "its a monkey... but a zombie",
                           "level": 1, "hp": 10, "dmg": 8,
                           "zones": ["ellinia", "kerning", "henesys", "sleepy wood", "perion"]}
                          ]
        self.assertTrue(expected_key in actual_value.keys())
        self.assertEqual(expected_value[0], next(actual_value.get(expected_key)))
        self.assertEqual(expected_value[1], next(actual_value.get(expected_key)))

    @patch('game.LIST_OF_DICTIONARY_MONSTERS_CONSTANT',
           return_value=[
               {"name": "Ellinia Lupin", "desc": "its a monkey... but a zombie",
                "level": 1, "hp": 10, "dmg": 8, "zones": ["ellinia"]},
               {"name": "Henesys Lupin", "desc": "its a monkey... but a zombie",
                "level": 1, "hp": 10, "dmg": 8, "zones": ["henesys"]},
               {"name": "Sleepy Wood Lupin", "desc": "its a monkey... but a zombie",
                "level": 1, "hp": 10, "dmg": 8, "zones": ["sleepy wood"]},
               {"name": "Perion Lupin", "desc": "its a monkey... but a zombie",
                "level": 1, "hp": 10, "dmg": 8, "zones": ["perion"]},
               {"name": "Kerning Lupin", "desc": "its a monkey... but a zombie",
                "level": 1, "hp": 10, "dmg": 8, "zones": ["kerning"]},
               {"name": "All region Lupin", "desc": "its a monkey... but a zombie",
                "level": 1, "hp": 10, "dmg": 8,
                "zones": ["ellinia", "kerning", "henesys", "sleepy wood", "perion"]}

           ])
    def test_monster_cycle_creator_kerning(self, mock_list_of_monster_dictionary):
        actual_value = game.monster_cycle_creator()
        expected_key = "kerning"
        expected_value = [{"name": "Kerning Lupin", "desc": "its a monkey... but a zombie",
                           "level": 1, "hp": 10, "dmg": 8, "zones": ["kerning"]},
                          {"name": "All region Lupin", "desc": "its a monkey... but a zombie",
                           "level": 1, "hp": 10, "dmg": 8,
                           "zones": ["ellinia", "kerning", "henesys", "sleepy wood", "perion"]}
                          ]
        self.assertTrue(expected_key in actual_value.keys())
        self.assertEqual(expected_value[0], next(actual_value.get(expected_key)))
        self.assertEqual(expected_value[1], next(actual_value.get(expected_key)))


