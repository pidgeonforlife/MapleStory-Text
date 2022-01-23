from unittest import TestCase
from unittest.mock import patch
import game


class TestUpgradeCharacter(TestCase):

    def test_upgrade_character_second_tier_dmg(self):
        test_character = {"class": "magician", "dmg": 10, "max_hp": 20, "level":{"level": 1, "exp": 300}}
        tier = "second"
        game.upgrade_character(test_character, tier)
        self.assertEqual(game.get_class("magician")["class_tier"][tier]["dmg"], test_character["dmg"])

    def test_upgrade_character_second_tier_hp(self):
        test_character = {"class": "magician", "dmg": 10, "maxP_hp": 20, "level":{"level": 1, "exp": 300}}
        tier = "second"
        game.upgrade_character(test_character, tier)
        self.assertEqual(game.get_class("magician")["class_tier"][tier]["hp"], test_character["max_hp"])

