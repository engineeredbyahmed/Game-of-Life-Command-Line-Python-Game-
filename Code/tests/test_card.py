import pytest

from card import Gift
from player import Player

def test_card():
    c = Gift("test gift card", 250)

    p = Player("Ahmed")

    current_cash = p.cash

    c.apply(p)

    assert p.cash == current_cash + 250

