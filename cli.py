# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board
from logic import other_player
from logic import get_winner

# Reminder to check all the tests

board_num = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

def print_board(input_board):
    """
    print board
    :param input_board: the input board need to be print
    :return: None
    """
    for row in input_board:
        print(row)
    
if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    current_player = 'X'
    count = 0
    print("The board location is represented by the number from 1 - 9:")
    print_board(board_num)
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

            if location.isdecimal() and 1 <= int(location) <= 9:
                location  = int(location)
                if board[(location - 1) // 3][(location - 1) % 3 ] is not None:
                    print(f'Location {location} has already been processed, please use availd one.')
                else:
                    is_valid = True
                    # update the board
                    board[(location - 1) // 3][(location - 1) % 3] = current_player
            else:
                print('The input is not valid, Please try again.')
                
        # Next plsyer
        current_player  = other_player(current_player)
        winner = get_winner(board)
        count += 1

    if winner is None:
        print('The board is full and there is no winner. Draw Game')
    else:
        print(f'Winner is {winner}!')
        print('Here is the result board:')
    print_board(board)

