import unittest
from game.handlers import Handlers

class TestHandlers(unittest.TestCase):
    def test_rank_fixer(self):
        rank = Handlers().rank_fixer("11")
        self.assertEqual(rank, "jack")
    def test_rank_fixer_ace(self):
        rank = Handlers().rank_fixer("14")
        self.assertEqual(rank, "ace")
    def test_rank_fixer_small(self):
        for i in range(2,11):
            rank = Handlers().rank_fixer(f"{i}")
            self.assertEqual(rank, i)
    def test_rank_integer(self):
        rank = Handlers().rank_integer("jack")
        self.assertEqual(rank, "11")
    def test_rank_integer_ace(self):
        rank = Handlers().rank_integer("ace")
        rank_queen = Handlers().rank.integer("queen")
        self.assertEqual(rank, "14")
        self.assertEqual(rank_queen, "12")
    def test_rank_integer_small(self):
        for i in range(2,11):
            rank = Handlers().rank_fixer(str(i))
            self.assertEqual(rank, str(i))
        
