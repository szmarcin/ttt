import random, time

class TicTacToe(object):
	def __init__(self, board, playerX, playerO):
		self.board = board
		self.playerX = playerX
		self.playerO = playerO
		self.player = random.choice([playerX, playerO])
	
	def play(self):
		self.render()
		while True:
			coord = self.get_coordinates()
			self.board.add_piece(coord, self.player.marker)
			self.render()
			if self.check_game_over():
				break
			time.sleep(.1)
			self.switch_players()
		

	def get_coordinates(self):
		while True:
			coord = self.player.ask_for_coordinates()
			if coord in self.board.available_coordinates():
				break
		return coord

	def switch_players(self):
		if self.player is self.playerX:
			self.player = self.playerO
		else:
			self.player = self.playerX
	
	def check_game_over(self):
		if self.check_draw() or self.check_victory():
			return True
		return False
	
	def check_draw(self):
		if self.board.is_full() and not self.check_victory():
			print("Draw\n")
			return True
		return False

	def check_victory(self):
		if self.board.winning_combination():
			print("{} won\n".format(self.player.marker))
			return True
		return False

	def render(self):
		board_state = []
		for i, piece in enumerate(self.board.state):
			if piece == self.board.EMPTY:
				board_state.append(str(i + 1))
			else:
				board_state.append(piece)
			
		print("\n%s %s %s" % (board_state[0], board_state[1], board_state[2]))
		print("%s %s %s" % (board_state[3], board_state[4], board_state[5]))
		print("%s %s %s\n" % (board_state[6], board_state[7], board_state[8]))

class Player(object):
	
	def __init__(self, marker):
		self.marker = marker
	
	def ask_for_coordinates(self):
		while True:
			coord = random.choice(range(9))
			if self.validate_coordinates_format(coord):
				return coord
	
	def validate_coordinates_format(self, coord):
		if type(coord) is int:
			return True
		return False
	
class Board(object):
	
	EMPTY = 0
	WINNING = [(0, 4, 8), (2, 4, 6), 			# diagonals
			   (0, 1, 2), (3, 4, 5), (6, 7, 8), # horizontals
			   (0, 3, 6), (1, 4, 7), (2, 5, 8)] # verticals
	
	def __init__(self):
		self.state = [self.EMPTY] * 9

	def add_piece(self, coord, marker = '.'):
		self.state[coord] = marker

	def available_coordinates(self):
		cords = []
		for i in range(len(self.state)): 
			if self.state[i] == self.EMPTY:
				cords.append(i)
		return cords
	 
	def winning_combination(self):
		for f,s,t in self.WINNING:
			if self.state[f] == self.state[s] == self.state[t] != self.EMPTY:
				return True
		return False
		
	def is_full(self):
		if all(self.state) != self.EMPTY:
			return True
		return False
	



playerX = Player(u'\u263D')
playerO = Player(u'\u263C')
board = Board()
ttt = TicTacToe(board, playerX, playerO)
ttt.play()

