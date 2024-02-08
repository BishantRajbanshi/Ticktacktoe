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
    
