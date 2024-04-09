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


def player(board):
	"""
	Returns player who has the next turn on a board.
	"""
	xs = 0
	os = 0

	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == X:
				xs += 1
			elif board[i][j] == O:
				os += 1

	if xs == 0 and os == 0:
		return X

	if xs > os:
		return O
	else:
		return X


def actions(board):
	"""
	Returns set of all possible actions (i, j) available on the board.
	"""
	emptyboardplaces = set()
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == None:
				emptyboardplaces.add((i, j))
	return emptyboardplaces


def result(board, action):
	"""
	Returns the board that results from making move (i, j) on the board.
	"""
	turn = player(board)
	i_value, j_value = action
	board[i_value][j_value] = turn
	return board


def winner(board):
	"""
	Returns the winner of the game, if there is one.
	"""
	if (terminal(board)):
		winner = utility(board)
		if (winner == 1):
			return X
		elif (winner == -1):
			return O


# The terminal function should accept a board as input, and return a boolean value indicating whether the game is over.
# If the game is over, either because someone has won the game or because all cells have been filled without anyone winning, the function should return True.
# Otherwise, the function should return False if the game is still in progress.
def terminal(board):
	"""
	Returns True if game is over, False otherwise.
	"""
	boardfilled = True

	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == None:
				boardfilled = False

	if boardfilled:
		return True
	
	for i in range(3):
		if board[i][0] == board[i][1] == board[i][2] != None:
			return True
		if board[0][i] == board[1][i] == board[2][i] != None:
			return True

	if board[0][0] == board[1][1] == board[2][2] != None:
		return True
	if board[0][2] == board[1][1] == board[2][0] != None:
		return True

	return False



def utility(board):
	"""
	Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
	"""
	for i in range(3):
		if board[i][0] == board[i][1] == board[i][2] != None:
			if board[i][0] == X:
				return 1
			elif board[i][0] == O:
				return -1
		if board[0][i] == board[1][i] == board[2][i] != None:
			if board[0][i] == X:
				return 1
			elif board[0][i] == O:
				return -1

	if board[0][0] == board[1][1] == board[2][2] != None:
		if board[0][0] == X:
			return 1
		elif board[0][0] == O:
			return -1
	if board[0][2] == board[1][1] == board[2][0] != None:
		if board[0][2] == X:
			return 1
		elif board[0][2] == O:
			return -1

	return 0


def deepcopy(board):
	new_board = []
	for row in board:
		new_row = []
		for element in row:
			new_row.append(element)
		new_board.append(new_row)
	return new_board

def minimax(board):
    if terminal(board):
        return None

    play = player(board)
    maximizer = play
    emptyboardplaces = actions(board)

    best_move = None
    best_score = float('-inf') if play == X else float('inf')

    for place in emptyboardplaces:
        new_board = deepcopy(board)
        new_board = result(new_board, place)
        score = evaluate_move(new_board, maximizer)
        if play == X:
            if score > best_score:
                best_score = score
                best_move = place
        else:
            if score < best_score:
                best_score = score
                best_move = place

    return best_move

def evaluate_move(board, player):
    if terminal(board):
        return utility(board)

    emptyboardplaces = actions(board)

    if player == X:
        best_score = float('-inf')
        for place in emptyboardplaces:
            new_board = deepcopy(board)
            new_board = result(new_board, place)
            score = evaluate_move(new_board, player)
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for place in emptyboardplaces:
            new_board = deepcopy(board)
            new_board = result(new_board, place)
            score = evaluate_move(new_board, player)
            best_score = min(best_score, score)
        return best_score


