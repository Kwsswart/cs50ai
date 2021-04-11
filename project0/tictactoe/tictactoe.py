"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def fake_state():
    """
    Returns starting state of the board.
    """
    return [[X, O, X],
            [X, O, O],
            [O, X, O]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    count = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != None:
                count += 1
    # First turn
    if board == initial_state():
        return X
    if count % 2 == 1:
        return O
    else: 
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    options = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] is None:
                options.add((i,j))

    return options


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # issue  "" TypeError: 'int' object is not subscriptable ""
    print(action)
    if action not in actions(board):
        raise Exception("Invalid Move")

    board_copy = copy.deepcopy(board)
    board_copy[action[0]][action[1]] = player(board_copy)

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    lines = [
        # Check rows
        [[0,0], [0,1], [0,2]],
        [[1,0], [1,1], [1,2]],
        [[2,0], [2,1], [2,2]],
        # Check diagonals
        [[0,0], [1,1], [2,2]],
        [[0,2], [1,1], [2,0]],
        # Check columns
        [[0,0], [1,0], [2,0]],
        [[0,1], [1,1], [2,1]],
        [[0,2], [1,2], [2,2]]
    ]
    for i in range(len(lines)):
        a, b, c = [lines[i][j] for j in range(len(lines[i]))]
        if board[a[0]][a[1]] and board[a[0]][a[1]] == board[b[0]][b[1]] and board[a[0]][a[1]] == board[c[0]][c[1]]:
            return board[a[0]][a[1]]
    return None
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if len(actions(board)) == 0:
        return True

    if winner(board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    maximum = float('-inf')
    minimum = float('inf')

    if player(board) == X:
        return max_val(board, maximum, minimum)[1]
    else:
        return min_val(board, maximum, minimum)[1]


def max_val(board, maximum, minimum):
    """
    Returns the max value of all possible actions
    """

    move = None

    if terminal(board):
        return [utility(board), None]

    v = float('-inf')

    for action in actions(board):
        check = min_val(result(board, action), maximum, minimum)[0]
        maximum = max(maximum, check)
        if check > v:
            v = check
            move = action
        '''if maximum > minimum:
            break'''

    return [v, move]


def min_val(board, maximum, minimum):
    """
    Returns the min value of all possible actions
    """

    move = None

    if terminal(board):
        return [utility(board), None]

    v = float('inf')

    for action in actions(board):
        check = max_val(result(board, action), maximum, minimum)[0]
        minimum = min(minimum, check)
        if check < v:
            v = check
            move = action
        '''if maximum < minimum:
            break'''

    return [v, move]