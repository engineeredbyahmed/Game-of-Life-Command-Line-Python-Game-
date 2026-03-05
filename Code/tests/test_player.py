import pytest
from player import Player

def test_player_earn():
    p1 = Player("Ahmed")
    p2 = Player("Bayan")
    current_p1 = p1.cash
    current_p2 = p2.cash
    p1.earn(600)
    p2.earn(1000)
    assert p1.cash == current_p1 + 600
    assert p2.cash == current_p2 + 1000

def test_player_move_forward():
    p = Player("Ahmed")
    p.move(5, 25)
    assert p.position == 5

def test_player_pay():
    p = Player("Ahmed")
    current = p.cash
    p.pay(600)
    assert p.cash == current - 600