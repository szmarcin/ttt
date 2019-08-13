import random, time

class TicTacToe(object):
	def __init__(self, board, playerX, playerO):
		self.board = board
		self.playerX = playerX
		self.playerO = playerO
		self.player = playerX
	
	def play(self):
		while True:
			self.render()
			coord = self.get_coordinates()
			self.board.add_piece(coord, self.player.marker)
			if self.check_game_over():
				break
			time.sleep(.25)
			self.switch_players()
		self.render()

	def get_coordinates(self):
		while True:
			coord = self.player.ask_for_coordinates()
			if self.board.piece_location_valid(coord):
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
		if self.board.is_full():
			print("Draw")
			return True
		return False

	def check_victory(self):
		if self.board.winning_combination():
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
	DIAGONALS = [(0, 4, 8), (2, 4, 6)]
	HORIZONTALS = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
	VERTICALS = [(0, 3, 6), (1, 4, 7), (2, 5, 8)]
	
	def __init__(self):
		self.state = [self.EMPTY] * 9

	def add_piece(self, coord, player = 1):
		self.state[coord] = player

	def within_valid_coordinates(self, coord):
		if coord in range(len(self.state)):
			return True
		return False
	 
	def coordinates_available(self, coord):
		if self.state[coord] == self.EMPTY:
			return True
		return False
	
	def piece_location_valid(self, coord):
		if self.coordinates_available(coord) and self.within_valid_coordinates(coord):
			return True
		return False
		
	def winning_diagonal(self):
		for d in self.DIAGONALS:
			if self.state[d[0]] == self.state[d[1]] == self.state[d[2]] != self.EMPTY:
				return True
		return False
	
	def winning_horizontal(self):
		for h in self.HORIZONTALS:
			if self.state[h[0]] == self.state[h[1]] == self.state[h[2]] != self.EMPTY:
				return True
		return False
		
	def winning_vertical(self):
		for v in self.VERTICALS:
			if self.state[v[0]] == self.state[v[1]] == self.state[v[2]] != self.EMPTY:
				return True
		return False

	def winning_combination(self):
		if self.winning_vertical() or self.winning_horizontal() or self.winning_diagonal():
				return True
		return False

	def is_full(self):
		if all(self.state) != self.EMPTY:
			return True
		return False
	



playerX = Player('X')
playerO = Player('O')
board = Board()
ttt = TicTacToe(board, playerX, playerO)
ttt.play()

