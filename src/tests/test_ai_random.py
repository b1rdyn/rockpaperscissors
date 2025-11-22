from ai_random import random_move, MOVES


def test_random_move_returns_valid_moves():
    for _ in range(100):
        move = random_move()
        assert move in MOVES


def test_random_move_generates_all_moves_eventually():
    seen = set()
    for _ in range(300):
        seen.add(random_move())

    assert seen == set(MOVES)
