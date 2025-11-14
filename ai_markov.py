from collections import defaultdict, deque
import random

MOVES = ["R", "P", "S"]

def counter_move(predicted_player_move: str | None) -> str:
    if predicted_player_move is None:
        return random.choice(MOVES)

    if predicted_player_move == "R":
        return "P" 
    if predicted_player_move == "P":
        return "S"
    return "R"

class MarkovSingleAI:
    def __init__(self, order: int):
        self.order = order
        self.history = deque(maxlen=order)
        self.transitions = defaultdict(lambda: defaultdict(int))

    def _predict_player_move(self) -> str | None:
        if len(self.history) < self.order:
            return None

        state = tuple(self.history)
        next_counts = self.transitions[state]
        if not next_counts:
            return None

        return max(next_counts, key=next_counts.get)

    def choose_move(self) -> str:
        predicted = self._predict_player_move()
        return counter_move(predicted)

    def update(self, player_move: str) -> None:
        if len(self.history) == self.order:
            state = tuple(self.history)
            self.transitions[state][player_move] += 1

        self.history.append(player_move)
