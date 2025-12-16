from typing import List
from ai_markov import MarkovSingleAI, MOVES
import random


def score_for_ai(ai_move: str, player_move: str) -> int:
    if ai_move == player_move:
        return 0

    if (
        (ai_move == "R" and player_move == "S") or
        (ai_move == "P" and player_move == "R") or
        (ai_move == "S" and player_move == "P")
    ):
        return 1

    return -1


class MultiAI:
    """
    MultiAI koostuu viidestä MarkovSingleAI:sta:

    Jokaisella kierroksella:
      - jokainen AI valitsee oman siirtonsa
      - jokaisen AI:n siirto pisteytetään pelaajan siirtoa vastaan (-1/0/1)
      - pisteet tallennetaan score-historiaan
      - paras AI valitaan viimeisten `focus_length` kierroksen pistemäärän perusteella

    Pelaajalle näytettävä siirto on aina kulloinkin parhaan AI:n siirto.
    """

    def __init__(self, focus_length: int = 5, debug: bool = False):
        self.focus_length = focus_length

        self.single_ais: List[MarkovSingleAI] = [
            MarkovSingleAI(order=i) for i in range(1, 6)
        ]

        self.scores: List[List[int]] = [[] for _ in self.single_ais]

        self.last_moves: List[str] = [random.choice(MOVES) for _ in self.single_ais]

        self.debug = debug

    def _best_ai_index(self) -> int:
        best_index = 0
        best_score = float("-inf")

        for i, score_history in enumerate(self.scores):
            window = score_history[-self.focus_length:]
            total = sum(window) if window else 0

            if total > best_score:
                best_score = total
                best_index = i

        return best_index

    def choose_move(self) -> str:
        for i, ai in enumerate(self.single_ais):
            self.last_moves[i] = ai.choose_move()

        best_ai_index = self._best_ai_index()

        if self.debug:
            window_scores = [
                sum(history[-self.focus_length:]) if history else 0
                for history in self.scores
            ]
            print(f"[DEBUG] Using AI #{best_ai_index + 1}")

        return self.last_moves[best_ai_index]

    def update(self, player_move: str) -> None:

        for i, ai in enumerate(self.single_ais):
            ai_move = self.last_moves[i]
            s = score_for_ai(ai_move, player_move)
            self.scores[i].append(s)
            ai.update(player_move)
