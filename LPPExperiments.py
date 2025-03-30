import random
import matplotlib.pyplot as plt

class Player:
    def __init__(self, id, strategy):
        self.id = id
        self.strategy = strategy
        self.total_profit = 0
        self.previous_bids = []
        self.bid = 0
        self.current_value = 0
        self.wins = 0  # Numar de licitatii castigate

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

def run_simulation(num_players, num_rounds, value_range, strategy_distribution, num_simulations=100):
    strategies = list(strategy_distribution.keys())
    
    strategy_stats = {strategy: {"wins": 0, "total_profit": 0, "bid_efficiency": []} for strategy in strategies}

    for _ in range(num_simulations):
        players = [Player(i, random.choices(strategies, weights=strategy_distribution.values())[0]) for i in range(num_players)]
        
        for _ in range(num_rounds):
            for player in players:
                player.current_value = random.uniform(*value_range)

            for player in players:
                player.make_bid([p.bid for p in players])

            winner = max(players, key=lambda p: p.bid)
            winner_profit = winner.current_value - winner.bid
            winner.total_profit += winner_profit
            winner.wins += 1

        for player in players:
            strategy_stats[player.strategy]["wins"] += player.wins
            strategy_stats[player.strategy]["total_profit"] += player.total_profit
            efficiency = sum([abs(player.current_value - player.bid) for player in players]) / num_rounds
            strategy_stats[player.strategy]["bid_efficiency"].append(efficiency)

    return strategy_stats

def plot_results(strategy_stats, num_simulations, title):
    strategies = list(strategy_stats.keys())
    
    wins = [strategy_stats[s]["wins"] / num_simulations for s in strategies]
    profits = [strategy_stats[s]["total_profit"] / num_simulations for s in strategies]
    efficiency = [sum(strategy_stats[s]["bid_efficiency"]) / num_simulations for s in strategies]

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 3, 1)
    plt.bar(strategies, wins, color='blue')
    plt.xticks(rotation=45)
    plt.title("Rata de succes (licitatii castigate)")

    plt.subplot(1, 3, 2)
    plt.bar(strategies, profits, color='green')
    plt.xticks(rotation=45)
    plt.title("Profit total")

    plt.subplot(1, 3, 3)
    plt.bar(strategies, efficiency, color='red')
    plt.xticks(rotation=45)
    plt.title("Eficienta bid-urilor")

    plt.suptitle(title)
    plt.tight_layout()
    plt.show()

# **Experimente pentru testarea strategiilor** 

experiments = [
    {"num_players": 5, "num_rounds": 10, "value_range": (10, 100), "strategy_distribution": {"agresiv": 1, "moderat": 1, "conservator": 1, "competitiv": 1, "adaptiv": 1}},
    {"num_players": 10, "num_rounds": 20, "value_range": (10, 100), "strategy_distribution": {"agresiv": 1, "moderat": 2, "conservator": 2, "competitiv": 1, "adaptiv": 1}},
    {"num_players": 5, "num_rounds": 10, "value_range": (50, 100), "strategy_distribution": {"riscant": 2, "precaut": 2, "aleator": 1}},
    {"num_players": 5, "num_rounds": 10, "value_range": (10, 50), "strategy_distribution": {"agresiv": 1, "moderat": 1, "conservator": 1, "competitiv": 1, "adaptiv": 1}},
    {"num_players": 20, "num_rounds": 5, "value_range": (10, 100), "strategy_distribution": {"competitiv": 2, "adaptiv": 2, "conservator": 1, "moderat": 1}},

    # Noi scenarii:
    {"num_players": 15, "num_rounds": 15, "value_range": (100, 500), "strategy_distribution": {"agresiv": 3, "moderat": 3, "conservator": 3, "competitiv": 3, "adaptiv": 3}},  # Piață competitivă mare
    {"num_players": 8, "num_rounds": 10, "value_range": (20, 200), "strategy_distribution": {"agresiv": 2, "conservator": 2, "adaptiv": 2, "aleator": 2}},  # Jucători variabili
    {"num_players": 5, "num_rounds": 15, "value_range": (5, 50), "strategy_distribution": {"riscant": 1, "precaut": 2, "competitiv": 2}},  # Resurse limitate
    {"num_players": 10, "num_rounds": 30, "value_range": (50, 500), "strategy_distribution": {"competitiv": 5, "adaptiv": 5}},  # Doar strategiile cele mai flexibile
    {"num_players": 20, "num_rounds": 10, "value_range": (10, 1000), "strategy_distribution": {"riscant": 5, "precaut": 5, "aleator": 5, "moderat": 5}},  # Piețe extreme
]

num_simulations = 500

for i, exp in enumerate(experiments):
    print(f"\nExperiment {i+1}: {exp}")
    results = run_simulation(**exp, num_simulations=num_simulations)
    plot_results(results, num_simulations, title=f"Experiment {i+1}")
