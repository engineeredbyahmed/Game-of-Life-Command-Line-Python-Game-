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
    def __init__(self):
        super().__init__("Start")

    def activate(self, game, player):
        print(player.name, "Just getting ready.")


class Payday(Space):
    def __init__(self):
        super().__init__("Payday")

    def activate(self, game, player):
        player.earn(1000)
        #print(player.name, "it is payday!. You earned 1000!")
        print(player.name, Style.color_text("it is payday!. You earned 1000!", Style.Green))

class Taxpay(Space):
    def __init__(self):
        super().__init__("Taxpay")

    def activate(self, game, player):
        player.pay(500)
        print(player.name, Style.color_text("You have to pay taxes. 500 is taken from you.", Style.Red))

        

class Empty(Space):
    def __init__(self):
         super().__init__("Empty")

    def activate(self, game, player):
        print(player.name, "Relax here")

class Event(Space):
    def __init__(self):
        super().__init__("Event")

    def activate(self, game, player):
        print("--- Event Card ---")
        print("Picking a card...")
        time.sleep(1.5)
        card = game.cards.draw()    
        print(card)                 
        card.apply(player)    

class Choice(Space):
    def __init__(self):
        super().__init__("Choice")

    def activate(self, game, player):
        print("--- Choice Space ---")
        print("Pick (1) if you want to invest in stocks (pay 600) with 50% chance to get 1000")
        print("Pick (2) if you want to gain 400 now")

        while True:
            try:
                option = int(input("Pick 1 or 2: ").strip())
                if option == 1:
                    player.pay(600)
                    print(player.name, " just paid 600 to invest")
                    if random.random() < 0.5:
                        player.earn(1000)
                        print(player.name, Style.color_text("You profited 1000!", Style.Green))
                        break
                    else:
                        print(player.name, Style.color_text("You just lost the 600 you invested", Style.Red))
                        break
                elif option == 2:
                    player.earn(400)
                    print(player.name, Style.color_text("You earned 400!", Style.Green))
                    break
                else:
                    print(player.name, "Invalid input. Please choose 1 or 2")
            except ValueError:
                print("Error: please enter a number 1 or 2")
                continue



class Retirement(Space):
    def __init__(self):
        super().__init__("Retirement")

    def activate(self, game, player):
        player.retire()
        print(player.name,"You have officially retired!")

    