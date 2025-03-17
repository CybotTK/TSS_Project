# import random

# class Player:
#     def __init__(self, strategy="cooperative"):
#         self.strategy = strategy  # "cooperative" (cerb) sau "selfish" (iepure)
#         self.score = 0

#     def decide(self):
#         if self.strategy == "cooperative":
#             return "stag"
#         elif self.strategy == "selfish":
#             return "hare"
#         else:
#             return random.choice(["stag", "hare"])  # Strategie aleatoare

# class StagHuntGame:
#     def __init__(self, player1, player2, rounds=10):
#         self.player1 = player1
#         self.player2 = player2
#         self.rounds = rounds
#         self.payoff_matrix = {
#             ("stag", "stag"): (3, 3),
#             ("stag", "hare"): (0, 2),
#             ("hare", "stag"): (2, 0),
#             ("hare", "hare"): (1, 1)
#         }
    
#     def play(self):
#         for _ in range(self.rounds):
#             choice1 = self.player1.decide()
#             choice2 = self.player2.decide()
#             reward1, reward2 = self.payoff_matrix[(choice1, choice2)]
#             self.player1.score += reward1
#             self.player2.score += reward2
#             print(f"Round: P1({choice1}) vs P2({choice2}) -> Scores: P1({self.player1.score}), P2({self.player2.score})")
    
#     def results(self):
#         return f"Final Score: P1({self.player1.score}), P2({self.player2.score})"

# # Simulare
# p1 = Player(strategy="cooperative")  # Jucător care cooperează (cerb)
# p2 = Player(strategy="selfish")  # Jucător care acționează independent (iepure)
# game = StagHuntGame(p1, p2, rounds=10)
# game.play()
# print(game.results())


# ///////////////////////

# import random

# class Player:
#     def __init__(self, strategies=["cooperative", "selfish", "random"]):
#         self.strategies = strategies  # Lista de strategii posibile
#         self.strategy = random.choice(strategies)  # Alege o strategie inițială
#         self.score = 0

#     def decide(self):
#         if self.strategy == "cooperative":
#             return "stag"
#         elif self.strategy == "selfish":
#             return "hare"
#         else:
#             return random.choice(["stag", "hare"])  # Strategie aleatoare

#     def update_strategy(self):
#         # Schimbă strategia în funcție de scor, cu o probabilitate de ajustare
#         if random.random() < 0.2:  # 20% șansă să schimbe strategia
#             self.strategy = random.choice(self.strategies)

# class StagHuntGame:
#     def __init__(self, player1, player2, rounds=10):
#         self.player1 = player1
#         self.player2 = player2
#         self.rounds = rounds
#         self.payoff_matrix = {
#             ("stag", "stag"): (3, 3),
#             ("stag", "hare"): (0, 2),
#             ("hare", "stag"): (2, 0),
#             ("hare", "hare"): (1, 1)
#         }
    
#     def play(self):
#         for _ in range(self.rounds):
#             choice1 = self.player1.decide()
#             choice2 = self.player2.decide()
#             reward1, reward2 = self.payoff_matrix[(choice1, choice2)]
#             self.player1.score += reward1
#             self.player2.score += reward2
#             print(f"Round: P1({self.player1.strategy} -> {choice1}) vs P2({self.player2.strategy} -> {choice2}) -> Scores: P1({self.player1.score}), P2({self.player2.score})")
            
#             self.player1.update_strategy()
#             self.player2.update_strategy()
    
#     def results(self):
#         return f"Final Score: P1({self.player1.score}), P2({self.player2.score})"

# # Simulare
# p1 = Player(strategies=["cooperative", "selfish", "random"])  # Jucător cu strategii variabile
# p2 = Player(strategies=["cooperative", "selfish", "random"])  # Jucător cu strategii variabile
# game = StagHuntGame(p1, p2, rounds=20)
# game.play()
# print(game.results())


import random

class Player:
    def __init__(self, strategies=["cooperative", "selfish", "random", "tit_for_tat", "tit_for_tat_with_forgiveness"]):
        self.strategies = strategies  # Lista de strategii posibile
        self.strategy = random.choice(strategies)  # Alege o strategie inițială
        self.score = 0
        self.last_opponent_choice = "stag"  # Inițial presupune cooperare

    def decide(self):
        if self.strategy == "cooperative":
            return "stag"
        elif self.strategy == "selfish":
            return "hare"
        elif self.strategy == "tit_for_tat":
            return self.last_opponent_choice  # Copiază ultima alegere a adversarului
        elif self.strategy == "tit_for_tat_with_forgiveness":
            if self.last_opponent_choice == "hare" and random.random() < 0.2:  # 20% șansă de a ierta
                return "stag"
            return self.last_opponent_choice
        else:
            return random.choice(["stag", "hare"])  # Strategie aleatoare

    def update_strategy(self):
        # Schimbă strategia în funcție de scor, cu o probabilitate de ajustare
        if random.random() < 0.2:  # 20% șansă să schimbe strategia
            self.strategy = random.choice(self.strategies)

class StagHuntGame:
    def __init__(self, player1, player2, rounds=10):
        self.player1 = player1
        self.player2 = player2
        self.rounds = rounds
        self.payoff_matrix = {
            ("stag", "stag"): (3, 3),
            ("stag", "hare"): (0, 2),
            ("hare", "stag"): (2, 0),
            ("hare", "hare"): (1, 1)
        }
    
    def play(self):
        for _ in range(self.rounds):
            choice1 = self.player1.decide()
            choice2 = self.player2.decide()
            reward1, reward2 = self.payoff_matrix[(choice1, choice2)]
            self.player1.score += reward1
            self.player2.score += reward2
            print(f"Round: P1({self.player1.strategy} -> {choice1}) vs P2({self.player2.strategy} -> {choice2}) -> Scores: P1({self.player1.score}), P2({self.player2.score})")
            
            # Actualizează alegerea anterioară a adversarului pentru strategia tit-for-tat
            self.player1.last_opponent_choice = choice2
            self.player2.last_opponent_choice = choice1
            
            self.player1.update_strategy()
            self.player2.update_strategy()
    
    def results(self):
        return f"Final Score: P1({self.player1.score}), P2({self.player2.score})"

# Simulare
p1 = Player(strategies=["cooperative", "selfish", "random", "tit_for_tat", "tit_for_tat_with_forgiveness"])  # Jucător cu strategii variabile
p2 = Player(strategies=["cooperative", "selfish", "random", "tit_for_tat", "tit_for_tat_with_forgiveness"])  # Jucător cu strategii variabile
game = StagHuntGame(p1, p2, rounds=20)
game.play()
print(game.results())
