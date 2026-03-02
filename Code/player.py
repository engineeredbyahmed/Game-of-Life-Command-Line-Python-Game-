class Player: 

    """
    This class contains players, their attributes, and methods. 

     Attributes:
        name            Player name
        cash            Starting money for the player
        position        All players will start from 0
        salary          When players get paid
        retired         When players retire (bool)
     Methods:
        earn            updating the cash as player earns money
        pay             updating the cash as player loses money
        move            updating position as player moves

    """

    def __init__(self, name):
        self.name = name
        self.cash = 5000
        self.position = 0
        self.salary = 0 
        self.skip_turn = False
        self.retired = False 

    def __str__(self):
        return f"{self.name}"

    def earn(self, amount):
        self.cash += amount

    def pay(self, amount):
        self.cash -= amount
    
    def move(self, steps, board_size):
        self.position += steps
        if self.position >= board_size - 1:
            self.position = board_size - 1
        if self.position < 0:
            self.position = 0

    def retire(self):
        self.retired = True
    
    def skip(self):
        self.skip_turn = True

    def balance(self):
        return self.cash

p1 = Player('Ahmed')





