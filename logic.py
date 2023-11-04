# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    n = len(board)

    # horizontal
    for row in range(0, n):
        flag = True
        for column in range(0, n - 1):
            if board[row][column] is None or board[row][column] != board[row][column + 1]:
                flag = False
                break
        if flag:
            return {board[row][0]}

    # vertical
    for column in range(0, n):
        flag = True
        for row in range(0, n - 1):
            if board[row][column] is None or board[row][column] != board[row + 1][column]:
                flag = False
                break
        if flag:
            return board[0][column]

    # diagonal
    flag = True
    for i in range(0, n - 1):
        if board[i][i] is None or board[i][i] != board[i + 1][i + 1]:
            flag = False
            break
    if flag:
        return board[0][0]

    flag = True
    for i in range(0, n - 1):
        if board[n - 1 - i][i] is None or board[n - 1 - i][i] != board[n - 2 - i][i + 1]:
            flag = False
            break
    if flag:
        return board[0][n - 1]

    return None  # FIXME


def other_player(player):
    """Given the character for a player, returns the other player."""
    if player == 'X':
        return 'O'
    else:
        return "X"  # FIXME
