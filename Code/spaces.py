import time
import random
from Style import Style


class Space:

    """
    This class serves as the parent class for all other spaces.
    Each subclass overrides the activate() method to define the specific behaviour. 
    The method gets applied when the player lands on that space.

     Attributes:

        name            Space name

     Methods:

        activate        Applying the effect of the space on the player                             

    """

    def __init__(self, name):
        self.name = name

    def activate(self,game, player):
        raise NotImplementedError("Subclasses must implement activate()")

    
class Start(Space):
    """ The space where all players start."""

    def __init__(self):
        super().__init__("Start")

    def activate(self, game, player):
        print(player.name, "Just getting ready.")


class Payday(Space):
    """The player receives 1000 when stepping on Payday space."""
    def __init__(self):
        super().__init__("Payday")

    def activate(self, game, player):
        print("Cash before:", player.cash)
        player.earn(1000)
        print(player.name, Style.color_text("it is payday!. You earned 1000!", Style.Green))
        print("Cash after:", player.cash)
        game.record_history(f"Round {game.round}: {player.name} earned 1000!")

class Taxpay(Space):
    """The player pays 500 when stepping on Taxpay space."""
    def __init__(self):
        super().__init__("Taxpay")

    def activate(self, game, player):
        print("Cash before:", player.cash)
        player.pay(500)
        print(player.name, Style.color_text("You have to pay taxes. 500 is taken from you.", Style.Red))
        print("Cash after:", player.cash)
        game.record_history(f"Round {game.round}: {player.name} lost 500 to pay taxes")



class Empty(Space):
    """The player does not not get or give anything on the empty space."""
    def __init__(self):
         super().__init__("Empty")

    def activate(self, game, player):
        print(player.name, "Nothing here. Just a moment to think about your life choices")
        print("Here is a joke for you while you wait: ")
        print(game.get_next_joke())
        game.record_history(f"Round {game.round}: {player.name} stepped on an empty space")

class Event(Space):
    """The player gets an event card picked up randomly on the event space."""
    def __init__(self):
        super().__init__("Event")

    def activate(self, game, player):
        print(Style.color_text("--- Event Space ---", Style.B_magenta))
        print("Picking a card...")
        time.sleep(1.5)
        game.record_history(f"Round {game.round}: {player.name} got an event card")
        card = game.cards.draw()                    
        card.apply(player, game)
        

class Choice(Space):
    """The player get to choose to take risk to invest or receive quick cash."""
    def __init__(self):
        super().__init__("Choice")

    def activate(self, game, player):
        print(Style.color_text("--- Choice Space ---", Style.B_blue))
        print("Pick (1) if you want to invest in stocks (pay 600) with 50% chance to get 1000")
        print("Pick (2) if you want to gain 400 now")

        while True:
            try:
                option = int(input("Pick 1 or 2: ").strip())
                if option == 1:
                    player.pay(600)
                    print(player.name, " just paid 600 to invest")
                    print("Investing in option trading for quick profit...")
                    time.sleep(1.5)
                    if random.random() < 0.5:
                        print("Cash before:", player.cash)
                        player.earn(1000)
                        print(player.name, Style.color_text("You profited 1000!", Style.Green))
                        print("Cash after:", player.cash)
                        game.record_history(f"Round {game.round}: {player.name} chose to invest and profited 1000")
                        break
                    else:
                        print(player.name, Style.color_text("You just lost the 600 you invested", Style.Red))
                        game.record_history(f"Round {game.round}: {player.name} chose to invest and lost 600")
                        break
                elif option == 2:
                    print("Cash before:", player.cash)
                    player.earn(400)
                    print(player.name, Style.color_text("You earned 400!", Style.Green))
                    print("Cash after:", player.cash)
                    game.record_history(f"Round {game.round}: {player.name} chose to earn 400 without investing")
                    break
                else:
                    print(player.name, "Invalid input. Please choose 1 or 2")
            except ValueError:
                print("Error: please enter a number 1 or 2")
                continue



class Retirement(Space):
    """The player retires when reaching the retirement space at the end of board."""
    def __init__(self):
        super().__init__("Retirement")

    def activate(self, game, player):
        player.retire()
        print(Style.color_text("You have officially retired!", Style.BOLD))
        game.record_history(f"Round {game.round}: {player.name} has officially retired")
        print(Style.color_text("You will gain 7% each round until other players finish", Style.Underline))

    