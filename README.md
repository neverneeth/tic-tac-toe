# Tic-Tac-Toe

A Python-based Tic-Tac-Toe game for single-player and two-player modes, featuring a saving and loading system and variable difficulty levels.

---

## Project Description

This Tic-Tac-Toe game allows players to:
- Play against a computer (single-player) with two difficulty levels: Easy and Medium.
- Compete against another player in a two-player mode.
- Save game progress and resume at any time.

The game provides an intuitive interface, ensures valid moves, and includes a mechanism to block winning moves in the Medium difficulty level.

---

## Features Implemented

- **Game Modes:**
  - Single-player mode with Easy and Medium difficulties.
  - Two-player mode.

- **Saving and Loading:**
  - Save game state to a file.
  - Load and resume a saved game.

- **Game Logic:**
  - Win detection for rows, columns, and diagonals.
  - Computer AI to make random moves (Easy) or block opponent's winning moves (Medium).

- **Error Handling:**
  - Invalid input detection.
  - Prevention of overwriting filled positions.

---

## How to Run the Project

1. Clone or download the repository to your local machine.
2. Ensure Python 3.6 or higher is installed.
3. Run the `main.py` file to start the game:
   ```bash
   python main.py
   ```
4. Follow the on-screen instructions to choose a game mode and difficulty level.

---

## Installation Instructions

1. **Prerequisites:**
   - Python 3.6 or higher.

2. **Steps:**
   - Clone the repository:
     ```bash
     git clone https://github.com/neverneeth/tic-tac-toe.git
     ```
   - Navigate to the project directory:
     ```bash
     cd tic-tac-toe
     ```
   - Run the game:
     ```bash
     python main.py
     ```

---

## Instructions for Playing

1. **Controls:**
   - Enter a number between 1-9 to place your mark on the grid.
   - Save progress anytime by entering 'S'.

2. **Game Rules:**
   - A player wins by forming a row, column, or diagonal of their mark ('O' or 'X').
   - The game ends in a draw if the grid is full with no winner.

---

## Future Enhancements

- Add a "Hard" difficulty level with advanced AI strategies.
- Improve user interface with a graphical display using libraries like `tkinter` or `pygame`.
- Enable multiplayer mode over a network.

---

Enjoy playing Tic-Tac-Toe!

