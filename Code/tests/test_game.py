"""
________________________________ Start of declaration _______________________________
I acknowledge the following uses of GenAI tools in this assessment:
- [ ] I have used GenAI tools to:
- [*] develop ideas.
- [ ] assist with research or gathering information.
- [*] help me understand key theories and concepts.
- [ ] identify trends and themes as part of my data analysis
- [*] suggest a plan or structure for my assessment.
- [*] give me feedback on a draft.
- [ ] generate images, figures or diagrams.
- [ ] proofread and correct grammar or spelling errors.
- [ ] generate citations or references.
- [*] Other: [please specify]
I used GenAI to find bugs and debug my code. 
- [ ] I have not used any GenAI tools in preparing this assessment.
I declare that I have referenced all use of GenAI outputs within my assessment in line with the
University referencing guidelines.
I certify that all material in this dissertation which is not my own has been identified.
________________________________ End of declaration _______________________________

"""



import pytest
from game import GameOfLife
from player import Player

@pytest.mark.parametrize("inputs, expected", [
    ("ahmed", "Ahmed"),
    (" bayan ", "Bayan"),
])

def test_get_player_name(inputs, expected):
    game = GameOfLife()
    
    assert game.format_player_name(inputs) == expected



@pytest.mark.parametrize("action, expected", [
    ("E", "e"),
    (" P ", "p"),
    ("q", "q"),
])

def test_action(action, expected):

    result = action.strip().lower()
    assert result == expected


def test_take_turn_retired_player():
    game = GameOfLife()
    player = Player("Ahmed")
    player.retired = True

    result = game.take_turn(player)
    assert result is True


def test_summary(capsys): # I used capsys to capture the output

    game = GameOfLife()
    p1 = Player("Ahmed")
    p2 = Player("Bayan")

    p1.cash = 6000
    p2.cash = 5800

    game.players = [p1, p2]
    game.summary()

    captured = capsys.readouterr() 
    #This is to retreive all the printed from summary function

    assert "6000" in captured.out
    assert "5800" in captured.out
    # captured out is used to check if these numbers are in the output
