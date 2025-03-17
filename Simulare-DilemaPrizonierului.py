import random

class Game:
    """Simulează o singură rundă din Dilema Prizonierului."""
    def play(self, action_p1, action_p2):
        if action_p1 == "T" and action_p2 == "T":
            return (-2, -2)  # Ambii primesc 2 ani de închisoare
        elif action_p1 == "C" and action_p2 == "C":
            return (-1, -1)  # Ambii primesc 1 an de închisoare
        elif action_p1 == "T" and action_p2 == "C":
            return (0, -3)   # P1 e liber, P2 primește 3 ani
        elif action_p1 == "C" and action_p2 == "T":
            return (-3, 0)   # P2 e liber, P1 primește 3 ani

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

# Testare
game = IteratedGame(rounds=5)
game.play_game(tit_for_tat, random_strategy)