import random
import os.path
import json
random.seed()

def draw_board(board):
    # develop code to draw the board
    print(" -----------")
    for i in range(3):
        print("|" + " " + board[i][0] + " | " + board[i][1] + " | " + board[i][2] + " " + "|")
        if i < 2:
            print(" -----------")
    print(" -----------")

def welcome(board):
    # prints the welcome message
    # display the board by calling draw_board(board)
    print('Welcome to the "Unbeatable Noughts and Crosses" game.')
    print('The board layout is shown below:')
    draw_board(board)
    

def initialise_board(board):
    # develop code to set all elements of the board to one space ' '
    return [[' ' for _ in range(3)] for _ in range(3)]
    
def get_player_move(board):
    # develop code to ask the user for the cell to put the X in,
    # and return row and col
    while True:
        try:
            move = int(input("Enter a number (1-9) to place 'X': "))
            row, col = divmod(move - 1, 3)
            if 1 <= move <= 9 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def choose_computer_move(board):
    # develop code to let the computer chose a cell to put a nought in
    # and return row and col
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    # Get a list of empty cells
    if empty_cells:
        # If there are empty cells, choose one randomly
        return random.choice(empty_cells)
    else:
        # If there are no empty cells, the board is full
        return None


def check_for_win(board, mark):
    # develop code to check if either the player or the computer has won
    # return True if someone won, False otherwise
    for i in range(3):
        if all(board[i][j] == mark for j in range(3)) or all(board[j][i] == mark for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == mark for i in range(3)) or all(board[i][2 - i] == mark for i in range(3)):
        return True
    return False

