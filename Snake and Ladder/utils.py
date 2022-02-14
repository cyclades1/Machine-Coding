import random


debug = False
class Board:

	def __init__(self, snake, ladder, player):
		self.snakes = {i:j for i , j in snake}
		self.ladders = {i:j for i , j in ladder}
		self.players = player
		self.player_pos = {p : 0 for p in player}
		self.player_cnt = len(player)
		self.chance = 0
		self.winner = None

	def __str__(self):
		return str(self.snakes)+str(self.ladders)+str(self.players)

	def check_snake_ladder(self, pos):
		on_ladder = pos in self.ladders
		on_snake = pos in self.snakes
		return on_snake or on_ladder

	def check_snake(self, pos):
		return pos in self.snakes

	def check_ladder(self, pos):
		return pos in self.ladders

	def set_player_pos(self, player, pos):
		self.player_pos[player]=pos

	def iswinner(self):
		return not bool(self.winner)

	def getwinner(self):
		if bool(self.winner):
			return self.winner
		return "No Winner"

	def update_round(self):
		point = random.randint(1, 6)
		player = self.players[self.chance]
		pos = self.player_pos[player]
		pos += point
		while self.check_snake_ladder(pos):
			if self.check_snake(pos):
				print("snake :", pos) if debug else True
				pos = self.snakes[pos]
			elif self.check_ladder(pos):
				print("ladder :", pos) if debug else True
				pos = self.ladders[pos]
		if pos>100:
			return
		print("{0} rolled a {1} and moved from {2} to {3}".format(player, point, self.player_pos[player], pos) )
		self.set_player_pos(player, pos)
		if pos == 100:
			self.winner = player
		self.chance = (self.chance+1)%self.player_cnt

		