from ai_multi import MultiAI, score_for_ai
from ai_markov import MOVES


def test_score_for_ai_all_outcomes():
    # Draws
    assert score_for_ai("R", "R") == 0
    assert score_for_ai("P", "P") == 0
    assert score_for_ai("S", "S") == 0

    # AI wins
    assert score_for_ai("R", "S") == 1
    assert score_for_ai("P", "R") == 1 
    assert score_for_ai("S", "P") == 1  

    # AI loses
    assert score_for_ai("R", "P") == -1
    assert score_for_ai("P", "S") == -1
    assert score_for_ai("S", "R") == -1


def test_multiai_best_ai_index_picks_highest_sum():
    ai = MultiAI(focus_length=5)

    ai.scores = [
        [1, -1, 0],   
        [2, 1],       
        [-1, -1, 0],  
        [],           
        [0, 0, 0],    
    ]

    best_index = ai._best_ai_index()
    assert best_index == 1


def test_multiai_best_ai_index_respects_focus_length_window():
    ai = MultiAI(focus_length=2)

    ai.scores = [
        [1, 1, 1, -1, -1],  
        [0, 0, 1, 1],      
        [1],               
        [],                
        [0, -1, 0],        
    ]

    best_index = ai._best_ai_index()
    assert best_index == 1


def test_multiai_choose_move_returns_valid_move():
    ai = MultiAI()
    move = ai.choose_move()
    assert move in MOVES


def test_multiai_update_updates_all_scores_and_keeps_lengths_in_sync():
    ai = MultiAI()

    move = ai.choose_move()
    assert move in MOVES

    ai.update("R")

    for score_history in ai.scores:
        assert len(score_history) == 1


def test_multiai_dynamic_best_ai_selection_with_dummy_ais():

    class DummyAI:
        def __init__(self, move):
            self.move = move
            self.updated_with = []

        def choose_move(self):
            return self.move

        def update(self, player_move: str):
            self.updated_with.append(player_move)

    ai = MultiAI(focus_length=3)

    dummy_ais = [
        DummyAI("R"),
        DummyAI("P"),
        DummyAI("S"),
    ]
    ai.single_ais = dummy_ais
    ai.scores = [
        [], 
        [], 
        [],  
    ]
    ai.last_moves = ["R", "P", "S"]

    ai.scores[0] = [1, 1]
    ai.scores[1] = [0, 0] 
    ai.scores[2] = [-1, -1]  

    move = ai.choose_move()
    assert move == "R"

    ai.scores[0] = [0, 0] 
    ai.scores[1] = [1, 1, 1]
    ai.scores[2] = [0, -1, 0] 

    move = ai.choose_move()
    assert move == "P"

    ai.update("R")
    for d in dummy_ais:
        assert d.updated_with == ["R"]

def test_multiai_all_ais_learn_some_transition_for_order_1():
    ai = MultiAI()

    for _ in range(5):
        ai.choose_move()
        ai.update("R")
        ai.choose_move()
        ai.update("P")

    order1_ai = None
    for single_ai in ai.single_ais:
        if single_ai.order == 1:
            order1_ai = single_ai
            break

    assert order1_ai is not None
    state = ("R",)
    assert order1_ai.transitions[state]["P"] >= 1
