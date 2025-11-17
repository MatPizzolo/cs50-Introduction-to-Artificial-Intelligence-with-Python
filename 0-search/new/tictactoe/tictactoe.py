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


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    total_x = 0
    total_y = 0
    for row in board:
        for state in row:
            if state == X:
                total_x += 1
            elif state == O:
                total_y += 1

    if total_x > total_y:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    possible_actions = set()

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                possible_actions.add((i,j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]

    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)

    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
        # Check rows
    if all(i == board[0][0] for i in board[0]):
        return board[0][0]
    elif all(i == board[1][0] for i in board[1]):
        return board[1][0]
    elif all(i == board[2][0] for i in board[2]):
        return board[2][0]
    # Check columns
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]
    # Check diagonals
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    else:
        return None

def full_board(board):
    for row in board:
        for element in board:
            if element is not X and not O:
                return False

    return True

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or full_board(board) is not True:
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


def max_val(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board):
        aux, act = min_val(result(board, action))
        if aux > v:
            v = aux
            move = action
            if v == 1:
                return v, move
    return v, move

def min_val(board):
    if terminal(board):
        return utility(board), None

    v = float('+inf')
    move = None
    for action in actions(board):
        aux, act = max_val(result(board, action))
        if aux < v:
            v = aux
            move = action
            if v == -1:
                return v, move
    return v, move

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    pp = player(board)
    if pp == X:
        value, action = max_val(board)
        return action
    else:
        value, action = min_val(board)
        return action


