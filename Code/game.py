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
I used ChatGBT to refractor the code to make it easier to understand.
I used GenAI to find bugs and debug my code. 
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


from alive_progress import alive_bar
import time
from tabulate import tabulate
import pyfiglet
from faker import Faker
from halo import Halo



fake = Faker()

class GameOfLife:
    MIN_PLAYERS = 2
    MAX_PLAYERS = 6
    ACTIONS = ("e", "p", "q")

    def __init__(self):
        self.players = []
        self.round = 0
        self.max_rounds = 25

        self.Board = Board([
            spaces.Start(),
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
        ])

        
        
        

        self.cards = Deck([
            card.Gift(Style.color_text("Gift from best friend (+250)", Style.Green), 250),
            card.Ticket(Style.color_text("Speeding Ticket (-150)", Style.Red), 150),
            card.Support(Style.color_text("Family Support (+500)", Style.Green), 500),
            card.Jump(Style.color_text("You passed your exam. Move 2 extra steps", Style.Green), 2),
            card.Fall(Style.color_text("You forgot to do laundry. Move 3 steps back", Style.Red), 3),
            card.Skip_Turn(Style.color_text("You are punished by being forced to miss this turn", Style.B_Red))
        ])
        self.cards.shuffle()


    # ---------------------------------------------------------------------------
    # User Input
    # This section include all usuer input for the game:
    # (1) Number of players, (2) Name of PLayers, (3) Action during each game round
    # ---------------------------------------------------------------------------
    def get_num_players(self) -> int:
        while True:
            raw = input(f"How many people are playing today? ({self.MIN_PLAYERS}-{self.MAX_PLAYERS} players): ").strip()
            try:
                num_players = int(raw)
            except ValueError:
                print("This is not a number. Please enter a number.")
                continue

            if self.MIN_PLAYERS <= num_players <= self.MAX_PLAYERS:
                return num_players

            print(f"Only from {self.MIN_PLAYERS} to {self.MAX_PLAYERS} players are allowed.")

    def format_player_name(self, name: str) -> str:
        return name.strip().capitalize()

    def get_player_name(self, i: int) -> str:
        while True:
            name = input(f"Name for player {i} or press F for a random name: ")
            if name.strip() == "f":
                random_name = fake.first_name()
                print(f"Random name selected: {random_name}")
                return random_name
        
            name_formatted= self.format_player_name(name)

            if name_formatted:
                return name_formatted
            print("Name cannot be empty.")

    def get_action(self) -> str:
        while True:
            action = input("Enter (e) to roll, (p) for game summary, or (q) to quit: ").strip().lower()
            if action in self.ACTIONS:
                return action
            print("Please choose one of the following: e, p, or q.")

# ---------------------------------------------------------------------------
# Game initiation and termination
# This section includes 
# (1) game summary, (2) winner declaration, (3) loop for players signing up
#---------------------------------------------------------------------------    
    def players_signup(self):
        num_players = self.get_num_players()

        for i in range(1, num_players + 1):
            name = self.get_player_name(i)
            self.players.append(Player(name))

        
        with alive_bar(5) as bar:
            print("Loading the game!")
            for i in range(5):
                time.sleep(0.5)
                bar()
        print("--" * 6)
        print(Style.color_text("Welcome All to the Game Of Life!", Style.B_White))
        print("--" * 6)
        for p in self.players:
            print(p)

    def summary(self):
        print("------- Game Summary -------")
        print("Round:", self.round, "/", self.max_rounds)
        print("Board size:", self.Board.size())
        print()

        table_data = []
        for player in self.players:
            status = "Retired" if player.retired else "Playing"
            table_data.append([player.name, player.cash, player.position, status])

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
            print(pyfiglet.figlet_format("Winner"))
            print(winner.name, "with cash:", winner.balance())
            
# ---------------------------------------------------------------------------
# Turn logic
# This section includes
# (1) players status, (2) quitting the game, (3) rolling the dice (4) skip turn
# ---------------------------------------------------------------------------
    def print_turn_status(self, player: Player):
        print("--" * 6)
        print(
            f"Player turn: {player.name}, owns £{player.cash} "
            f"and standing on position {player.position}"
        )

    def handle_quit(self, player: Player):
        print(player.name, "Thank you for playing. Sad to see you go ):")
        self.summary()
        self.winner_announcement()

    def roll_move_activate(self, player: Player):
        dice = Halo(text='Rolling dice...', spinner='dots', animation="bounce")
        dice.start()
        time.sleep(1.5)
        dice.succeed("Dice rolled!")
        time.sleep(1.5)
        steps = Dice.roll()

        print(f"{player.name} got {steps}!")
        print("--" * 6)

        player.move(steps, self.Board.size())
        space = self.Board.get_location(player.position)
        space.activate(self, player)

    def take_turn(self, player: Player) -> bool:
        """
        Returns False if the game should end (player chose quit).
        Returns True if the game continues.
        """
        if player.retired:
            return True

        if player.skip_turn:
            print(player.name, "is skipping this turn.")
            player.skip_turn = False
            return True

        while True:
            self.print_turn_status(player)
            action = self.get_action()

            if action == "p":
                self.summary()
                continue

            if action == "q":
                with alive_bar(5) as bar:
                    print("finishing the game...")
                    for _ in range(5):
                        time.sleep(0.5)
                        bar()
                self.handle_quit(player)
                return False

            if action == "e":
                try:
                    self.roll_move_activate(player)
                except Exception as e:
                    print("Error: Something unexpected happened:", e)
                    continue
                return True

    # ---------------------------------------------------------------------------
    # Game loop
    # This section uses all function above all together ro run the game
    # The game is terminated by either finishing the full 25 turns or quitting
    # ---------------------------------------------------------------------------
    def Play(self):
        self.players_signup()

        while True:
            self.round += 1

            print(Style.color_text(f"\n--- Round {self.round} ---", Style.B_White))

            for player in self.players:
                if not self.take_turn(player):
                    return  

            if self.round >= self.max_rounds:
                break

            if all(p.retired for p in self.players):
                break

        print("------- Game Over -------")
        self.summary()
        self.winner_announcement()


