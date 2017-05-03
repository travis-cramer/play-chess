def print_board(board):
	for row in board:
		print ' '.join(row)



def set_board():
	board = []
	# Make empty board of right size.
	for i in range(8):
		board.append(['|||']*8)

	# Make it checkered
	for i in range(0,8,2):
		for j in range(0,8,2):
			board[i][j] = '| |'

	for i in range(1,8,2):
		for j in range(1,8,2):
			board[i][j] = '| |'
		
	

	# Set up pawns
	for i in range(8):
		board[1][i] = '[i]'
		board[6][i] = '(i)'

	# Set up backlines
	# Rooks
	for i in range(0,8,7):
		board[0][i] = '[I]'
		board[7][i] = '(I)'

	# Knights
	for i in range(1,7,5):
		board[0][i] = '[>]'
		board[7][i] = '(>)'

	# Bishops
	for i in range(2,6,3):
		board[0][i] = '[|]'
		board[7][i] = '(|)'

	# Queens
	board[0][3] = '[*]'
	board[7][3] = '(*)'

	# Kings
	board[0][4] = '[^]'
	board[7][4] = '(^)'

	return board





print_board(set_board())


