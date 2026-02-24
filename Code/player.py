class Player: 

    """
    This class contains players, their attributes, and methods. 
    
    """

    def __init__(self, name):
        self.name = name
        self.cash = 5000
        self.position = 0
        self.salary = 0 
        self.retired = False 

    def earn(self, amount):
        self.cash += amount

    def pay(self, amount):
        self.cash -= amount
    
    def move(self,steps):
        self.position += steps

    def retire(self):
        self.retired = True

    def balance(self):
        return self.cash

    




