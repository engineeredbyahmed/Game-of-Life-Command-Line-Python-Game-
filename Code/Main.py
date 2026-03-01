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
from dice import Dice
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
                num_players = int(input("How many people are playing today? (2-6 players): ").strip())
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
            
            self.players += 1
            
        print("--" * 6)
        print("Welcome all")
        print("--" * 6)
        for players in self.players:
            print(players)

    def Play(self):
        self.players_signup()

        while True:
            self.round += 1
            print(f"\n--- Round {self.round} ---")

            for players in self.players:

                print(
                        f"Player turn: {players.name}, owns {players.cash} "
                        f"and standing on position {players.position}"
                            )   
                
                action = input("Enter (1) to roll/n, (2) for game summary, or (3) to quit")

                steps = Dice.roll()
                print(f"{players.name} got {steps}!")
                players.move(steps)
                
                space = self.Board.get_location(players.position) 
                space.activate(self, players)




    

game = GameOfLife()

game.Play()



