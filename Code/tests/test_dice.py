import pytest
from dice import Dice

def test_dice():
    result = Dice.roll()
    assert 1 <= result <= 6