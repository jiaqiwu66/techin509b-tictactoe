# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

import random

from logic import make_empty_board
from logic import other_player
from logic import get_winner
from logic import location_is_valid


# Reminder to check all the tests
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


class TicTacToc:
    board = None
    winner = None
    count = 0
    # define mode for single player
    is_single_player = None
    # X always be the first
    # O always be the second
    is_single_player_first = None
    player_1 = None
    player_2 = None
    bot = None

    NUMBER = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    WELCOME = """
      _______ _        _______           _______         
     |__   __(_)      |__   __|         |__   __|        
        | |   _  ___     | | __ _  ___     | | ___   ___ 
        | |  | |/ __|    | |/ _` |/ __|    | |/ _ \\ / _ \\
        | |  | | (__     | | (_| | (__     | | (_) |  __/
        |_|  |_|\\___|    |_|\\__,_|\\___|    |_|\\___/ \\___|  
    """

    def __init__(self):
        self.board = make_empty_board()
        self.count = 0
        self.winner = None

    def start_game(self):
        print(self.WELCOME)
        print("The board location is represented by the number from 1 - 9:")
        print_board(self.NUMBER)

    def chose_mode(self, mode):
        """
        choose game mode, single or 2-player
        """
        if int(mode) == 1:
            self.is_single_player = True
            print("Now you are at Single Players Mode. You'll playing against teh computer. Good luck!")
        else:
            self.is_single_player = False
            self.player_1 = 'X'
            self.player_2 = 'O'
            print("Now you are at Two Players Mode. Enjoy the game!")

    def player_priority(self, player_first):
        if player_first == 'n':
            self.is_single_player_first = False
            self.bot = 'X'
            self.player_1 = 'O'
            print("The bot will go first using X. Then the player's turn with O.")
        else:
            self.is_single_player_first = True
            self.player_1 = 'X'
            self.bot = 'O'
            print("You will go first using X. Then the bot goes with O.")

    def bot_step(self):
        available = []
        for row in range(0, 3):
            for col in range(0, 3):
                if game.board[row][col] is None:
                    available.append(row * 3 + col + 1)
        loc = random.choice(available)
        print(f"The bot puts on the location #{loc}")

        if self.is_single_player_first:
            self.board[(loc - 1) // 3][(loc - 1) % 3] = 'O'
        else:
            self.board[(loc - 1) // 3][(loc - 1) % 3] = 'X'


if __name__ == '__main__':
    game = TicTacToc()
    game.start_game()
    is_mode_valid = False
    while not is_mode_valid:
        input_mode = input("1. Single Player: Player VS Bot \n"
                           "2. Two Players: Player 1 VS 2 \n"
                           "Please choose the game mode: ")
        if input_mode.isdecimal() and 1 <= int(input_mode) <= 2:
            is_mode_valid = True
            game.chose_mode(input_mode)
            if game.is_single_player:
                player_choice = input("Do you want to go first (Y / n): ")
                game.player_priority(player_choice)
        else:
            print("Your input is invalid, please only input 1 or 2.")

    current_player = 'X'

    while game.winner is None and game.count < 9:
        print("The current board is:")
        print_board(game.board)
        game.count += 1
        if game.count % 2 == 1:
            print(f"Round {(game.count + 1) // 2}: ")

        # single player mode
        if game.is_single_player:
            if game.player_1 == current_player:
                is_valid = False
                while not is_valid:
                    location = input(f'Player {current_player}:please input the location (the number): ')
                    is_valid = location_is_valid(current_player, game.board, location)
            else:
                game.bot_step()

        # 2-player mode
        else:
            is_valid = False
            while not is_valid:
                location = input(f'Player {current_player}:please input the location (the number): ')
                is_valid = location_is_valid(current_player, game.board, location)

        # Next player
        current_player = other_player(current_player)
        game.winner = get_winner(game.board)

    if game.winner is None:
        print('The board is full and there is no winner. Draw Game')
    else:
        print(f'Winner is {game.winner}!')
        if game.is_single_player:
            if game.winner == game.player_1:
                print("Congratulation, you beat the bot!")
            else:
                print("Unfortunately, you lose the game. Try harder next time.")
    print('Here is the result board:')
    print_board(game.board)
