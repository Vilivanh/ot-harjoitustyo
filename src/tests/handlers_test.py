import unittest
from game.handlers import Handlers

class TestHandlers(unittest.TestCase):
    def test_rank_fixer(self):
        rank = Handlers.rank_fixer("11")
        self.assertEqual(rank, "jack")
    def test_rank_fixer_ace(self):
        rank = Handlers.rank_fixer("14")
        self.assertEqual(rank, "ace")
    def test_rank_fixer_small(self):
        rank = Handlers.rank_fixer("4")
        self.assertEqual(rank, "4")
    def test_rank_integer(self):
        rank = Handlers.rank_integer("jack")
        self.assertEqual(rank, "11")
    def test_rank_integer_ace(self):
        rank = Handlers.rank_integer("ace")
        self.assertEqual(rank, "14")
    def test_rank_integer_small(self):
        rank = Handlers.rank_integer("4")
        self.assertEqual(rank, "4")
