
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
        pass

class Payday(Space):
    def __init__(self):
        super().__init__("Payday")

    def activate(self, game, player):
        player.earn(1000)

class Taxpay(Space):
    def __init__(self):
        super().__init__("Taxpay")

    def activate(self, game, player):
        player.pay(500)

        

class Empty(Space):
    def __init__(self):
         super().__init__("Empty")

    def activate(self, game, player):
        pass

class Event(Space):
    def __init__(self):
        super().__init__("Event")

    def activate(self, game, player):
        card = game.cards.draw()    
        print("--- EVENT CARD ---")
        print(card)                 
        card.apply(player)    

class Choice(Space):
    def __init__(self):
        super().__init__("Choice")

    def activate(self, game, player):
        pass

class Retirement(Space):
    def __init__(self):
        super().__init__("Retirement")

    def activate(self, game, player):
        pass

    