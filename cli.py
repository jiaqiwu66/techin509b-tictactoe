# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board
from logic import other_player
from logic import get_winner
from logic import location_is_valid


# Reminder to check all the tests

NUMBER = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

WELCOME = """
  _______ _ _      _______           _______
 |__   __(_) |    |__   __|         |__   __|
    | |   _| | __    | | __ _  ___     | | ___   ___
    | |  | | |/ /    | |/ _` |/ __|    | |/ _ \ / _ \\
    | |  | |   <     | | (_| | (__     | | (_) |  __/
    |_|  |_|_|\\_\\    |_|\\__,_|\\___|    |_|\\___/ \\___|
"""


def print_board(input_board):
    """
    print board
    :param input_board: the input board need to be print
    :return: None
    """
    for row in input_board:
        print("-------------")
        print("|", end='')
        for element in row:
            if element is None:
                print(f'   |', end='')
            else:
                print(f' {element} |', end='')
        print()
    print("-------------")


if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    current_player = 'X'
    count = 0
    print(WELCOME)
    print("The board location is represented by the number from 1 - 9:")
    print_board(NUMBER)
    while winner is None and count < 9:
        # print("TODO: take a turn!")
        # TODO: Show the board to the user.
        # TODO: Input a move from the player.
        # TODO: Update the board.
        # TODO: Update who's turn it is.
        print("The current board is:")
        print_board(board)
    
        is_valid = False
        while not is_valid:
            location = input(f'{current_player}:please input the location (the number): ')
            is_valid = location_is_valid(current_player, board, location)
                
        # Next player
        current_player = other_player(current_player)
        winner = get_winner(board)
        count += 1

    if winner is None:
        print('The board is full and there is no winner. Draw Game')
    else:
        print(f'Winner is {winner}!')
        print('Here is the result board:')
    print_board(board)
