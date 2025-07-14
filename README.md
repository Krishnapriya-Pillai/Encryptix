# Encryptix
Recommendation system: Implement an AI agent that plays the classic game of Tic-Tac-Toe against a human player. You can use algorithms like Minimax with or without Alpha-Beta Pruning to make the AI player unbeatable. This project will help you understand game theory and basic search algorithms.

Player 1 (user) - makes the first move
Player 2 (AI) - makes moves following the player 1

Uses Minimax algorithm to make the best possible move

The Minimax algorithm is a recursive algorithm that simulates all the possible future moves and choses to move with the best score. The score outcomes are:
 - AI win = +10
 - Human win = -10
 - Draw = 0

The best move is made by:
 - scanning all available squares.
 - applying the Minimax algorithm
chooses the best scoring move for the AI

After each move:
 - Checks for win, lose or draw
 - updates display accordingly: if human wins - green, if AI wins - red and if draw - grey
