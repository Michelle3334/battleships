import random


rows = 0
columns = 0
board = []
ship_row = 0
ship_column = 0
turns = 0


"""
Welcome message
"""
print("Welcome to battleships!")


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
        print("You hit the battleship! Congratulations!\n")

    elif (board[row_guess-1][column_guess-1] == "X"):
        print("\nYou guessed that already.")

    else:
        print("\nYou missed the ship.")
        update_miss(board, row_guess, column_guess)
        display_board(board, rows, columns)

if (turns >= 5):
    print("\nSorry, You ran out of bombs and failed to sink the ship. :-(")
