from time import sleep

error_msg = 'Invalid input. You are disqualified.'
alpha = 'abcdefgh'
numeric = '12345678'

coordinate_dict = {}
for i in range(8):
	coordinate_dict[alpha[i]] = i + 1

def print_instructions():
	print """
	Hello. Welcome to Chess. 
	It's a brand new game. 
	You are the first to ever play it.
	"""
	sleep(1)
	print """
	When stating your move, state it 
	in this fashion: 
	'a4 to c6' or 'e2 to e4'. 
	Be careful. An invalid input is 
	an immediate disqualification.
	"""
	sleep(1)
	print """
	Also, if someone wins, 
	please let me know so that I can 
	end the game. 
	Just have the winner enter: 'I won'.
	Typing 'End' also works, but it's 
	not as fun.
				Thanks :)


				"""
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
	# (9x9 because coordinates will be added 
	# (a-h, 1-8) in their own column and row)

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
	


# Sets board with standard chess setup

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



# Makes list of games for computer to reference to for potential moves

def make_game_history(file):
	transcription = ""
	i = 0
	while i < 15000:
		line = file.readline()
		transcription = transcription + line
		i = i + 1

	game_history = transcription.split('\n1.')
	for i in range(len(game_history)):
		game_history[i] = '1.' + game_history[i]

	return game_history



def find_move(current_position, game_history):

	# Find games identical to the current one.

	LENGTH = len(current_position)

	identical_games = []
	for game in game_history:
		if current_position == game[:LENGTH]:
			identical_games.append(game)

	# Add an if statement in case there are no identical games.

	if len(identical_games) == 0:
		pass

	# The following is written as a first draft 'test' with 
	# minimal preferences (such as likelihood of victory).

	if len(identical_games) > 0:
		second_half = identical_games[0][LENGTH:].split(" ")
		move = second_half[1]
		return move
	else:
		print 'No possible move found.'



# Testing...




f = open('chess_data.pgn', 'r')

my_game_history = make_game_history(f)
my_current_position = '1.Nf3 Nf6 2.d4 c5 3.c4'
my_move = find_move(my_current_position, my_game_history)
print my_move

f.close()










