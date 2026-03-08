import pytest
from game import GameOfLife

@pytest.mark.parametrize("inputs, expected", [
    ("ahmed", "Ahmed"),
    (" bayan ", "Bayan"),
])

def test_get_player_name(inputs, expected):
    game = GameOfLife()
    
    assert game.format_player_name(inputs) == expected