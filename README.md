# ⭕❌ Tic-Tac-Toe AI: Minimax Algorithm

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Course](https://img.shields.io/badge/Course-3303%20Artificial%20Intelligence-brightgreen.svg)

A smart, unbeatable Tic-Tac-Toe game developed in Python as the final project for the **3303 - Artificial Intelligence** course. This project demonstrates the practical application of adversarial search algorithms in game theory, specifically utilizing the **Minimax algorithm** to create an AI opponent that never loses.

## 🧠 About the Project

This project explores decision-making in Artificial Intelligence. The goal was to build a computer agent capable of playing a perfect game of Tic-Tac-Toe. By predicting possible future moves and evaluating board states, the AI optimally chooses its next move to force a win or a draw, making it mathematically impossible to beat.

### ✨ Key Features
* **Unbeatable AI Opponent:** Implements the Minimax algorithm to evaluate all possible future game states.
* **Interactive Gameplay:** Play against the computer in a seamless terminal/GUI environment.
* **Optimized Decision Making:** Showcases core AI concepts like game trees, state evaluation, and utility functions.
* **Clean Code Architecture:** Modular Python script (`Tic_Tac_Toe.py`) designed for readability and efficiency.

## 🛠️ Technologies Used
* **Language:** Python 3.x
* **Core Concepts:** Game Theory, Minimax Algorithm, Recursion, Adversarial Search

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites
Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation & Execution
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/AnasAbdelraouf128/Tic_Tac_Toe-Game.git](https://github.com/AnasAbdelraouf128/Tic_Tac_Toe-Game.git)
🎮 How to Play
The game is played on a standard 3x3 grid.

You will play as X and the AI will play as O (or vice versa depending on the prompt).

Enter your move based on the coordinate/numbering system prompted on the screen.

Try to get 3 in a row (horizontal, vertical, or diagonal) before the AI does. (Spoiler: It won't let you!)

🔬 How the AI Works (Under the Hood)
The AI opponent is powered by the Minimax Algorithm. It generates a complete game tree traversing all possible moves until a terminal state is reached (Win, Lose, or Draw).

Maximizing Player: The AI tries to maximize its score (+10 for a win).

Minimizing Player: The AI assumes the human player will play optimally and tries to minimize the AI's score (-10 for a human win).

Result: The AI maps out the board, assigns a value to every possible move, and executes the move that yields the highest utility.

🎓 Acknowledgements
Developed as the final project for Course 3303 - Artificial Intelligence.

Created by Anas Abdelraouf.
