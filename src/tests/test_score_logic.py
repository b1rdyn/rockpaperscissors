import pytest
from ai_multi import score_for_ai

@pytest.mark.parametrize(
    "ai_move, player_move, expected",
    [
        # draws
        ("R", "R", 0),
        ("P", "P", 0),
        ("S", "S", 0),

        # AI wins
        ("R", "S", 1),  
        ("P", "R", 1),  
        ("S", "P", 1),  

        # AI loses
        ("R", "P", -1),
        ("P", "S", -1),
        ("S", "R", -1),
    ],
)
def test_score_for_ai_all_outcomes(ai_move, player_move, expected):
    assert score_for_ai(ai_move, player_move) == expected
