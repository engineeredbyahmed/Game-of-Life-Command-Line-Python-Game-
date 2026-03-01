
import random

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
        print(player.name, "is is payday!. You earned 1000!")

class Taxpay(Space):
    def __init__(self):
        super().__init__("Taxpay")

    def activate(self, game, player):
        player.pay(500)
        print(player.name, "You have to pay taxes. 500 is taken from you")

        

class Empty(Space):
    def __init__(self):
         super().__init__("Empty")

    def activate(self, game, player):
        print(player.name, "Relax here")

class Event(Space):
    def __init__(self):
        super().__init__("Event")

    def activate(self, game, player):
        card = game.cards.draw()    
        print("--- Event Card ---")
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
            option = input("Pick 1 or 2: ").strip()
            if option == "1":
                player.pay(600)
                print(player.name, " just paied 600 to invest")
                if random.random() < 0.5:
                    player.earn(1000)
                    print(player.name, "You profited 1000!")
                    break
                else:
                    print(player.name, "You just lost 1000")
            elif option == "2":
                player.earn(400)
                print(player.name, "You earned 400")
                break
            else:
                print(player.name, "Invalid input. Please choose 1 or 2")



class Retirement(Space):
    def __init__(self):
        super().__init__("Retirement")

    def activate(self, game, player):
        player.retire()

    