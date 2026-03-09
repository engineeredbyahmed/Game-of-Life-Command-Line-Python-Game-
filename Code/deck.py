import random

class Deck:

    """
    This class contains Deck, and its methods. 

     Methods:
        __len__         To count the cards
        Shuffle         Mixing the cards to mimic real life board games
        Draw            So cards do not show twice and actually run out
        
    """

    def __init__(self, cards):
        self.cards = cards

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()