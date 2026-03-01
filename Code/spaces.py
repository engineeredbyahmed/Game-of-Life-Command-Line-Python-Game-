
class Space:

    def __init__(self, name):
        self.name = name

    def activate(self,GameOfLife, player):
        raise NotImplementedError("Subclasses must implement activate()")

    
class Start(Space):
    def __init__(self):
        super().__init__("Start")

    def activate(self, GameOfLife, player):
        pass

class Payday(Space):
    def __init__(self):
        super().__init__("Payday")

    def activate(self, GameOfLife, player):
        player.earn(1000)

class Taxpay(Space):
    def __init__(self):
        super().__init__("Taxpay")

    def activate(self, GameOfLife, player):
        player.pay(500)

        

class Empty(Space):
    def __init__(self):
         super().__init__("Empty")

    def activate(self, GameOfLife, player):
        pass

class Event(Space):
    def __init__(self):
        super().__init__("Event")

    def activate(self, GameOfLife, player):
        pass

class Choice(Space):
    def __init__(self):
        super().__init__("Choice")

    def activate(self, GameOfLife, player):
        pass

class Retirement(Space):
    def __init__(self):
        super().__init__("Retirement")

    def activate(self, GameOfLife, player):
        pass

    