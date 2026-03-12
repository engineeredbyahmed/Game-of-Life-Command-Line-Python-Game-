import random
import time 


class Dice:
    """
    This class is used to roll a 6-sided die

    Methods:
    @staticmethod   

    The reason for this design choice:

    (1) Only one dice used for the game.
        There is no need to create an instance 
        of the dice
        
    """

    @staticmethod
    def roll():
        return random.randint(1,6)
    

