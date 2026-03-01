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
                        spaces.Retirement()
                        ]
                        )
        

        self.cards = Deck([
            card.Gift("Gift from best friend (+250)", 250),
            card.Ticket("Speeding Ticket (-150)", -150),
            card.Support("Family Support (+500)", 500),
            card.Jump("You passed your exam. Move 2 extra steps", 2),
            card.Fall("You forgot to do laundry. Move 3 steps back" , 3)
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
                name = input(f"Name for player {i}: ").strip()

            p = Player(name)
            
            self.players.append(p)
            
        print("--" * 6)
        print("Welcome all")
        print("--" * 6)
        for players in self.players:
            print(players)

    
    def summary(self):
        print("------- Game Summary -------")
        print("Round:", self.round, "/", self.max_rounds)
        print("Board size:", self.Board.size())
        for players in self.players:
            if players.retired == True:
                print(players.name, "This player has retired")
            if players.retired == False:
                print(players.name, "This player is still playing")
            print("-", players.name, "| Cash:", players.cash) 
            print("Pos:", players.position, "| Salary:", players.salary)
        print("----------------------------\n")



    #-------------------------
    # Starting the Game (↓)
    #-------------------------

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
                
                action = input("Enter (1) to roll/n, (2) for game summary, or (3) to quit: ")


                if action == "1":
                    steps = Dice.roll()
                    print(f"{players.name} got {steps}!")
                    players.move(steps)
                    
                    #return self.print_summary()
                    

                if action == "2":
                    self.summary()
                    action_2nd = input("Enter (1) , (3) to quit: ")
                    if action_2nd == "3":
                        print(players.name, "Thank you for playing. Sad to see you go ):")
                        return self.print_summary()
                        
                if action == "3":
                    print(players.name, "Thank you for playing. Sad to see you go ):")
                    exit()

                
                space = self.Board.get_location(players.position) 
                space.activate(self, players)




    

game = GameOfLife()

game.Play()



