"""
________________________________ Start of declaration _______________________________
I acknowledge the following uses of GenAI tools in this assessment:
- [ ] I have used GenAI tools to:
- [*] develop ideas.
- [ ] assist with research or gathering information.
- [*] help me understand key theories and concepts.
- [ ] identify trends and themes as part of my data analysis
- [*] suggest a plan or structure for my assessment.
- [ ] give me feedback on a draft.
- [ ] generate images, figures or diagrams.
- [ ] proofread and correct grammar or spelling errors.
- [ ] generate citations or references.
- [ ] Other: [please specify]
- [ ] I have not used any GenAI tools in preparing this assessment.
I declare that I have referenced all use of GenAI outputs within my assessment in line with the
University referencing guidelines.
I certify that all material in this dissertation which is not my own has been identified.
________________________________ End of declaration _______________________________
"""

from player import Player
import dice
import spaces
from board import Board

class GameOfLife:

    def __init__(self):
        self.players = []
        self.round = 0

        self.Board = Board([spaces.Start(),
                        spaces.Empty(),
                        spaces.Event(),
                        spaces.Choice(),
                        spaces.Payday(),
                        spaces.Empty(),
                        spaces.Taxpay(),
                        spaces.Empty(),
                        spaces.Payday(),
                        spaces.Empty(),
                        spaces.Event(),
                        spaces.Choice(),
                        spaces.Payday(),
                        spaces.Empty(),
                        spaces.Taxpay(),
                        spaces.Empty(),
                        spaces.Payday(),
                        spaces.Event(),
                        spaces.Choice(),
                        spaces.Retirement()
                        ]
                        )


    def players_signup(self):
        while True:
            try:
                num_players = int(input("How many people are playing today?(2-6 players): ").strip())
                if 2<= num_players <=6 :
                    break
                else:
                     print('Only from 2 to 6 players are allowed')
            except ValueError:
                    raise ValueError('This is not a number. Please Enter a number.')
        
        for i in range(1, num_players + 1):
            name = []
            while name == []:
                name = input(f"Name for player {i}: ").strip()

            p = Player(name)
            
            self.players.append(p)

game = GameOfLife()

game.players_signup()


