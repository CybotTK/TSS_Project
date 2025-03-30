import random

class Player:
    def __init__(self, id, strategy):
        self.id = id
        self.strategy = strategy  # Strategia aleasă
        self.total_profit = 0  # Profitul acumulat pe parcursul rundelor
        self.previous_bids = []  # Istoricul ofertelor sale
        self.bid = 0  # Inițializăm bid-ul ca 0
        self.current_value = 0  # Valoarea curentă a obiectului la fiecare rundă

    def make_bid(self, all_previous_bids=[]):
        """Jucătorul face o ofertă în funcție de strategia sa și de rundele anterioare."""
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
            # Licitează puțin sub cel mai mare bid cunoscut
            max_known_bid = max(all_previous_bids)
            self.bid = max_known_bid * random.uniform(0.9, 0.99)
        elif self.strategy == "adaptiv" and self.previous_bids:
            # Crește ușor oferta dacă în runda anterioară nu a câștigat
            last_bid = self.previous_bids[-1]
            max_known_bid = max(all_previous_bids) if all_previous_bids else 0
            if last_bid < max_known_bid:
                self.bid = min(self.current_value, last_bid * 1.05)
            else:
                self.bid = last_bid * 0.95  # Dacă a câștigat, scade puțin
        else:
            self.bid = random.uniform(0.2, 1.0) * self.current_value  # Default
        
        self.previous_bids.append(self.bid)
        return self.bid

def first_price_auction(num_players=5, num_rounds=5):
    strategies = ["agresiv", "moderat", "conservator", "aleator", "riscant", "precaut", "competitiv", "adaptiv"]

    # Inițializăm jucătorii cu strategii aleatorii
    players = [Player(i, random.choice(strategies)) for i in range(num_players)]

    print("\n=== Simulare Licitație - Multiple Runde ===")

    for round_num in range(1, num_rounds + 1):
        print(f"\n--- Runda {round_num} ---")
        
        # Alegem o valoare random a obiectului pentru fiecare jucător în această rundă
        for player in players:
            player.current_value = random.uniform(10, 100)  # Obiectul valorează între 10 și 100

        # Generăm ofertele înainte de a construi lista de bids
        for player in players:
            player.make_bid([p.bid for p in players])

        all_bids = [player.bid for player in players]  # Acum bid-urile sunt definite

        # Determinăm câștigătorul rundei
        winner = max(players, key=lambda p: p.bid)
        winner_profit = winner.current_value - winner.bid
        winner.total_profit += winner_profit

        # Afișăm rezultatele rundei
        for player in players:
            print(f"Jucător {player.id}: Valoare {player.current_value:.2f}, Ofertă {player.bid:.2f}, Strategie: {player.strategy}")

        print(f"\n🏆 Câștigător: Jucător {winner.id} cu oferta {winner.bid:.2f} ({winner.strategy})")
        print(f"💰 Profit runda {round_num}: {winner_profit:.2f}")

    # După toate rundele, afișăm profitul total al fiecărui jucător
    print("\n=== Rezultate Finale ===")
    for player in players:
        print(f"Jucător {player.id} ({player.strategy}) - Profit Total: {player.total_profit:.2f}")

# Rulăm simularea
first_price_auction()
