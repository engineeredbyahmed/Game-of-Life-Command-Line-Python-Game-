import pytest


from board import Board
from spaces import Space

def test_board():
    Space = ["Empty", "Payday", "Choice"]
    board = Board(Space)

    result = board.get_location(1)

    assert result == "Payday"