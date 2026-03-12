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
I used PlantUML to generate a UML Diagram that shows how classes relate to each other.
- [ ] I have not used any GenAI tools in preparing this assessment.
I declare that I have referenced all use of GenAI outputs within my assessment in line with the
University referencing guidelines.
I certify that all material in this dissertation which is not my own has been identified.
________________________________ End of declaration _______________________________

"""

# ---------------------------------------------------------------------------
# importing all classes to the game loop
# ---------------------------------------------------------------------------
from player import Player
from dice import Dice
import spaces
from board import Board
from deck import Deck
import card
from Style import Style


# ---------------------------------------------------------------------------
# importing all libraries to the game loop
# ---------------------------------------------------------------------------
from alive_progress import alive_bar
import time
from tabulate import tabulate
import pyfiglet
from faker import Faker
from halo import Halo
import sphinx


fake = Faker()

class GameOfLife:


    """
    This class contains the whole game loop.

    it connects the players, board, spaces deck, cards, stylesrounds, user input,
    player turn, and declaring a winner.
    """


    MIN_PLAYERS = 2
    MAX_PLAYERS = 6
    ACTIONS = ("e", "p", "q", "h")

    def __init__(self):
        """
        to initialize the game.

        it creates the player list, rounds, game history,
        board spaces, and it shuffles the cards deck.
        """
        self.players = []
        self.round = 0
        self.max_rounds = 25
        self.history = []

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
            card.Jump(Style.color_text("You passed your programming with python exam. Move 2 extra steps", Style.Green), 2),
            card.Fall(Style.color_text("You forgot to do laundry. Move 3 steps back", Style.Red), 3),
            card.SkipTurn(Style.color_text("You are punished by being forced to miss this turn", Style.B_Red))
        ])
        self.cards.shuffle()


    # ---------------------------------------------------------------------------
    # User Input
    # This section include all usuer input for the game:
    # (1) Number of players, (2) Name of PLayers, (3) Action during each game round
    # ---------------------------------------------------------------------------
    def get_num_players(self) -> int:
        """
        To get the number of players from the user.
        """
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

        """
        To format and standardize the player's name.

        Args:
        name (str): The name entered by the user.

        Returns:
        str: The name with no extra space and first letter capitalized.
        """
        return name.strip().capitalize()

    def get_player_name(self, i: int) -> str:
        """
        To get the name of players from the user.
        """
        while True:
            name = input(f"Name for player {i} or press F for a random name: ")
            if name.strip().lower() == "f":
                random_name = fake.first_name()
                print(f"Random name selected: {random_name}")
                return random_name
            
            if name == "":
                print("Name cannot be empty. Please insert a name.")
                continue

            name_formatted= self.format_player_name(name)

            if name_formatted:
                return name_formatted
            print("Name cannot be empty.")

    def get_action(self) -> str:
        """
        To get the action from the player.
    """
        while True:
            action = input("Enter (e) to roll, (p) for game summary, (h) to show game history, or (q) to quit: ").strip().lower()
            if action in self.ACTIONS:
                return action
            print("Please choose one of the following: e, p, h, or q.")

# ---------------------------------------------------------------------------
# Game initiation and termination
# This section includes 
# (1) game summary, (2) winner declaration, (3) loop for players signing up
#---------------------------------------------------------------------------    
    def players_signup(self):
        """
        To record all names of players and put them in a list alltogether.
        To show fun animation of the game loading.
        """
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
        """
        Shows the total game smmary of the current round
        (player name, cash, current postion, status)
        Used tabulate library to make stats more organized and clean
        """

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

        """
        To declare the winner of the game.

        The player with highest cash is declared winner of the game.
        If two players have the same cash, the game announces is is
        a tie between them.
        """

        #Assumed the first player is always the winner to start with
        #Sittign tie is false until told otherwise
        winner = self.players[0]
        tie = False

        #Started comparing other players in loop while not counting the first place
        # since the first player was already stated above
        for player in self.players[1:]: 
            if player.balance() > winner.balance():
                winner = player
                tie = False
            elif player.balance() == winner.balance():
                tie = True

        # This will print whenever two or more players have the same balance
        if tie:
            print("It's a tie with cash:", winner.balance())
        
        # This will print the winner with the highest cash
        # Using pyfiglet for fun text effect
        else:
            print(pyfiglet.figlet_format("Winner"))
            print(winner.name, "with cash:", winner.balance())


    def record_history(self,incident):
        """
        To record all history of the game each single round. 
        """
        self.history.append(incident)

    def show_history(self):
        """
        To display the history.
        """
        print("------- Game History ------")

        if not self.history:
            print("No incidents yet.")
            return
        for incident in self.history:
            print(incident)
            
# ---------------------------------------------------------------------------
# Turn logic
# This section includes
# (1) players status, (2) quitting the game, (3) rolling the dice (4) skip turn
# ---------------------------------------------------------------------------
    def print_turn_status(self, player: Player):
        """
        To display the player's stats each round.
        """
        print("--" * 6)
        print(
            f"Player turn: {player.name}, owns £{player.cash} "
            f"and standing on position {player.position}"
        )

    def handle_quit(self, player: Player):
        """
        if a player chooses (q) the game is terminated.
        to show game summary of the game and declare winner immediatel. 
        """
        print(player.name, "Thank you for playing. Sad to see you go ):")
        self.summary()
        self.winner_announcement()

    def roll_move_activate(self, player: Player):
        """
        To roll the dice, move the player, and activate 
        the space where a player lands on.
        """ 

        # Used Halo lirbrary for fun effects 
        # I made the Dice as a static method
        # because the player will only use one dice the whole game
        dice = Halo(text='Rolling dice...', spinner='dots')
        dice.start()
        time.sleep(1.5)
        dice.succeed("Dice rolled!")
        time.sleep(1.5)
        steps = Dice.roll()
        

        print(f"{player.name} got {steps}!")
        self.record_history(f"Round {self.round}: {player.name} got {steps}!")
        print("--" * 6)

        # The move method takes the steps and board size as inputs and returns player position
        # Space activation to apply effect on the player
        player.move(steps, self.Board.size())
        space = self.Board.get_location(player.position)
        space.activate(self, player)

    def take_turn(self, player: Player) -> bool:
        """
        To execute a full game round.
        Retired players gain interest.
        Punished players get to miss the current trun.

        Returns False if the game should end (player chose quit).
        Returns True if the game continues.
        """
        INTEREST = 0.07 # Defined the interest rate 

        # Each round retried players earn interest on their total cash
        # It returns True for the game to continue
        if player.retired:
            interest = int(player.cash * INTEREST)
            player.cash += interest
            print(player.name, "earned interest:", interest)
            self.record_history(f"Round {self.round}: {player.name} earned interest: {interest}")
            return True

        # important: reseting the skip turn to False
        # This makes the player skips one turn only
        if player.skip_turn:
            print(player.name, "is skipping this turn.")
            player.skip_turn = False
            return True

        while True:
            self.print_turn_status(player)
            action = self.get_action()

            # Using "continue" to go back to the top of the loop
            # everytime p is pressed 
            if action == "p":
                self.summary()
                continue 

            # Used a fun library to show some bars moving
            # it returns False in order to exit the game. 
            if action == "q":
                with alive_bar(5) as bar:
                    print("finishing the game...")
                    for _ in range(5):
                        time.sleep(0.5)
                        bar()
                self.handle_quit(player)
                return False

            if action == "h":
                self.show_history()
                continue

            # This runs the round loops
            # It reuterns True to continue the game
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
        """
        The first stage of game.

        The game ends on either by
        (1) Reaching maximum rounds.
        (2) When all players retire.
         """
        
        self.players_signup()

        while True:
            # to increase one round each loop
            self.round += 1

            print(Style.color_text(f"\n--- Round {self.round} ---", Style.B_White))

            # to give a round for each player
            # any player return False, the game exits straight away  
            for player in self.players:  
                if not self.take_turn(player): 
                    return  
                
            #The game finishes by these conditions below
            if self.round >= self.max_rounds:
                break
            # (1) When all 25 rounds finish
            # The game ends even if no one retired

            if all(p.retired for p in self.players):
                break
            # (2) When all players retire by reaching the end of the board

        print("------- Game Over -------")
        self.summary()
        self.winner_announcement()


