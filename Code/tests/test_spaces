import pytest

from spaces import Retirement, Taxpay
from player import Player

def test_retirement():
    p = Player("Ahmed")

    Retirement().activate(None, p)

    assert p.retired is True


def test_Taxpay():
    p = Player("Ahmed")
    current = p.cash

    Taxpay().activate(None, p)

    assert p.cash == current - 500