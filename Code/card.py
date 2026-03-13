
"""
________________________________ Start of declaration _______________________________
I acknowledge the following uses of GenAI tools in this assessment:
- [ ] I have used GenAI tools to:
- [ ] develop ideas.
- [ ] assist with research or gathering information.
- [ ] help me understand key theories and concepts.
- [ ] identify trends and themes as part of my data analysis
- [ ] suggest a plan or structure for my assessment.
- [ ] give me feedback on a draft.
- [ ] generate images, figures or diagrams.
- [ ] proofread and correct grammar or spelling errors.
- [ ] generate citations or references.
- [*] Other: [please specify]
I used ChatGBT to refractor the code to make it easier to understand.
- [ ] I have not used any GenAI tools in preparing this assessment.
I declare that I have referenced all use of GenAI outputs within my assessment in line with the
University referencing guidelines.
I certify that all material in this dissertation which is not my own has been identified.
________________________________ End of declaration _______________________________

"""



from Style import Style


class Card:
    """
    This class containts base card class for all cards.
    All other cards inherit from the base class. 

    Methods:
        __str__ : return card description
        apply   : apply card effect to player
    """

    def __init__(self, description: str):
        self.description = description

    def __str__(self) -> str:
        return self.description

    def apply(self, player):
        raise NotImplementedError("Subclasses must implement apply().")


class CashCard(Card):
    """The parent class when receiving or losing cash."""
    def __init__(self, description: str, amount: int):
        super().__init__(description)
        self.amount = amount

    def update_cash(self, player, change: int):
        print("Cash before:", player.cash)
        player.cash += change
        print(self.description)
        print("Cash after:", player.cash)


class MoveCard(Card):
    """
    The parent class when getting a card that moves the
    player forward or backward.
    """
    def __init__(self, description: str, steps: int):
        super().__init__(description)
        self.steps = steps

    def update_position(self, player, change: int, game):
        print("Position before:", player.position)
        player.move(change, game.Board.size())
        print(self.description)
        print("Position after:", player.position)


class Gift(CashCard):
    """ The child class when receiving cash."""
    def apply(self, player, game):
        self.update_cash(player, self.amount)
        game.record_history(f"Round {game.round}: {player.name} got a gift from their best friend (+250)")


class Ticket(CashCard):
    """ The child class when losing cash."""
    def apply(self, player, game):
        print(Style.color_text(self.description, Style.Red))
        print("Cash before:", player.cash)
        player.cash -= self.amount
        print("Cash after:", player.cash)
        game.record_history(f"Round {game.round}: {player.name} got a speeding Ticket (-150)")


class Support(CashCard):
    """ The child class when receiving cash as well."""
    def apply(self, player, game):
        self.update_cash(player, self.amount)
        game.record_history(f"Round {game.round}: {player.name} got a family Support (+500)")


class Jump(MoveCard):
    """ The child class when moving forward."""
    def apply(self, player, game):
        self.update_position(player, self.steps, game)
        game.record_history(f"Round {game.round}: {player.name}  passed their programming with python exam. Moved 2 steps forward")


class Fall(MoveCard):
    """ The child class when moving backward."""
    def apply(self, player, game):
        self.update_position(player, -self.steps, game)
        game.record_history(f"Round {game.round}: {player.name} forgot to do laundry. Moved 3 steps backward")


class SkipTurn(Card):
    """ The class when a player is forced to skip one turn."""
    def apply(self, player, game):
        player.skip_turn = True
        print(self.description)
        game.record_history(f"Round {game.round}: {player.name} punished by being forced to miss this turn")