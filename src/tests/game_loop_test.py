import unittest

import game_loop
import constants

class TestLoop(unittest.TestCase):
    def test_game_loop(self):
        ComputerHands = [[('3', 'club'), ('2', 'diamond'), ('5', 'spade')], [('10', 'diamond')], [('3', 'heart'), ('ace', 'spade')], [('jack', 'club'), ('queen', 'diamond')], [('8', 'spade'), ('5', 'heart')]]
        PlayerHand = [('king', 'club'), ('9', 'heart')]
        tabledeck = [('8', 'diamond')]
        TurnToPlay = "Computer 1"
        played_cards = 20
        game_loop()
        self.assertEqual(vastaus, 6)
