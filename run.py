import random


rows = 0
columns = 0
board = []
turns = 0


"""
Welcome message
"""
print("Welcome to battleships!")


"""
Request user to select number of rows
"""
while True:
    try:
        rows = int(input("Please enter the number of rows (4-9).\n"))
    except ValueError:
        print("That is not a number! Try again")
    else:
        if 4 <= rows < 10:
            break
        else:
            print("Invalid number, please try again.")


"""
Request user to select number of columns
"""
while True:
    try:
        columns = int(input("Please enter the number of columns(4-9).\n"))
    except ValueError:
        print("That is not a number! Try again")
    else:
        if 4 <= columns < 10:
            break
        else:
            print("Invalid number, please try again.")


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


def setup():
    """
    Run all the functions
    """
    create_board(rows, columns)
    display_board(board, columns, rows)
    global ship_row
    ship_row = random_row(board)
    global ship_column
    ship_column = random_col(board)


setup()
