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
from deck import Deck
import card
from Style import Style

import time
import random
from tabulate import tabulate

class GameOfLife:

    def __init__(self):
        self.players = []
        self.round = 0
        self.max_rounds = 25

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
                        spaces.Event(),
                        spaces.Retirement()
                        ]
                        )
        

        self.cards = Deck([
            card.Gift("Gift from best friend (+250)", 250),
            card.Ticket("Speeding Ticket (-150)", 150),
            card.Support("Family Support (+500)", 500),
            card.Jump("You passed your exam. Move 2 extra steps", 2),
            card.Fall("You forgot to do laundry. Move 3 steps back" , 3),
            card.Skip_Turn("You are punished by being forced to miss this turn")
        ]
)
        self.cards.shuffle()


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
                name = input(f"Name for player {i}: ").strip().capitalize()

            player = Player(name)
            
            self.players.append(player)
            
        print("--" * 6)
        print(Style.color_text("Wellcome All to the Game Of Life!", Style.B_White))
        print("--" * 6)
        for players in self.players:
            print(players)
        
    
    def summary(self):
        print("------- Game Summary -------")
        print("Round:", self.round, "/", self.max_rounds)
        print("Board size:", self.Board.size())
        print()

        table_data = []

        for player in self.players:
            status = "Retired" if player.retired else "Playing"

            table_data.append([
                player.name,
                player.cash,
                player.position,
                status
            ])

        headers = ["Player", "Cash", "Position", "Status"]

        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
        print("----------------------------\n")

    def winner_announcement(self):
        
        winner = self.players[0]
        tie = False
        

        for player in self.players[1:]:
            if player.balance() > winner.balance():
                winner = player
                tie = False
                
                
            elif player.balance() == winner.balance():
                 tie = True
                
        
        if tie:
            print("It's a tie with cash:", winner.balance())
        else:
            print("Winner:", winner.name, "with cash:", winner.balance())
        
                 
        
            
        

    #-------------------------
    # Starting the Game (↓)
    #-------------------------

    def Play(self):
        
        self.players_signup()

        while True:
            self.round += 1
            print(f"\n--- Round {self.round} ---")

            for player in self.players:
                if player.retired:
                    continue

                if player.skip_turn:
                        print(player.name)
                        continue
                

                while True:
                        print("--" * 6)
                        print(
                            f"Player turn: {player.name}, owns £{player.cash} "
                            f"and standing on position {player.position}"
                        )
                        
                        action = input("Enter (e) to roll, (p) for game summary, or (q) to quit: ").strip().lower()

                        if action == "p":
                            self.summary()
                            continue   

                        elif action == "q":
                            print(player.name, "Thank you for playing. Sad to see you go ):")
                            return self.summary(), self.winner_announcement() 
                                                    
                        
                            
                        elif action == "e":
                            print("Rolling dice...")
                            time.sleep(1.5)
                            steps = Dice.roll()
                            
                            print(f"{player.name} got {steps}!")
                            print("--" * 6)
                            player.move(steps,self.Board.size())

                            space = self.Board.get_location(player.position)
                            space.activate(self,player)
                            break     

                        else:
                            print("Please choose one of the following e, p, or q.")
                        
            if self.round >= self.max_rounds:
                break

            if all(player.retired for player in self.players):
                break

        print("------- Game Over -------")
        self.summary()
        self.winner_announcement()



    

game = GameOfLife()

game.Play()



