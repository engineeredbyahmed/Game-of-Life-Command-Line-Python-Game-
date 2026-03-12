
# Game of Life (Command-Line Pyth Game)

This project is a Python implementation of a simplified board game inspired by *The Game of Life*.  
The game allows 2 to 6 players to move across a board, draw cards, and interact with different spaces until the game ends and a winner is determined based on their final balance.

## Features

- Multiplayer gameplay
- Dice-based movement
- Different board spaces (events, taxes, payday, , taxes, payday,choices, retirement)
- Card system that affects player cash or position
- Player retirement and skip turns
- Game history tracking
- Game summary every round
- Winner and tie detection

## Project Structure

Code/

- main.py # Entry point of the game
- game.py # Main game logic and game loop
- player.py # Player class and player actions
- board.py # Game board structure
- spaces.py # Different types of board spaces
-  deck.py # Card deck management
-  card.py # Card types and effects
-  dice.py # Dice rolling logic
-  Style.py # Text formatting utilities

-  tests/ # Pytest test cases
-  docs/ # Sphinx documentation

## Requirements

Python 3.10+ recommended.

Install dependencies:
You will need to install 
requirements.txt
for the game to run correctly. 

## Running the Game

To run the game 
Please run main.py file

Follow the terminal instructions to:

- enter player names
- roll dice
- interact with spaces and cards
- continue until the game ends

---

## Testing

The project includes automated tests using **pytest**.

## Documentation

Project documentation is generated using **Sphinx**.

---

## Technologies Used

- Python
- Object-Oriented Programming
- Pytest (testing)
- Sphinx (documentation)

---

## Author

Ahmed Al-Dulaim  
MSc Data Science – University of Exeter
