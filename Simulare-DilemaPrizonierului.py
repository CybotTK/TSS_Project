import random

class Game:
    """Simulează o singură rundă din Dilema Prizonierului."""
    def play(self, action_p1, action_p2):
        if action_p1 == "T" and action_p2 == "T":
            return (2, 2)  # Ambii primesc 2 ani de închisoare
        elif action_p1 == "C" and action_p2 == "C":
            return (1, 1)  # Ambii primesc 1 an de închisoare
        elif action_p1 == "T" and action_p2 == "C":
            return (0, 3)   # P1 e liber, P2 primește 3 ani
        elif action_p1 == "C" and action_p2 == "T":
            return (3, 0)   # P2 e liber, P1 primește 3 ani

class IteratedGame:
    """Rulează Dilema Prizonierului pe mai multe runde."""
    def __init__(self, rounds=10):
        self.game = Game()
        self.rounds = rounds

    def play_game(self, strategy_p1, strategy_p2):
        """Rulează jocul pe mai multe runde, folosind strategiile specificate."""
        score_p1, score_p2 = 0, 0
        history = []
        
        for _ in range(self.rounds):
            action_p1 = strategy_p1(history)
            action_p2 = strategy_p2(history)
            reward_p1, reward_p2 = self.game.play(action_p1, action_p2)

            score_p1 += reward_p1
            score_p2 += reward_p2
            history.append((action_p1, action_p2))

            print(f"Runda {len(history)}: P1 - {action_p1}, P2 - {action_p2} | Scor: {score_p1}, {score_p2}")

        print(f"\nScor final: P1 - {score_p1}, P2 - {score_p2}")

# Strategii diferite
def always_cooperate(_): return "C"
def always_betray(_): return "T"
def random_strategy(_): return random.choice(["C", "T"])
def tit_for_tat(history):
    """Începe cooperând, apoi copiază ultima alegere a adversarului."""
    if not history:
        return "C"
    return history[-1][1]  # Copiază ultima alegere a adversarului

# Simularea cu strategii diferite
game = IteratedGame(rounds=20)

# always_cooperate vs always_cooperate
print("Simulare: always_cooperate vs always_cooperate")
game.play_game(always_cooperate, always_cooperate)

# always_cooperate vs always_betray
print("\nSimulare: always_cooperate vs always_betray")
game.play_game(always_cooperate, always_betray)

# always_cooperate vs random_strategy
print("\nSimulare: always_cooperate vs random_strategy")
game.play_game(always_cooperate, random_strategy)

# always_cooperate vs tit_for_tat
print("\nSimulare: always_cooperate vs tit_for_tat")
game.play_game(always_cooperate, tit_for_tat)

# always_betray vs always_betray
print("\nSimulare: always_betray vs always_betray")
game.play_game(always_betray, always_betray)

# always_betray vs random_strategy
print("\nSimulare: always_betray vs random_strategy")
game.play_game(always_betray, random_strategy)

# always_betray vs tit_for_tat
print("\nSimulare: always_betray vs tit_for_tat")
game.play_game(always_betray, tit_for_tat)

# random_strategy vs random_strategy
print("\nSimulare: random_strategy vs random_strategy")
game.play_game(random_strategy, random_strategy)

# random_strategy vs tit_for_tat
print("\nSimulare: random_strategy vs tit_for_tat")
game.play_game(random_strategy, tit_for_tat)

# tit_for_tat vs tit_for_tat
print("\nSimulare: tit_for_tat vs tit_for_tat")
game.play_game(tit_for_tat, tit_for_tat)

"""Simulare: always_cooperate vs always_cooperate
Runda 1: P1 - C, P2 - C | Scor: 1, 1
Runda 2: P1 - C, P2 - C | Scor: 2, 2
Runda 3: P1 - C, P2 - C | Scor: 3, 3
Runda 4: P1 - C, P2 - C | Scor: 4, 4
Runda 5: P1 - C, P2 - C | Scor: 5, 5
Runda 6: P1 - C, P2 - C | Scor: 6, 6
Runda 7: P1 - C, P2 - C | Scor: 7, 7
Runda 8: P1 - C, P2 - C | Scor: 8, 8
Runda 9: P1 - C, P2 - C | Scor: 9, 9
Runda 10: P1 - C, P2 - C | Scor: 10, 10
Runda 11: P1 - C, P2 - C | Scor: 11, 11
Runda 12: P1 - C, P2 - C | Scor: 12, 12
Runda 13: P1 - C, P2 - C | Scor: 13, 13
Runda 14: P1 - C, P2 - C | Scor: 14, 14
Runda 15: P1 - C, P2 - C | Scor: 15, 15
Runda 16: P1 - C, P2 - C | Scor: 16, 16
Runda 17: P1 - C, P2 - C | Scor: 17, 17
Runda 18: P1 - C, P2 - C | Scor: 18, 18
Runda 19: P1 - C, P2 - C | Scor: 19, 19
Runda 20: P1 - C, P2 - C | Scor: 20, 20

Scor final: P1 - 20, P2 - 20

Simulare: always_cooperate vs always_betray
Runda 1: P1 - C, P2 - T | Scor: 3, 0
Runda 2: P1 - C, P2 - T | Scor: 6, 0
Runda 3: P1 - C, P2 - T | Scor: 9, 0
Runda 4: P1 - C, P2 - T | Scor: 12, 0
Runda 5: P1 - C, P2 - T | Scor: 15, 0
Runda 6: P1 - C, P2 - T | Scor: 18, 0
Runda 7: P1 - C, P2 - T | Scor: 21, 0
Runda 8: P1 - C, P2 - T | Scor: 24, 0
Runda 9: P1 - C, P2 - T | Scor: 27, 0
Runda 10: P1 - C, P2 - T | Scor: 30, 0
Runda 11: P1 - C, P2 - T | Scor: 33, 0
Runda 12: P1 - C, P2 - T | Scor: 36, 0
Runda 13: P1 - C, P2 - T | Scor: 39, 0
Runda 14: P1 - C, P2 - T | Scor: 42, 0
Runda 15: P1 - C, P2 - T | Scor: 45, 0
Runda 16: P1 - C, P2 - T | Scor: 48, 0
Runda 17: P1 - C, P2 - T | Scor: 51, 0
Runda 18: P1 - C, P2 - T | Scor: 54, 0
Runda 19: P1 - C, P2 - T | Scor: 57, 0
Runda 20: P1 - C, P2 - T | Scor: 60, 0

Scor final: P1 - 60, P2 - 0

Simulare: always_cooperate vs random_strategy
Runda 1: P1 - C, P2 - T | Scor: 3, 0
Runda 2: P1 - C, P2 - T | Scor: 6, 0
Runda 3: P1 - C, P2 - C | Scor: 7, 1
Runda 4: P1 - C, P2 - T | Scor: 10, 1
Runda 5: P1 - C, P2 - T | Scor: 13, 1
Runda 6: P1 - C, P2 - T | Scor: 16, 1
Runda 7: P1 - C, P2 - T | Scor: 19, 1
Runda 8: P1 - C, P2 - C | Scor: 20, 2
Runda 9: P1 - C, P2 - C | Scor: 21, 3
Runda 10: P1 - C, P2 - T | Scor: 24, 3
Runda 11: P1 - C, P2 - C | Scor: 25, 4
Runda 12: P1 - C, P2 - C | Scor: 26, 5
Runda 13: P1 - C, P2 - T | Scor: 29, 5
Runda 14: P1 - C, P2 - T | Scor: 32, 5
Runda 15: P1 - C, P2 - C | Scor: 33, 6
Runda 16: P1 - C, P2 - T | Scor: 36, 6
Runda 17: P1 - C, P2 - T | Scor: 39, 6
Runda 18: P1 - C, P2 - C | Scor: 40, 7
Runda 19: P1 - C, P2 - C | Scor: 41, 8
Runda 20: P1 - C, P2 - C | Scor: 42, 9

Scor final: P1 - 42, P2 - 9

Simulare: always_cooperate vs tit_for_tat
Runda 1: P1 - C, P2 - C | Scor: 1, 1
Runda 2: P1 - C, P2 - C | Scor: 2, 2
Runda 3: P1 - C, P2 - C | Scor: 3, 3
Runda 4: P1 - C, P2 - C | Scor: 4, 4
Runda 5: P1 - C, P2 - C | Scor: 5, 5
Runda 6: P1 - C, P2 - C | Scor: 6, 6
Runda 7: P1 - C, P2 - C | Scor: 7, 7
Runda 8: P1 - C, P2 - C | Scor: 8, 8
Runda 9: P1 - C, P2 - C | Scor: 9, 9
Runda 10: P1 - C, P2 - C | Scor: 10, 10
Runda 11: P1 - C, P2 - C | Scor: 11, 11
Runda 12: P1 - C, P2 - C | Scor: 12, 12
Runda 13: P1 - C, P2 - C | Scor: 13, 13
Runda 14: P1 - C, P2 - C | Scor: 14, 14
Runda 15: P1 - C, P2 - C | Scor: 15, 15
Runda 16: P1 - C, P2 - C | Scor: 16, 16
Runda 17: P1 - C, P2 - C | Scor: 17, 17
Runda 18: P1 - C, P2 - C | Scor: 18, 18
Runda 19: P1 - C, P2 - C | Scor: 19, 19
Runda 20: P1 - C, P2 - C | Scor: 20, 20

Scor final: P1 - 20, P2 - 20

Simulare: always_betray vs always_betray
Runda 1: P1 - T, P2 - T | Scor: 2, 2
Runda 2: P1 - T, P2 - T | Scor: 4, 4
Runda 3: P1 - T, P2 - T | Scor: 6, 6
Runda 4: P1 - T, P2 - T | Scor: 8, 8
Runda 5: P1 - T, P2 - T | Scor: 10, 10
Runda 6: P1 - T, P2 - T | Scor: 12, 12
Runda 7: P1 - T, P2 - T | Scor: 14, 14
Runda 8: P1 - T, P2 - T | Scor: 16, 16
Runda 9: P1 - T, P2 - T | Scor: 18, 18
Runda 10: P1 - T, P2 - T | Scor: 20, 20
Runda 11: P1 - T, P2 - T | Scor: 22, 22
Runda 12: P1 - T, P2 - T | Scor: 24, 24
Runda 13: P1 - T, P2 - T | Scor: 26, 26
Runda 14: P1 - T, P2 - T | Scor: 28, 28
Runda 15: P1 - T, P2 - T | Scor: 30, 30
Runda 16: P1 - T, P2 - T | Scor: 32, 32
Runda 17: P1 - T, P2 - T | Scor: 34, 34
Runda 18: P1 - T, P2 - T | Scor: 36, 36
Runda 19: P1 - T, P2 - T | Scor: 38, 38
Runda 20: P1 - T, P2 - T | Scor: 40, 40

Scor final: P1 - 40, P2 - 40

Simulare: always_betray vs random_strategy
Runda 1: P1 - T, P2 - C | Scor: 0, 3
Runda 2: P1 - T, P2 - C | Scor: 0, 6
Runda 3: P1 - T, P2 - T | Scor: 2, 8
Runda 4: P1 - T, P2 - T | Scor: 4, 10
Runda 5: P1 - T, P2 - C | Scor: 4, 13
Runda 6: P1 - T, P2 - T | Scor: 6, 15
Runda 7: P1 - T, P2 - T | Scor: 8, 17
Runda 8: P1 - T, P2 - C | Scor: 8, 20
Runda 9: P1 - T, P2 - T | Scor: 10, 22
Runda 10: P1 - T, P2 - T | Scor: 12, 24
Runda 11: P1 - T, P2 - T | Scor: 14, 26
Runda 12: P1 - T, P2 - T | Scor: 16, 28
Runda 13: P1 - T, P2 - T | Scor: 18, 30
Runda 14: P1 - T, P2 - C | Scor: 18, 33
Runda 15: P1 - T, P2 - C | Scor: 18, 36
Runda 16: P1 - T, P2 - T | Scor: 20, 38
Runda 17: P1 - T, P2 - T | Scor: 22, 40
Runda 18: P1 - T, P2 - T | Scor: 24, 42
Runda 19: P1 - T, P2 - T | Scor: 26, 44
Runda 20: P1 - T, P2 - T | Scor: 28, 46

Scor final: P1 - 28, P2 - 46

Simulare: always_betray vs tit_for_tat
Runda 1: P1 - T, P2 - C | Scor: 0, 3
Runda 2: P1 - T, P2 - C | Scor: 0, 6
Runda 3: P1 - T, P2 - C | Scor: 0, 9
Runda 4: P1 - T, P2 - C | Scor: 0, 12
Runda 5: P1 - T, P2 - C | Scor: 0, 15
Runda 6: P1 - T, P2 - C | Scor: 0, 18
Runda 7: P1 - T, P2 - C | Scor: 0, 21
Runda 8: P1 - T, P2 - C | Scor: 0, 24
Runda 9: P1 - T, P2 - C | Scor: 0, 27
Runda 10: P1 - T, P2 - C | Scor: 0, 30
Runda 11: P1 - T, P2 - C | Scor: 0, 33
Runda 12: P1 - T, P2 - C | Scor: 0, 36
Runda 13: P1 - T, P2 - C | Scor: 0, 39
Runda 14: P1 - T, P2 - C | Scor: 0, 42
Runda 15: P1 - T, P2 - C | Scor: 0, 45
Runda 16: P1 - T, P2 - C | Scor: 0, 48
Runda 17: P1 - T, P2 - C | Scor: 0, 51
Runda 18: P1 - T, P2 - C | Scor: 0, 54
Runda 19: P1 - T, P2 - C | Scor: 0, 57
Runda 20: P1 - T, P2 - C | Scor: 0, 60

Scor final: P1 - 0, P2 - 60

Simulare: random_strategy vs random_strategy
Runda 1: P1 - C, P2 - T | Scor: 3, 0
Runda 2: P1 - T, P2 - C | Scor: 3, 3
Runda 3: P1 - C, P2 - T | Scor: 6, 3
Runda 4: P1 - C, P2 - T | Scor: 9, 3
Runda 5: P1 - T, P2 - C | Scor: 9, 6
Runda 6: P1 - T, P2 - C | Scor: 9, 9
Runda 7: P1 - T, P2 - T | Scor: 11, 11
Runda 8: P1 - T, P2 - T | Scor: 13, 13
Runda 9: P1 - C, P2 - T | Scor: 16, 13
Runda 10: P1 - T, P2 - T | Scor: 18, 15
Runda 11: P1 - C, P2 - C | Scor: 19, 16
Runda 12: P1 - T, P2 - C | Scor: 19, 19
Runda 13: P1 - C, P2 - C | Scor: 20, 20
Runda 14: P1 - C, P2 - C | Scor: 21, 21
Runda 15: P1 - T, P2 - C | Scor: 21, 24
Runda 16: P1 - T, P2 - T | Scor: 23, 26
Runda 17: P1 - T, P2 - C | Scor: 23, 29
Runda 18: P1 - C, P2 - T | Scor: 26, 29
Runda 19: P1 - T, P2 - T | Scor: 28, 31
Runda 20: P1 - C, P2 - T | Scor: 31, 31

Scor final: P1 - 31, P2 - 31

Simulare: random_strategy vs tit_for_tat
Runda 1: P1 - T, P2 - C | Scor: 0, 3
Runda 2: P1 - T, P2 - C | Scor: 0, 6
Runda 3: P1 - T, P2 - C | Scor: 0, 9
Runda 4: P1 - T, P2 - C | Scor: 0, 12
Runda 5: P1 - C, P2 - C | Scor: 1, 13
Runda 6: P1 - T, P2 - C | Scor: 1, 16
Runda 7: P1 - C, P2 - C | Scor: 2, 17
Runda 8: P1 - T, P2 - C | Scor: 2, 20
Runda 9: P1 - C, P2 - C | Scor: 3, 21
Runda 10: P1 - T, P2 - C | Scor: 3, 24
Runda 11: P1 - T, P2 - C | Scor: 3, 27
Runda 12: P1 - C, P2 - C | Scor: 4, 28
Runda 13: P1 - T, P2 - C | Scor: 4, 31
Runda 14: P1 - T, P2 - C | Scor: 4, 34
Runda 15: P1 - T, P2 - C | Scor: 4, 37
Runda 16: P1 - T, P2 - C | Scor: 4, 40
Runda 17: P1 - C, P2 - C | Scor: 5, 41
Runda 18: P1 - C, P2 - C | Scor: 6, 42
Runda 19: P1 - C, P2 - C | Scor: 7, 43
Runda 20: P1 - T, P2 - C | Scor: 7, 46

Scor final: P1 - 7, P2 - 46

Simulare: tit_for_tat vs tit_for_tat
Runda 1: P1 - C, P2 - C | Scor: 1, 1
Runda 2: P1 - C, P2 - C | Scor: 2, 2
Runda 3: P1 - C, P2 - C | Scor: 3, 3
Runda 4: P1 - C, P2 - C | Scor: 4, 4
Runda 5: P1 - C, P2 - C | Scor: 5, 5
Runda 6: P1 - C, P2 - C | Scor: 6, 6
Runda 7: P1 - C, P2 - C | Scor: 7, 7
Runda 8: P1 - C, P2 - C | Scor: 8, 8
Runda 9: P1 - C, P2 - C | Scor: 9, 9
Runda 10: P1 - C, P2 - C | Scor: 10, 10
Runda 11: P1 - C, P2 - C | Scor: 11, 11
Runda 12: P1 - C, P2 - C | Scor: 12, 12
Runda 13: P1 - C, P2 - C | Scor: 13, 13
Runda 14: P1 - C, P2 - C | Scor: 14, 14
Runda 15: P1 - C, P2 - C | Scor: 15, 15
Runda 16: P1 - C, P2 - C | Scor: 16, 16
Runda 17: P1 - C, P2 - C | Scor: 17, 17
Runda 18: P1 - C, P2 - C | Scor: 18, 18
Runda 19: P1 - C, P2 - C | Scor: 19, 19
Runda 20: P1 - C, P2 - C | Scor: 20, 20

Scor final: P1 - 20, P2 - 20
"""