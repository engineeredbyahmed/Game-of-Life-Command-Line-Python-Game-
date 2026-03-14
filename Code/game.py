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
- [*] generate images, figures or diagrams.
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
# Importing all classes to the game loop
# ---------------------------------------------------------------------------
from player import Player
from dice import Dice
import spaces
from board import Board
from deck import Deck
import card
from Style import Style


# ---------------------------------------------------------------------------
# Importing all libraries to the game loop
# ---------------------------------------------------------------------------
from alive_progress import alive_bar
import time
from tabulate import tabulate
import pyfiglet
from faker import Faker
from halo import Halo
import sphinx
import random
import pyjokes

fake = Faker()
# to generate random name


class GameOfLife:


    """
    This class contains the whole game loop.

    it connects the players, board, spaces deck, cards, stylesrounds, user input,
    player turn, and declaring a winner.
    """


    MIN_PLAYERS = 2
    MAX_PLAYERS = 6
    ACTIONS = ("r", "p", "q", "h")

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
        self.jokes = pyjokes.get_jokes()
        random.shuffle(self.jokes)

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


    def get_next_joke(self):
        if not self.jokes:
            self.jokes = pyjokes.get_jokes()
            random.shuffle(self.jokes)
        return self.jokes.pop()

    # ---------------------------------------------------------------------------
    # User Input
    # This section include all user input for the game:
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
            action = input("Enter (r) to roll, (p) for game summary, (h) to show game history, or (q) to quit: ").strip().lower()
            if action in self.ACTIONS:
                return action
            print("Please choose one of the following: r, p, h, or q.")

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

        table_data1 = []
        for player in self.players:
            status = "Retired" if player.retired else "Playing"
            table_data1.append([player.name, player.cash, player.position, status])

        headers1 = ["Player", "Cash", "Position", "Status"]
        print(tabulate(table_data1, headers=headers1, tablefmt="fancy_grid"))

        table_data2 = []
        for player in self.players:
            row = [player.name]

            for space in ["Payday", "Taxpay", "Empty", "Event", "Choice"]:
                row.append(player.space_visits[space])

            table_data2.append(row)

        headers2 = ["Player", "Payday", "Taxpay", "Empty", "Event", "Choice"]


        print("Space Visit Summary")
        print(tabulate(table_data2, headers=headers2, tablefmt="fancy_grid"))

            
        print("----------------------------\n")

    def winner_announcement(self):

        """
        To declare the winner of the game.

        The player with highest cash is declared winner of the game.
        If two players have the same cash, the game announces is is
        a tie between them.
        """

        #Assumed the first player is always the winner to start with
        #Setting tie is false until told otherwise
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
        print("------- Game History -------")

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
        to show game summary of the game and declare winner immediately.
        """
        print(player.name, "Thank you for playing. Sad to see you go ):")
        self.summary()
        self.winner_announcement()

    def roll_move_activate(self, player: Player):
        """
        To roll the dice, move the player, and activate 
        the space where a player lands on.
        """ 

        # Used Halo library for fun effects 
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
        space_type = space.name
        player.space_visits[space_type] += 1
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

        # Each round retired players earn interest on their total cash
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
            # It returns True to continue the game
            if action == "r":
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






"""
          *** AI declaration ***
Gen AI used: ChatGPT
Prompt used:
"give me ideas on how to connect my classes of game of life hasbro in python without writting code. 
Players, cards, spaces, deck, board , and dice"
 
Output returned from GenAI:
Think of your program as one main game controller that manages everything.
Big picture
Game is the center.
It owns or controls:
Players
Board
Deck
Dice
Then:
Board is made of Spaces
Deck is made of Cards
So the structure is:
Game
→ has many Players
→ has one Board
→ has one Deck
→ has one Dice
Board
→ has many Spaces
Deck
→ has many Cards
That is the simplest and most logical design.
What each class is responsible for
1. Game
This should be the “manager” of the whole game.
It should know:
whose turn it is
when the game starts
when the game ends
how turns happen in order
when a player rolls the dice
when a player moves
what happens when they land on a space
when to draw a card
how to determine the winner
So the Game class does not do every detail itself, but it tells the other classes when to act.
You can think of it like the director of a movie.
2. Player
A Player represents one person in the game.
A player should store things like:
name
money / cash
current position on the board
job / life status if your version includes that
retirement state if relevant
any other personal game data
The player does not control the whole game.
It only stores and updates its own state.
So the player is more like:
“I am Ahmed, I have £5000, I’m on space 7, and I’m retired.”
3. Board
The Board is the path players move through.
It should:
contain all spaces in order
know how many spaces exist
help identify which space a player is standing on
help with movement around the track if needed
The board should not decide the whole turn.
It mainly represents the layout of the game world.
4. Space
A Space is one location on the board.
Examples:
Start
Payday
Event
Choice
Tax
Retirement
Each space should represent one type of landing action.
A good way to think about it:
The Board is the full road
A Space is one square on that road
When a player lands somewhere, the Game asks the board which space is there, and then that Space causes its effect.
5. Card
A Card is one event or instruction.
Examples:
receive money
lose money
move forward
move backward
special effect
A card should only represent one event and its impact.
So a card is not the whole deck, and not the whole game.
It is just one instruction object.
6. Deck
The Deck manages all cards.
It should:
hold the collection of cards
shuffle them
give one card when needed
possibly remove used cards if they should run out
possibly reset if empty, depending on your rules
So:
Card = one item
Deck = collection of card items
7. Dice
The Dice is simple.
It should only be responsible for:
generating a random roll
returning a valid dice number
That’s all.
It should not move the player directly.
It should not change money.
It should not control turns.
The Game uses the dice result to decide movement.
How the classes interact during a turn
A turn can be imagined like this:
Game selects the current Player
Game tells Dice to roll
Dice returns a number
Game updates the Player position
Game asks the Board which Space the player landed on
That Space triggers its effect
If the space requires a card:
Game asks Deck for a Card
the Card affects the Player
Game checks whether the game should continue
This is the cleanest flow.
Best relationship map
You can describe the relationships like this in your report or notebook:
Game has Players
Game has a Board
Game has a Deck
Game has a Dice
Board contains Spaces
Deck contains Cards
Player interacts with Board by moving across Spaces
Player interacts with Cards when drawing from the Deck
Dice provides movement value to the Game
Game coordinates all interactions
That already sounds strong and organized.
A useful mental model
Here is a very easy analogy:
Game = teacher running the classroom
Players = students
Board = classroom map
Spaces = desks/stations in the classroom
Deck = stack of instruction papers
Cards = one instruction paper
Dice = random number tool
The teacher controls the lesson, but the students, map, and papers each have their own role.
Composition idea
A strong OOP way to explain it is this:
Your design mostly uses composition.
Meaning:
a board is composed of spaces
a deck is composed of cards
a game is composed of players, board, dice, and deck
This is usually cleaner than putting all logic in one giant class.
Good separation of responsibility
A common mistake is making one class do too much.
A cleaner split is:
Game = controls flow
Player = stores player state
Board = stores path
Space = defines landing behavior
Deck = manages cards
Card = defines one event
Dice = gives random move value
That separation will make your design easier to explain in coursework.
If you want inheritance too
You can also structure Spaces and Cards using inheritance.
For example conceptually:
Space as a parent idea
StartSpace
PaydaySpace
EventSpace
TaxSpace
RetirementSpace
And:
Card as a parent idea
GiftCard
TicketCard
MoveForwardCard
MoveBackCard
Why this helps:
Each subtype has the same general purpose, but different behavior.
That makes your design more organized and more object-oriented.



Gen AI used: ChatGPT
Prompt used:
"how to declare winner in a simple way without writing code"
 
Output returned from GenAI:
The simplest way to think about declaring the winner is to treat it as a final comparison step after the game ends.
Instead of thinking about code, imagine it as a logical procedure.
1. Decide what determines the winner
In the Hasbro Game of Life, the winner is usually:
The player with the most money at the end of the game.
So your rule becomes:
Winner = player with the highest balance.
You only need one value to compare.
2. Wait until the game ends
You should only determine the winner after all players reach retirement (or after the game finishes according to your rules).
So the sequence conceptually is:
All players take turns.
Players eventually reach retirement.
The game finishes.
The winner is determined.
3. Compare all players' money
Now imagine you place all players on a table and look at their balances.
Example:
Player	Cash
Ahmed	12000
Michael	15000
Sarah	15000
You simply ask:
Who has the highest amount?
4. Handle two possible outcomes
Case 1 — One player has the highest balance
Example:
Player	Cash
Ahmed	12000
Michael	15000
Sarah	13000
Winner:
Michael
Case 2 — Two or more players have the same highest balance
Example:
Player	Cash
Ahmed	15000
Michael	15000
Sarah	13000
Then you declare:
Tie between Ahmed and Michael
5. Conceptual algorithm (no code)
The logic in plain language:
Assume the first player is the winner.
Check the next player.
If that player has more money, update the winner.
Continue checking every player.
If two players have the same highest value, mark it as a tie.
After checking everyone, announce the result.
6. Simple wording for your report
You could describe it like this:
At the end of the game, the balances of all players are compared. The player with the highest amount of money is declared the winner. 
If two or more players have the same highest balance, the game declares a tie.
That explanation is clear, simple, and academically acceptable.
7. Mental model
Think of it like a leaderboard at the end of a race:
Everyone finishes.
You check who has the highest score.
If two people have the same score → tie.



Gen AI used: ChatGPT
Prompt used:
"I'd like to implment a card where a player is punished by being forced to skip a turn. 
how would I do that without writing code for me"

Output returned from GenAI:
1. Give the player a state that can remember penalties
Your Player object should know whether they must miss a future turn.
Common ways:
a boolean like “skip next turn”
or a counter like “turns to skip”
The counter approach is usually better, because later you can support:
skip 1 turn
skip 2 turns
stack penalties
2. Let the card apply an effect to the player
The skip-turn card should not run the whole turn logic itself. Its job is only:
identify the player
update that player’s skip status
So conceptually, when the card is drawn, it changes something on the player such as:
“this player must skip 1 turn”
That keeps responsibilities clear:
card = applies effect
player = stores status
game loop = checks whether player can act
3. Check the penalty at the start of a turn
Before a player rolls or chooses an action, your turn system should ask:
Is this player supposed to skip?
If yes:
show a message
reduce the skip count
end their turn immediately
If no:
continue normally
That check belongs in the place that controls turns, not inside every individual action.
4. Decide exactly when the skip happens
You need one rule and stick to it:
Usually the best rule is:
player draws the punishment card now
they finish the consequence of drawing it
on their next turn, they lose the turn
That is clearer than making them lose the current turn halfway through.
5. Use wording that matches the mechanic
Be careful with the description:
“Skip your next turn” = one future turn lost
“Miss the next 2 turns” = counter becomes 2
That way the text matches the actual game behavior.
6. Keep it scalable
If you design it as a generic status effect, later you can easily add cards like:
move back 2 spaces
skip next turn
gain bonus next payday
protected from next tax
So think in terms of:
player has attributes/state
cards modify that state
turn system reads that state
A simple mental flow
It should behave like this:
Player lands on event/card space
Skip-turn card is drawn
Card marks player as needing to skip a future turn
Game continues normally
When that player’s next turn begins, the game detects the penalty
Their turn is skipped and the penalty is cleared or reduced

"""