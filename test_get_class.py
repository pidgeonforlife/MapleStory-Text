from unittest import TestCase
from game import get_class, LIST_OF_CLASSES


class TestGetClass(TestCase):
    def test_get_class_magician(self):
        actual = get_class("magician")
        expected = {"name": "magician",
                    "class_tier": {"first": {"name": "Magician",
                                             "exp": 0,
                                             "hp": 10,
                                             "dmg": 15,
                                             "dodge": 0,
                                             "dmg_reduc": 5
                                             },
                                   "second": {"name": "Wizard",
                                              "exp": 200,
                                              "hp": 20,
                                              "dmg": 25,
                                              "dodge": 0.02,
                                              "dmg_reduc": 10,
                                              "attacks": ["uses Ice Strike to create an Ice explosion!",
                                                          "uses Explosion to create a Fire explosion!"]

                                              },
                                   "third": {"name": "Arch Magician",
                                             "exp": 600,
                                             "hp": 30,
                                             "dmg": 35,
                                             "dodge": 0.05,
                                             "dmg_reduc": 20,
                                             "attacks": [
                                                 "uses Blizzard! You summon a freezing artic wind to freeze your "
                                                 "enemy!",
                                                 "uses Meteor Shower! You summon meteorites from the sky to rain "
                                                 "down on the enemy"]

                                             }},
                    "attack_lines": ["uses Magic Claw! You cast magical energy to scratch the enemy.",
                                     "whacks the enemy with a staff!",
                                     "uses Magic Ball to his the enemy with energy"]}
        self.assertEqual(actual, expected)

    def test_get_class_thief(self):
        actual = get_class("thief")
        expected = {"name": "thief",
                    "class_tier": {"first": {"name": "Assassin",
                                             "exp": 0,
                                             "hp": 15,
                                             "dmg": 15,
                                             "dodge": 0.20,
                                             "dmg_reduc": 0
                                             },
                                   "second": {"name": "Hermit",
                                              "exp": 200,
                                              "hp": 30,
                                              "dmg": 25,
                                              "dodge": 0.50,
                                              "dmg_reduc": 10,
                                              "attacks": ["uses Shuriken Burst to throw exploding stars at the enemy!",
                                                          "uses Gust Charm to blow the enemy back!"]

                                              },
                                   "third": {"name": "Night Lord",
                                             "exp": 600,
                                             "hp": 50,
                                             "dmg": 35,
                                             "dodge": 0.80,
                                             "dmg_reduc": 0,
                                             "attacks": ["uses Triple Throw! You throw 3 stars simultaneously",
                                                         "uses Dark Flare! You summon the Dark Lord's throwing star "
                                                         "and hurl it at the enemy"]

                                             }},
                    "attack_lines": ["throws ninja stars at the enemy!",
                                     "punches the enemy."]}
        self.assertEqual(actual, expected)

    def test_get_class_beginner(self):
        actual = get_class("beginner")
        expected = {"name": "beginner",
                    "class_tier": {"first": {"name": "Beginner",
                                             "exp": 0,
                                             "hp": 20,
                                             "dmg": 10,
                                             "dodge": 0,
                                             "dmg_reduc": 0
                                             },
                                   "second": {"name": "Beginner",
                                              "exp": 200,
                                              "hp": 20,
                                              "dmg": 25,
                                              "dodge": 0,
                                              "dmg_reduc": 0,
                                              "attacks": ["threw a red snail shell!",
                                                          "threw a blue snail shell!",
                                                          "threw a snail shell!"]
                                              },
                                   "third": {"name": "Beginner",
                                             "exp": 2000,
                                             "hp": 1000,
                                             "dmg": 500,
                                             "dodge": 1.00,
                                             "dmg_reduc": 0,
                                             "attacks": ["threw a red snail shell!",
                                                         "threw a blue snail shell!",
                                                         "threw a snail shell!"]
                                             }},
                    "attack_lines": ["threw a red snail shell!",
                                     "threw a blue snail shell!",
                                     "threw a snail shell!"]}
        self.assertEqual(actual, expected)
