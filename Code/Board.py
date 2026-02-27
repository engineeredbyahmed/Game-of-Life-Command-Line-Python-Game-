class Board:
    def __init__(self,total_spaces):
        self.total_spaces = total_spaces

    def size(self):
        return len(self.total_spaces)
    
    def get_location(self,position):
        while position >= self.size():
            position -= self.size()
        return self.total_spaces[position]

