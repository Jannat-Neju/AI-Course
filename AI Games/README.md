# AI Games

This folder contains all the AI games code. (Chess, Tik tac toe, Connect Four)


# ♟️ Chess (AI vs Human)

This is a simple Chess game where the user plays against an AI opponent. The AI uses classic game-tree search algorithms to make intelligent decisions.

---

## ✅ How to Run

Make sure you have Python and `pygame` installed on your system.

```bash
python chess.py
🔧 Requirements
📦 Software & Libraries:
Python 3.x

pygame

##💡 Installation:
If pygame is not installed, you can install it with:

bash
Copy
Edit
pip install pygame


##🕹️ How to Play
You play as White.

Use your mouse to click on a piece and then click the destination square to move.

The AI (Black) will calculate and perform its move automatically.

The game continues until a checkmate, stalemate, or draw occurs.

Standard chess rules apply.


##📸 Screenshot
 chess_screenshot.png



##🤖 Algorithm Used
🧠 Min-Max Algorithm with Alpha-Beta Pruning
The AI simulates several possible future game states using the Min-Max algorithm.

Alpha-Beta Pruning optimizes the search by eliminating branches that don’t need to be evaluated.

This allows the AI to make smarter moves without unnecessary calculations.





#❌⭕ Tic Tac Toe (AI vs Human)

A classic Tic Tac Toe game where the player competes against an AI that plays optimally using the Min-Max algorithm.

---

## ✅ How to Run

Make sure Python and `pygame` are installed.

```bash
python tictactoe.py
🔧 Requirements
📦 Software & Libraries:
Python 3.x

pygame

##💡 Installation:
Install pygame using pip:

bash
Copy
Edit
pip install pygame


##🕹️ How to Play
You play as X.

The AI plays as O.

Click on a cell to place your X.

The AI will automatically respond with the optimal move.

First player to align three of their marks horizontally, vertically, or diagonally wins.

If the board is full and no one has won, the game is a draw.


##📸 Screenshot
tictactoe_screenshot.png.



##🤖 Algorithm Used
🧠 Min-Max Algorithm
The AI simulates every possible game state and chooses the move that maximizes its chance of winning (or minimizes your chance).

It's an unbeatable AI — always playing the best move.





# 🔴🟡 Connect 4 (AI vs Human)

A strategic Connect 4 game where the player plays against a computer-controlled opponent using Min-Max with heuristic evaluation.

---

## ✅ How to Run

Make sure Python and required libraries are installed.

```bash
python connect4.py
🔧 Requirements
📦 Software & Libraries:
Python 3.x

pygame

numpy

##💡 Installation:
Install dependencies using pip:

bash
Copy
Edit
pip install pygame numpy


##🕹️ How to Play
You play as RED, the AI plays as YELLOW.

Click on a column to drop your disc.

The first to connect 4 discs in a row (horizontally, vertically, or diagonally) wins.

If the board fills up with no winner, it’s a draw.

##📸 Screenshot
connect4_screenshot.png.


##🤖 Algorithm Used
🧠 Min-Max Algorithm with Heuristic Evaluation
The AI uses the Min-Max algorithm to simulate future moves.

A heuristic evaluation function scores non-terminal board states based on opportunities to win.

In larger depths, Alpha-Beta Pruning can be applied to reduce unnecessary computation.


