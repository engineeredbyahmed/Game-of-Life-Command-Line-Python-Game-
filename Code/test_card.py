import pytest

from card import Gift
from player import Player
from game import GameOfLife

def test_card():
    c = Gift("test gift card", 250)

    p = Player("Ahmed")

    game = GameOfLife()

    current_cash = p.cash

    c.apply(p, game)

    assert p.cash == current_cash + 250

