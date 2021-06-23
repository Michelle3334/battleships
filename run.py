import random
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("battleships")

name = [""]
number = 0
rows = 0
columns = 0
board = []
ship_row = 0
ship_column = 0
turns = 0


"""
Welcome player
"""
name = input("Enter your name here:\n")


def update_sheet(data):
    """
    Update worksheet with new players name
    """
    players_name = SHEET.worksheet("players")
    players_name.append_row([data])


print(f"\nWelcome to battleships {name}.")


def get_number():
    """
    Get the last row in the sheet
    """
    number = len(SHEET.worksheet("players").get_all_values()) - 1
    print(f"You are player number: {number}. Let's play!")


"""
Request user to select grid size
"""
while True:
    try:
        rows = columns = int(input("\nPlease enter the grid size (4-9).\n"))
    except ValueError:
        print("\nThat is not a number! Try again")
    else:
        if 4 <= rows < 10:
            break
        else:
            print("\nInvalid number, please try again.")


def create_board(r, c):
    """
    Create game board
    """
    for _ in range(rows):
        row = []
        for _ in range(columns):
            row.append(" ")
        board.append(row)
    return board


def display_board(board, columns, rows):
    """
    Display the game board
    """
    column_names = '123456789'[:columns]
    print('  | ' + ' | '.join(column_names) + ' |')
    for number, rows in enumerate(board, 1):
        print(number, '| ' + ' | '.join(rows) + ' |')


"""
Random placement of ship on board
"""


def random_row(board):
    return random.randint(1, len(board) - 1)


def random_col(board):
    return random.randint(1, len(board[0]) - 1)


"""
Functions for updating game board for hit or miss
"""


def update_hit(board, row_guess, column_guess):
    board[row_guess-1][column_guess-1] = 'O'


def update_miss(board, row_guess, column_guess):
    board[row_guess-1][column_guess-1] = 'X'


"""
Function to update game board after running out
of bombs
"""


def final_board(board, ship_row, ship_column):
    board[ship_row-1][ship_column-1] = 'O'


def setup():
    """
    Run all the functions
    """
    update_sheet(name)
    get_number()
    create_board(rows, columns)
    display_board(board, columns, rows)
    global ship_row
    ship_row = random_row(board)
    global ship_column
    ship_column = random_col(board)


setup()


"""
Play the game
"""
while turns != 5:
    turns += 1
    while True:
        try:
            row_guess = int(input(
                f"Guess row: Enter number between 1 and {rows}\n")
            )
        except ValueError:
            print("\nThat is not a number! Try again")
        else:
            if 1 <= row_guess <= rows:
                break
            else:
                print("\nInvalid row number, please try again.")

    while True:
        try:
            column_guess = int(input(
               f"\nGuess column: Enter number between 1 and {columns}\n")
            )
        except ValueError:
            print("\nThat is not a number! Try again")
        else:
            if 1 <= column_guess <= columns:
                break
            else:
                print("\nInvalid column number, please try again.")

    if (row_guess == ship_row) and (column_guess == ship_column):
        update_hit(board, row_guess, column_guess)
        display_board(board, rows, columns)
        print(f"You hit the battleship! Congratulations {name}!\n")
        print("Click 'RUN PROGRAM' to play again")
        break

    elif (board[row_guess-1][column_guess-1] == "X"):
        print("\nYou guessed that already and wasted a bomb.")

    else:
        print("\nYou missed the ship.")
        update_miss(board, row_guess, column_guess)
        display_board(board, rows, columns)

if (turns >= 5):
    print(f"\nSorry {name} :-(")
    print("You ran out of bombs and failed to sink the ship.")
    print("See how close you were!")
    update_miss(board, row_guess, column_guess)
    final_board(board, ship_row, ship_column)
    display_board(board, rows, columns)
    print("Click 'RUN PROGRAM' to play again.")
