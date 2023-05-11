import unittest
from game.Computerchoose import ComputerChoose
from game.handlers import Handlers
class TestHand:
    def __init__(self, hand=None):
        self.hand = hand or []
    def add_card_to_test_hand(self, card):
        self.hand.append(card)
        return card


class TestComputerchoose(unittest.TestCase):
    def setUp(self):
        self.test_card_list_a = [("2", "spade"), ("5", "diamond"), ("ace", "diamond"), ("king", "spade"), ("queen", "club")]
        self.test_card_list_b = [("2", "heart"), ("5", "diamond"), ("ace", "diamond"), ("king", "spade"), ("queen", "club"), ("3", "heart"), ("4", "heart"), ("9", "heart")]
        self.test_tabledeck = [("5", "heart"), ("7", "heart")]
    def test_emptytable(self):
        self.hand_a = TestHand(self.test_card_list_a)
        self.hand_b = TestHand(self.test_card_list_b)
        chosen_a = ComputerChoose().emptytable(self.hand_a)
        chosen_b = ComputerChoose().emptytable(self.hand_b)
        self.assertEqual(chosen_a, ("2","spade"))
        self.assertEqual(chosen_b, ("2","heart"))
    def test_nonempty(self):
        self.tabledeck_a = TestHand(self.test_tabledeck)
        self.test_card_list_b = TestHand(self.test_card_list_b)
        self.players_number = 6
        chosen = ComputerChoose().nonempty(self.test_tabledeck, self.test_card_list_b, self.players_number)
        self.assertEqual(chosen, ("9", "heart"))

    
