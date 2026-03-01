
class Cards:
    def __init__(self, description):
        self.description = description  

    def __str__(self):
        return f"{self.description}"


class Gift(Cards):
    def __init__(self,description, amount):
        super().__init__(description)
        self.amount = amount

    def apply(self, player):
        print("Cash before:", player.cash)
        player.cash += self.amount 
        print(self.description)
        print("Cash after:", player.cash)


class Ticket(Cards):
    def __init__(self,description, amount):
        super().__init__(description)
        self.amount = amount

    def apply(self, player):
        print("Cash before:", player.cash)
        player.cash -= self.amount 
        print(self.description)
        print("Cash after:", player.cash)

class Support(Cards):
    def __init__(self,description, amount):
        super().__init__(description)
        self.amount = amount

    def apply(self, player):
        print("Cash before:", player.cash)
        player.cash += self.amount 
        print(self.description)
        print("Cash after:", player.cash)


class Jump(Cards):
    def __init__(self,description, steps):
        super().__init__(description)
        self.steps = steps

    def apply(self, player):
        print("Position before:", player.postion)
        player.postion += self.steps 
        print(self.description)
        print("Position after:", player.postion)


class Fall(Cards):
    def __init__(self,description, steps):
        super().__init__(description)
        self.steps = steps

    def apply(self, player):
        print("Position before:", player.postion)
        player.postion -= self.steps 
        print(self.description)
        print("Position after:", player.postion)

class Skip_Turn(Cards):
    def __init__(self,description):
        super().__init__(description)
    

    def apply(self, player):
        player.skip = True
        print(self.description)
        print(player.name, "is punished by forced to miss this turn")