import unittest

from shuffle import Methods

class TestShuffle(unittest.TestCase):
    def test_shuffle(self):
        playerlists = shuffle[1]
        vastaus = len(playerlists)
        self.assertEqual(vastaus, 4)


