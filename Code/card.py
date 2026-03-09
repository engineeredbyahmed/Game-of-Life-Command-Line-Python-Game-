
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
    def __init__(self, description: str, amount: int):
        super().__init__(description)
        self.amount = amount

    def update_cash(self, player, change: int):
        print("Cash before:", player.cash)
        player.cash += change
        print(self.description)
        print("Cash after:", player.cash)


class MoveCard(Card):
    def __init__(self, description: str, steps: int):
        super().__init__(description)
        self.steps = steps

    def update_position(self, player, change: int):
        print("Position before:", player.position)
        player.position += change
        print(self.description)
        print("Position after:", player.position)


class Gift(CashCard):
    def apply(self, player):
        self.update_cash(player, self.amount)


class Ticket(CashCard):
    def apply(self, player):
        print(Style.color_text(self.description, Style.Red))
        print("Cash before:", player.cash)
        player.cash -= self.amount
        print("Cash after:", player.cash)


class Support(CashCard):
    def apply(self, player):
        self.update_cash(player, self.amount)


class Jump(MoveCard):
    def apply(self, player):
        self.update_position(player, self.steps)


class Fall(MoveCard):
    def apply(self, player):
        self.update_position(player, -self.steps)


class SkipTurn(Card):
    def apply(self, player):
        player.skip_turn = True
        print(self.description)