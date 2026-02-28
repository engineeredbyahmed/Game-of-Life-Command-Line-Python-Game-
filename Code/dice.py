import random


class Dice:
    """
    This class is used to roll a 6-sided die

    """
    @staticmethod
    def roll():
        return random.randint(1,6)
    

