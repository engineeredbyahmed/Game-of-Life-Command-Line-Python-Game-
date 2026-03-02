from Style import Style

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
        print(Style.color_text(self.description,Style.Green))
        print("Cash after:", player.cash)


class Ticket(Cards):
    def __init__(self,description, amount):
        super().__init__(description)
        self.amount = amount

    def apply(self, player):
        print("Cash before:", player.cash)
        player.cash -= self.amount 
        print(Style.color_text(self.description,Style.Red))
        print("Cash after:", player.cash)

class Support(Cards):
    def __init__(self,description, amount):
        super().__init__(description)
        self.amount = amount

    def apply(self, player):
        print("Cash before:", player.cash)
        player.cash += self.amount 
        print("Cash after:", player.cash)


class Jump(Cards):
    def __init__(self,description, steps):
        super().__init__(description)
        self.steps = steps

    def apply(self, player):
        print("Position before:", player.position)
        print(self.description)
        player.position += self.steps 
        print("Position after:", player.position)


class Fall(Cards):
    def __init__(self,description, steps):
        super().__init__(description)
        self.steps = steps

    def apply(self, player):
        print("Position before:", player.position)
        player.position -= self.steps 
        print("Position after:", player.position)

class Skip_Turn(Cards):
    def __init__(self,description):
        super().__init__(description)
    

    def apply(self, player):
        player.skip_turn = True
        print(self.description)
       