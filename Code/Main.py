
"""
To create an instance of the Game of Life. 

It imports the GameOfLife class
It uses Play() method to start the ga2me.
"""

from game import GameOfLife


def main():
    """to start the game."""
    game = GameOfLife()
    game.Play()


    """
    Added this condition so the game
    does not start when making the html file
    """
if __name__ == "__main__":
    main()