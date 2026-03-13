import pytest

from deck import Deck

def test_deck():
    c = Deck(["Test Card 1", "Test Card 2", "Test Card 3"])

    start_size = len(c)

    c.draw()

    assert c is not None
    assert len(c) == start_size

