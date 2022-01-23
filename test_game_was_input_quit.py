from unittest import TestCase
import game


class TestWasInputQuit(TestCase):
    def test_was_input_quit(self):
        with self.assertRaises(SystemExit) as cm:
            game.was_input_quit("quit")
        self.assertEqual(cm.exception.code, "You have quit the game \n Thanks for playing")

    def test_was_input_quit_not(self):
        try:
            game.was_input_quit("north")
        except SystemExit:
            self.fail("was_input_quit() exited unexpectedly")
