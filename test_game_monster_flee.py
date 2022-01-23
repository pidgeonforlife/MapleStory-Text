from unittest import TestCase
from unittest.mock import patch
import io
import game


class TestMonsterFlee(TestCase):

    @patch('random.random', return_value=0)
    def test_monster_flee_did_run_return(self, mock_random):
        test_monster = {"name": "test monster"}
        actual = game.monster_flee(test_monster)
        self.assertTrue(actual)

    @patch('random.random', return_value=0)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_monster_flee_did_run_return_correct_print(self, mock_output, mock_random):
        test_monster = {"name": "test monster"}
        game.monster_flee(test_monster)
        actual = mock_output.getvalue()
        expected = f"{test_monster['name']} ran away!\n"
        self.assertEqual(expected, actual)

    @patch('random.random', return_value=10)
    def test_monster_flee_did_not_run_return(self, mock_random):
        test_monster = {"name": "test monster"}
        actual = game.monster_flee(test_monster)
        self.assertFalse(actual)

    @patch('random.random', return_value=10)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_monster_flee_did_not_run_return_correct_print(self, mock_output, mock_random):
        test_monster = {"name": "test monster"}
        game.monster_flee(test_monster)
        actual = mock_output.getvalue()
        expected = f""
        self.assertEqual(expected, actual)
