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


def check_for_draw(board):
    # develop cope to check if all cells are occupied
    # return True if it is, False otherwise
    for row in board:
        if ' ' in row:
            return False  # If there's an empty space, game is not a draw
    return not (check_for_win(board, 'X') or check_for_win(board, 'O'))  # If there's no empty space and no winner, it's a draw

        
def play_game(board):
    #Initializes the board
    board = initialise_board(board)
    while True:
        # Player's turn
        row, col = get_player_move(board)
        board[row][col] = 'X'
        draw_board(board)

        if check_for_win(board, 'X'):
            print("Congratulations! You win!")
            board = initialise_board(board)
            draw_board(board)
            return True  

        if check_for_draw(board):
            print("The game is a draw.")
            return False

        #Computer's turn
        row, col = choose_computer_move(board)
        while board[row][col] == 'X':  # Ensure computer does not overwrite player's move
            row, col = choose_computer_move(board)
        board[row][col] = 'O'
        draw_board(board) #Updated board

        if check_for_win(board, 'O'):
            print("Computer wins! Better luck next time.")
            return False

     
def menu():
    # get user input of either '1', '2', '3' or 'q'
    # 1 - Play the game
    # 2 - Save score in file 'leaderboard.txt'
    # 3 - Load and display the scores from the 'leaderboard.txt'
    # q - End the program

    print("1 - Play the game")
    print("2 - Save score in file 'leaderboard.txt'")
    print("3 - Load and display the scores from 'leaderboard.txt'")
    print("q - End the program")
    choice = input("Enter your choice: ")
    return choice

def load_scores():
    """
    Loads the leaderboard scores from the file.
    """
    if os.path.exists('leaderboard.txt'):
        with open('leaderboard.txt', 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print("Error: Unable to decode JSON from the file.")
                return {}
    else:
        print("Leaderboard file does not exist.")
        return {}

    
def save_score(score):
    """
    Saves the player's score to the leaderboard file.
    """
    name = input("Enter your name: ")
    scores = load_scores()
    scores[name] = score
    with open('leaderboard.txt', 'w') as file:
        json.dump(scores, file)
        print("Score saved successfully.")


def display_leaderboard(leaders):
    """
    Displays the leaderboard.
    """
    print("\nLEADERBOARD:")
    print("Name\tScore")
    for name, score in leaders.items():
        print(f"{name}\t{score}")
