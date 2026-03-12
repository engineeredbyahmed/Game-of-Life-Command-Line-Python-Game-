
class Board:
    """
    This class containts base the board of the game.
    The board contains all spaces inside of it

     Methods:
        size          : return the total number of spaces
        get_location  : to get the position of the player on the board
    """

    def __init__(self,total_spaces):
        self.total_spaces = total_spaces

    def size(self):
        return len(self.total_spaces)
    
    def get_location(self,position):
        while position >= self.size():
            position -= self.size()
        return self.total_spaces[position]

