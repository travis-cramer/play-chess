from time import sleep
import os

error_msg = 'Invalid input. You are disqualified.'
alpha = 'abcdefgh'
num_lab = '12345678'

coordinate_dict = {}
for i in range(8):
	coordinate_dict[alpha[i]] = i + 1

def print_instructions():
	sleep(1)
	print "Get ready..."
	sleep(1)
	print 'Begin!'
	sleep(1)

def print_board(board):
	for row in board:
		print ' '.join(row)

def make_board():
	board = []
	# Make empty board of right size.
	for i in range(9):
		board.append(['|||']*9)

	# Make it checkered
	for i in range(1,9,2):
		for j in range(0,9,2):
			board[i][j] = '| |'

	for i in range(2,9,2):
		for j in range(1,9,2):
			board[i][j] = '| |'
		
	# Label coordinates (A-H)
	col_lab = []
	for i in range(8):
		col_lab.append('0')
	for i in range(8):
		col_lab[i] = ' ' + alpha[i] + ' '
	for i in range(8):
		board[8][i + 1] = col_lab[i]

	# Label coordinates (1-8)
	for i in range(8):
		board[i][0] = ' ' + str(8 - i) + ' '

	return board
	


def set_board(board):
	# Set up pawns
	for i in range(1,9):
		board[1][i] = '[i]'
		board[6][i] = '(i)'

	# Set up backlines
	# Rooks
	for i in range(1,9,7):
		board[0][i] = '[I]'
		board[7][i] = '(I)'

	# Knights
	for i in range(2,8,5):
		board[0][i] = '[>]'
		board[7][i] = '(>)'

	# Bishops
	for i in range(3,7,3):
		board[0][i] = '[|]'
		board[7][i] = '(|)'

	# Queens
	board[0][4] = '[*]'
	board[7][4] = '(*)'

	# Kings
	board[0][5] = '[^]'
	board[7][5] = '(^)'

	# Clear bottom left corner
	board[8][0] = '   '

	return board


def move_piece(board, game):
	move = raw_input('Enter move: ')

	if len(move) != 8:
		if move == 'End' or move == 'I won':
			game = 1
			print 'Good job. You destroyed your friend. How kind.'
		else:
			print error_msg
			game = 1
			return game
	elif move[0] not in alpha or move[6] not in alpha:
		print error_msg
		game = 1	
	elif move[1] not in num_lab or move[7] not in num_lab:
		print error_msg
		game = 1
	else:
		initial = [move[0],int(move[1])]
		final = [move[6],int(move[7])]

	# Put copy of moving piece in final destination.
		piece = board[8 - initial[1]][coordinate_dict[initial[0]]]
		board[8 - final[1]][coordinate_dict[final[0]]] = piece

	# "Delete" copy of moving piece from initial position. Must account for checkered board (light or dark?).
		if (8 - initial[1]) % 2 == 0:
			if coordinate_dict[initial[0]] % 2 == 0:
				board[8 - initial[1]][coordinate_dict[initial[0]]] = '|||'
			else:
				board[8 - initial[1]][coordinate_dict[initial[0]]] = '| |'
		else:
			if coordinate_dict[initial[0]] % 2 == 0:
				board[8 - initial[1]][coordinate_dict[initial[0]]] = '| |'
			else:
				board[8 - initial[1]][coordinate_dict[initial[0]]] = '|||'
	return game

def play_chess():
	game = 0
	print_instructions()
	my_board = make_board()
	my_board = set_board(my_board)
	print_board(my_board)
	while game == 0:
		game = move_piece(my_board, game)
		if game == 0:
			sleep(0.5)
			os.system('clear')
			print_board(my_board)


play_chess()

