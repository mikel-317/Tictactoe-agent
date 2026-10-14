# Tic-Tac-Toe AI

A Python implementation of Tic-Tac-Toe, built as a foundation for exploring artificial intelligence and reinforcement learning.

The project currently includes a playable game environment, a random agent that selects valid moves, and simulations of 1,000 games to analyse the outcomes. The next goal is to implement a Q-learning agent that can learn to play through experience.

## Features

- **Game environment:** A 3×3 Tic-Tac-Toe board implemented using NumPy.
- **Board representation:** Uses numerical values to represent the game state:
  - `1` — X
  - `-1` — O
  - `0` — Empty square
- **Move validation:** Identifies legal moves and prevents players from occupying filled squares.
- **Win detection:** Checks rows, columns and diagonals for a winning line.
- **Draw detection:** Recognises when the board is full and neither player has won.
- **Random agent:** Selects a random move from the available legal moves.
- **Automated simulations:** Runs 1,000 games between two random agents and records the number of X wins, O wins and draws.

## How It Works

The project separates the game environment from the agent.

The **environment** manages the board, tracks whose turn it is, validates moves and determines the outcome of each game.

The **random agent** observes the current game state and chooses one of the available legal moves. It does not plan ahead or learn from previous games.

Two random agents can play against each other automatically, allowing the results to be analysed over many games.

## Technologies

- Python
- NumPy
- `random` — Python's standard library

## Getting Started

### Requirements

Python 3 and NumPy.

Install NumPy using:

```bash
pip install numpy
```

### Running the Project

1. Clone this repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Navigate into the project directory:

   ```bash
   cd YOUR_REPOSITORY_NAME
   ```

3. Run the Python file containing the game and agent:

   ```bash
   python YOUR_FILENAME.py
   ```

Replace the placeholder names with your actual repository URL, directory name and Python filename.

## Learning Goals

This project is an opportunity to explore how an AI agent can make decisions, evaluate outcomes and improve its performance.

The random agent provides a baseline against which more intelligent strategies can be compared.

## Roadmap

- [x] Implement the Tic-Tac-Toe environment.
- [x] Add valid move generation and game-ending conditions.
- [x] Implement a random agent.
- [x] Simulate 1,000 games and record the results.
- [ ] Calculate and analyse win and draw rates.
- [ ] Implement tabular Q-learning from scratch.
- [ ] Train the learning agent through repeated self-play.
- [ ] Evaluate its performance against random play.
- [ ] Investigate whether the learned strategy approaches optimal play.

## Future Direction

The long-term goal is to develop an agent that learns effective strategies through reinforcement learning, rather than selecting moves randomly.

Q-learning will introduce state-action values
