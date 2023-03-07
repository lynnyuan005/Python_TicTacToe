'''
This is a Tic-Tac-Toe game. Here are the rules:
	1) The game is played on a grid that's 3 squares by 3 squares.
	2) First player choose to be X or O.
	3) Players take turns putting their marks in empty squares.
	4) The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.
'''

def display_board(board_list):
	'''
	board_list: a list that contains 9 items. Expected value of an item is from [Range(1,10), 'X', 'O'].
	This function displays board_list into a 3X3 square
	'''
	print('-------------')
	print(f'| {board_list[6]} | {board_list[7]} | {board_list[8]} |')
	print('-------------')
	print(f'| {board_list[3]} | {board_list[4]} | {board_list[5]} |')
	print('-------------')
	print(f'| {board_list[0]} | {board_list[1]} | {board_list[2]} |')
	print('-------------')

def ask_input(taken_positions,player_name):
	'''
	This funciton is used to ask position a player want to mark. It returns a number.
	taken_positions: a set of index that are already taken. Item should be number.
	player_name: the player that is asked to place marker.
	'''
	index_choice = 'EMPTY'
	while not index_choice.isdigit() or int(index_choice) not in range(1,10):
		index_choice = input(f'{player_name}, Please enter a position number from the board to place your mark (1-9): ')
		if not index_choice.isdigit():
			print('Invalid input. Please enter a number.')
		elif int(index_choice) not in range(1,10):
			print('Invalid input. Your position number should be from 1 to 9.')
		elif int(index_choice) in taken_positions:
			print('Invalid input. This position is already taken in the board.')
			index_choice = 'EMPTY'
		else:
			return int(index_choice)

def check_win(taken_positions):
	'''
	This funciton is used to determine if there's a winner in the input board_list.
	taken_positions: a set of index that are already taken. Item should be number.
	'''
	win_pattern = [{1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,5,7}]
	for pattern in win_pattern:
		if taken_positions >= pattern:
			return True
		else:
			continue
	return False

def ask_name(player):
	'''
	This function is used to ask name of a player.
	player: a string of player role. e.g. "player 1"
	'''
	player_name = ''
	while player_name == '':
		player_name = input(f'Please enter name of {player}: ')
		if player_name == '':
			print('Player name cannot be empty!')
		else:
			return player_name

# Set up game
print('Welcome to the Tic-Tac-Toe game!')
player_1 = ask_name('Player 1')
while True:
	player_2 = ask_name('Player 2')
	# Make sure the name of two players are different.
	if player_2.lower() == player_1.lower():
		print(f'{player_2} is already taken. Please use a different name.')
	else:
		break

print(f'{player_1} uses mark "X" and {player_2} uses mark "O".')

# Initialize variables
board_list = list(range(1,10))
winner = ''
player_log = [{'Name':player_1,'Positions':set(),'Mark':'X'},{'Name':player_2,'Positions':set(),'Mark':'O'}]
current_player = 0
display_board(board_list)
turn_count = 0

# Start playing
while winner == '':
	# Determine current player
	current_player = turn_count%2
	# Union all positions that are already taken
	taken_positions = player_log[0]['Positions'].union(player_log[1]['Positions'])
	# Ask player to select position
	index_choice = ask_input(taken_positions,player_log[current_player]['Name'])
	# Update board_list and positions taken by current user in player_log
	board_list[index_choice-1] = player_log[current_player]['Mark']
	player_log[current_player]['Positions'].add(index_choice)
	display_board(board_list)

	# Check if game should be ended
	if check_win(player_log[current_player]['Positions']):
		winner = player_log[current_player]['Name']
		break
	else:
		turn_count += 1

	# End game after 9 turns
	if turn_count >= 9:
		break

if winner == '':
	print('Tie! No one wins and no one loses.')
else:
	print(f'Congrats! {winner} wins the game!')
