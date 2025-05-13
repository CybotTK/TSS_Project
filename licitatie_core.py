# licitatie_core.py
import random

class Player:
    def __init__(self, id, strategy):
        self.id = id
        self.strategy = strategy
        self.total_profit = 0
        self.previous_bids = []
        self.bid = 0
        self.current_value = 0
        self.wins = 0

    def make_bid(self, all_previous_bids=[]):
        if self.strategy == "agresiv":
            self.bid = random.uniform(0.8, 1.0) * self.current_value
        elif self.strategy == "moderat":
            self.bid = random.uniform(0.5, 0.8) * self.current_value
        elif self.strategy == "conservator":
            self.bid = random.uniform(0.2, 0.5) * self.current_value
        elif self.strategy == "aleator":
            self.bid = random.uniform(0.2, 1.0) * self.current_value
        elif self.strategy == "riscant":
            self.bid = random.uniform(0.95, 1.0) * self.current_value
        elif self.strategy == "precaut":
            self.bid = random.uniform(0.1, 0.4) * self.current_value
        elif self.strategy == "competitiv" and all_previous_bids:
            max_known_bid = max(all_previous_bids)
            self.bid = max_known_bid * random.uniform(0.9, 0.99)
        elif self.strategy == "adaptiv" and self.previous_bids:
            last_bid = self.previous_bids[-1]
            max_known_bid = max(all_previous_bids) if all_previous_bids else 0
            if last_bid < max_known_bid:
                self.bid = min(self.current_value, last_bid * 1.05)
            else:
                self.bid = last_bid * 0.95
        else:
            self.bid = random.uniform(0.2, 1.0) * self.current_value

        self.previous_bids.append(self.bid)
        return self.bid
