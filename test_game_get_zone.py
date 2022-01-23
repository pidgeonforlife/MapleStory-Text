from unittest import TestCase
import game


class TestGetZone(TestCase):

    def test_get_zone_kerning(self):
        player_coords = [1, 1]
        actual_value = game.get_zone(player_coords)
        expected_value = "kerning"
        self.assertEqual(actual_value, expected_value)

    def test_get_zone_perion(self):
        player_coords = [11, 23]
        actual_value = game.get_zone(player_coords)
        expected_value = "perion"
        self.assertEqual(actual_value, expected_value)

    def test_get_zone_ellinia(self):
        player_coords = [23, 23]
        actual_value = game.get_zone(player_coords)
        expected_value = "ellinia"
        self.assertEqual(actual_value, expected_value)

    def test_get_zone_sleepywood(self):
        player_coords = [11, 11]
        actual_value = game.get_zone(player_coords)
        expected_value = "sleepy wood"
        self.assertEqual(actual_value, expected_value)

    def test_get_zone_henesys(self):
        player_coords = [15, 6]
        actual_value = game.get_zone(player_coords)
        expected_value = "henesys"
        self.assertEqual(actual_value, expected_value)

