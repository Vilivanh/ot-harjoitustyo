import unittest

from game.play import Play

class TestShuffle(unittest.TestCase):
    def test_shuffle(self):
        player, playing_computers = Play.deal(6)
        vastaus = len(playing_computers)
        self.assertEqual(vastaus, 5)
    def test_get_right_amount_of_cards(self):
        player, playing_computers = Play.deal(6)
        number_of_cards = len(player)
        self.assertEqual(number_of_cards, 9)
    def test_get_right_amount_of_cards_with_four_players(self):
        player, playing_computers = Play.deal(4)
        number_of_cards = len(player)
        self.assertEqual(number_of_cards, 13)
    def test_get_right_amount_of_cards_for_computer(self):
        player, playing_computers = Play.deal(6)
        number_of_cards = len(playing_computers[4])
        self.assertEqual(number_of_cards, 8)
    def test_get_right_amount_of_cards_for_computer_with_four_players(self):
        player, playing_computers = Play.deal(4)
        number_of_cards = len(playing_computers[1])
        self.assertEqual(number_of_cards, 13)




