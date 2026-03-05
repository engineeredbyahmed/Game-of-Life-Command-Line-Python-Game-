import pytest
from player import Player

def test_player_earn():
    p = Player("Ahmed")
    start = p.cash
    p.earn(600)
    assert p.cash == start + 600

def test_player_move_forward():
    p = Player("Ahmed")

    p.move(5, 25)

    assert p.position == 5
