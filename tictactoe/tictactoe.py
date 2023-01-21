"""
Tic Tac Toe Player
"""

import math


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

def countXO(state):
    countX, countO = 0, 0
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j] == 'X':
                countX += 1
            if state[i][j] == "O":
                countO += 1
    return countX, countO

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX, countO = countXO(board)
    if countX == countO:
        return "X"
    return "O"
    raise NotImplementedError

def check_vertical(board):
    for i in range(3):
        #print(board[i][0], board[i][1], board[i][2])
        if board[0][i] == board[1][i] == board[2][i]:
            return True, board[0][i]
    return False, None

def check_horizontal(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return True, board[i][0]
    return False, None

def check_diagonal(board):
    if board[0][0] == board[1][1] == board[2][2] or board[2][0] == board[1][1] == board[0][2]:
        return True, board[1][1]
    return False, None


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_list = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action_list.append((i, j))


    return action_list
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    p = player(board)
    new_board = [[EMPTY for i in range(3)] for j in range(3)]

    for i in range(3):
        for j in range(3):
            new_board[i][j] = board[i][j]
    i, j = action
    if board[i][j] != None:
        raise Exception
    else:
        new_board[i][j] = p
    return new_board
   


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    if check_diagonal(board)[0]:
        return check_diagonal(board)[1]
    if check_horizontal(board)[0]:
        return check_horizontal(board)[1]
    if check_vertical(board)[0]:
        return check_vertical(board)[1]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    
    for i in range(3):
        if EMPTY in board[i]:
            return False
    return True


    
    raise NotImplementedError


    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    if winner(board) == "O":
        return -1
    return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        v = -5
        for action in actions(board):
            minval = min_value(result(board, action))[0]
            if v < minval:
                v = minval
                optimal_move = action
        return v, optimal_move

    def min_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        v = 5
        for action in actions(board):
            maxval = max_value(result(board, action))[0]
            if v > maxval:
                v = maxval
                optimal_move = action
        return v, optimal_move
    if terminal(board):
        return None
    cur_player = player(board)
    if cur_player == "X":
        return max_value(board)[1]
    else:
        return min_value(board)[1]
    raise NotImplementedError


