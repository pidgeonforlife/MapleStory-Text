from unittest import TestCase
from unittest.mock import patch
import io
import game


class TestCreateCharacter(TestCase):

    @patch('game.choose_class', return_value="warrior")
    @patch('game.validate_name', return_value="TestName")
    def test_create_character_auto_fields(self, mock_validate_name, mock_choose_class):
        actual = game.create_character()
        self.assertEqual(game.get_class("warrior")["class_tier"]["first"]["hp"], actual.get("max_hp"))
        self.assertEqual(game.get_class("warrior")["class_tier"]["first"]["hp"], actual.get("hp"))
        self.assertEqual(game.get_class("warrior")["class_tier"]["first"]["dmg"], actual.get("dmg"))
        self.assertEqual([0, 0], actual.get("position"))
        self.assertEqual({"level": 1, "exp": 0}, actual.get("level"))
        self.assertEqual(False, actual.get("active"))

    @patch('game.choose_class', return_value="warrior")
    @patch('game.validate_name', return_value="TestName")
    def test_create_character_user_fields(self, mock_validate_name, mock_choose_class):
        actual = game.create_character()
        self.assertEqual("warrior", actual.get("class"))
        self.assertEqual("TestName", actual.get("name"))
