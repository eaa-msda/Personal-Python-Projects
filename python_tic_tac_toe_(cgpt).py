# -*- coding: utf-8 -*-
"""Python - Tic-Tac-Toe (CGPT)

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CNV4Zi0zj13j56nFZ3e6mY7yHIxamrAM
"""

# Errol Ian Ave Acosta
# Python (Personal)
# Tic-Tac-Toe Game Code for Google Colab (CGPT)
# 12 November 2024"



import random

# Initialize the board
def init_board():
    return [' ' for _ in range(9)]

# Display the board
def display_board(board):
    print(f"""
     {board[0]} | {board[1]} | {board[2]}
    ---|---|---
     {board[3]} | {board[4]} | {board[5]}
    ---|---|---
     {board[6]} | {board[7]} | {board[8]}
    """)

# Check for a win or tie
def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def check_tie(board):
    return ' ' not in board

# Make a move
def make_move(board, position, player):
    if board[position] == ' ':
        board[position] = player
        return True
    return False

# Get the computer's move
def computer_move(board):
    available_positions = [i for i, spot in enumerate(board) if spot == ' ']
    return random.choice(available_positions)

# Main game function
def tic_tac_toe():
    board = init_board()
    current_player = 'X'

    print("Welcome to Tic-Tac-Toe!")
    display_board(board)

    while True:
        if current_player == 'X':
            # Player's turn
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if move < 0 or move >= 9:
                    print("Invalid move. Choose between 1 and 9.")
                    continue
            except ValueError:
                print("Please enter a number.")
                continue

            if not make_move(board, move, 'X'):
                print("This position is already taken. Try another.")
                continue
        else:
            # Computer's turn
            move = computer_move(board)
            make_move(board, move, 'O')
            print(f"Computer chose position {move + 1}")

        display_board(board)

        # Check for win or tie
        if check_winner(board, current_player):
            print(f"{current_player} wins!")
            break
        elif check_tie(board):
            print("It's a tie!")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
tic_tac_toe()