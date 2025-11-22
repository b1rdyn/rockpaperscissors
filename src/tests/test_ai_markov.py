from ai_markov import counter_move, MarkovSingleAI, MOVES


def test_counter_move_basic_mapping():
    assert counter_move("R") == "P"
    assert counter_move("P") == "S"
    assert counter_move("S") == "R"


def test_counter_move_none_returns_valid_move():
    move = counter_move(None)
    assert move in MOVES


def test_markov_single_ai_updates_transitions():
    ai = MarkovSingleAI(order=1)
    ai.update("R")
    ai.update("P")
    state = ("R",)
    assert ai.transitions[state]["P"] == 1


def test_markov_single_ai_learns_repeated_move():
    ai = MarkovSingleAI(order=1)
    for _ in range(5):
        ai.update("R")
    move = ai.choose_move()
    assert move == "P"
