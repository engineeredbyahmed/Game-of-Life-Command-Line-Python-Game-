import pytest

from deck import Deck

def test_deck():
    c = Deck(["Test Card 1", "Test Card 2", "Test Card 2"])

    start_size = len(c)

    c.draw()

    assert len(c) == start_size - 1



