from unittest import TestCase
from unittest.mock import patch
import game


class TestPlayerDmgLine(TestCase):

    def test_player_dmg_line_low_dmg_mage(self):
        test_character = {"class": "magician",
                          "level": {"level": 3}}
        expected_value = game.get_class("magician")["attack_lines"]
        actual_value = game.player_dmg_line(test_character, 1)
        self.assertTrue(actual_value in expected_value)

    def test_player_dmg_line_high_dmg_two_mage(self):
        test_character = {"class": "magician",
                          "level": {"level": 2}}
        expected_value = game.get_class("magician")["class_tier"]["second"]["attacks"]
        actual_value = game.player_dmg_line(test_character, 10000)
        self.assertTrue(actual_value in expected_value)

    def test_player_dmg_line_high_dmg_three_mage(self):
        test_character = {"class": "magician",
                          "level": {"level": 3}}
        expected_value = game.get_class("magician")["class_tier"]["third"]["attacks"]
        actual_value = game.player_dmg_line(test_character, 10000)
        self.assertTrue(actual_value in expected_value)

    def test_player_dmg_line_low_dmg_thief(self):
        test_character = {"class": "thief",
                          "level": {"level": 3}}
        expected_value = game.get_class("thief")["attack_lines"]
        actual_value = game.player_dmg_line(test_character, 1)
        self.assertTrue(actual_value in expected_value)

    def test_player_dmg_line_high_dmg_two_thief(self):
        test_character = {"class": "thief",
                          "level": {"level": 2}}
        expected_value = game.get_class("thief")["class_tier"]["second"]["attacks"]
        actual_value = game.player_dmg_line(test_character, 10000)
        self.assertTrue(actual_value in expected_value)

    def test_player_dmg_line_high_dmg_three_thief(self):
        test_character = {"class": "thief",
                          "level": {"level": 3}}
        expected_value = game.get_class("thief")["class_tier"]["third"]["attacks"]
        actual_value = game.player_dmg_line(test_character, 10000)
        self.assertTrue(actual_value in expected_value)

    def test_player_dmg_line_low_dmg_warrior(self):
        test_character = {"class": "warrior",
                          "level": {"level": 3}}
        expected_value = game.get_class("warrior")["attack_lines"]
        actual_value = game.player_dmg_line(test_character, 1)
        self.assertTrue(actual_value in expected_value)

    def test_player_dmg_line_high_dmg_two_warrior(self):
        test_character = {"class": "warrior",
                          "level": {"level": 2}}
        expected_value = game.get_class("warrior")["class_tier"]["second"]["attacks"]
        actual_value = game.player_dmg_line(test_character, 10000)
        self.assertTrue(actual_value in expected_value)

    def test_player_dmg_line_high_dmg_three_warrior(self):
        test_character = {"class": "warrior",
                          "level": {"level": 3}}
        expected_value = game.get_class("warrior")["class_tier"]["third"]["attacks"]
        actual_value = game.player_dmg_line(test_character, 10000)
        self.assertTrue(actual_value in expected_value)

    def test_player_dmg_line_low_dmg_beginner(self):
        test_character = {"class": "beginner",
                          "level": {"level": 3}}
        expected_value = game.get_class("beginner")["attack_lines"]
        actual_value = game.player_dmg_line(test_character, 1)
        self.assertTrue(actual_value in expected_value)

    def test_player_dmg_line_high_dmg_two_beginner(self):
        test_character = {"class": "beginner",
                          "level": {"level": 2}}
        expected_value = game.get_class("beginner")["class_tier"]["second"]["attacks"]
        actual_value = game.player_dmg_line(test_character, 10000)
        self.assertTrue(actual_value in expected_value)

    def test_player_dmg_line_high_dmg_three_beginner(self):
        test_character = {"class": "beginner",
                          "level": {"level": 3}}
        expected_value = game.get_class("beginner")["class_tier"]["third"]["attacks"]
        actual_value = game.player_dmg_line(test_character, 10000)
        self.assertTrue(actual_value in expected_value)