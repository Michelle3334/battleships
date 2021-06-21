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
