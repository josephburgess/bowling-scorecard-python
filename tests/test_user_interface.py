import unittest
from unittest.mock import Mock, patch
from app.user_interface import UserInterface


class TestUserInterface(unittest.TestCase):
    def setUp(self):
        self.game = Mock()
        self.user_interface = UserInterface(self.game)

    @patch("builtins.input", side_effect=["5"])
    def test_get_roll_one(self, mock_input):
        roll_one = self.user_interface.get_roll_one()
        assert roll_one == 5

    @patch("builtins.input", side_effect=["5", "3"])
    def test_get_roll_two(self, mock_input):
        self.user_interface.get_roll_one()
        roll_two = self.user_interface.get_roll_two()
        assert roll_two == 3

    @patch("builtins.input", side_effect=["5", "5", "2"])
    def test_get_roll_three(self, mock_input):
        self.game.frame_count = 10
        self.user_interface.get_roll_one()
        self.user_interface.get_roll_two()
        roll_three = self.user_interface.get_roll_three()
        assert roll_three == 2

    @patch("builtins.input", side_effect=["5", "5", "2"])
    def test_roll_three_user_input_when_not_final_frame(self, mock_input):
        self.game.frame_count = 8
        self.user_interface.get_roll_one()
        self.user_interface.get_roll_two()
        roll_three = self.user_interface.get_roll_three()
        assert roll_three == 0

    def test_get_roll_three_in_frames_1_to_9(self):
        for i in range(1, 10):
            self.game.frame_count = i
            roll_three = self.user_interface.get_roll_three()
            assert roll_three == 0

    def test_get_roll_three_in_frame_10_open_frame(self):
        self.game.frame_count = 10
        self.user_interface.roll_one = 5
        self.user_interface.roll_two = 4
        roll_three = self.user_interface.get_roll_three()
        assert roll_three == 0

    @patch("builtins.input", side_effect=["10", "10", "5"])
    def test_get_roll_three_in_frame_10_strike(self, mock_input):
        self.game.frame_count = 10
        self.user_interface.get_roll_one()
        self.user_interface.get_roll_two()
        roll_three = self.user_interface.get_roll_three()
        assert roll_three == 5


if __name__ == "__main__":
    unittest.main()
