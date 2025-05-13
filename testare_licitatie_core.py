# test_licitatie_core.py
import unittest
from licitatie_core import Player

class TestPlayerStrategies(unittest.TestCase):

    def setUp(self):
        self.value = 100

    def test_agresiv(self):
        player = Player(1, "agresiv")
        player.current_value = self.value
        bid = player.make_bid()
        self.assertGreaterEqual(bid, 0.8 * self.value)
        self.assertLessEqual(bid, 1.0 * self.value)

    def test_moderat(self):
        player = Player(1, "moderat")
        player.current_value = self.value
        bid = player.make_bid()
        self.assertGreaterEqual(bid, 0.5 * self.value)
        self.assertLessEqual(bid, 0.8 * self.value)

    def test_conservator(self):
        player = Player(1, "conservator")
        player.current_value = self.value
        bid = player.make_bid()
        self.assertGreaterEqual(bid, 0.2 * self.value)
        self.assertLessEqual(bid, 0.5 * self.value)

    def test_aleator(self):
        player = Player(1, "aleator")
        player.current_value = self.value
        bid = player.make_bid()
        self.assertGreaterEqual(bid, 0.2 * self.value)
        self.assertLessEqual(bid, 1.0 * self.value)

    def test_riscant(self):
        player = Player(1, "riscant")
        player.current_value = self.value
        bid = player.make_bid()
        self.assertGreaterEqual(bid, 0.95 * self.value)
        self.assertLessEqual(bid, 1.0 * self.value)

    def test_precaut(self):
        player = Player(1, "precaut")
        player.current_value = self.value
        bid = player.make_bid()
        self.assertGreaterEqual(bid, 0.1 * self.value)
        self.assertLessEqual(bid, 0.4 * self.value)

    def test_competitiv(self):
        player = Player(1, "competitiv")
        player.current_value = self.value
        previous_bids = [80, 90, 85]
        bid = player.make_bid(previous_bids)
        self.assertLess(bid, max(previous_bids))
        self.assertGreater(bid, 0)

    def test_adaptiv_gain(self):
        player = Player(1, "adaptiv")
        player.current_value = self.value
        player.previous_bids = [70]
        bid = player.make_bid([80])
        self.assertGreaterEqual(bid, 70)

    def test_adaptiv_reduce(self):
        player = Player(1, "adaptiv")
        player.current_value = self.value
        player.previous_bids = [90]
        bid = player.make_bid([80])
        self.assertLessEqual(bid, 90)

if __name__ == '__main__':
    unittest.main()


#RULEZ DOAR CAND SE SCHIMBA CODUL PRINCIPAL
#PENTRU ECHIPA SI SCHIMBARI IN COD