import sys
import time 
class GameOfLife:
	def __init__(self, grid):
		self.DRAWING = False
		self.RUNNING = False
		self.grid = grid

	def update(self, mouse_pos):
		
		if not self.RUNNING:
			if self.DRAWING:
				x, y = self.get_tile_pos(mouse_pos)
				self.grid.matrix[y][x] = 1
		else:
			# Conways Game Of Life
			temp_matrix = []
			for i, row in enumerate(self.grid.matrix):
				temp_row = []
				for j, cell in enumerate(row):
					temp_row.append(self.nextState(cell, i, j))
				temp_matrix.append(temp_row)

			self.grid.matrix = temp_matrix
			time.sleep(0.1)

	def draw(self, screen):
		self.grid.draw(screen)

	def get_tile_pos(self, mouse_pos):
		x = mouse_pos[0]
		y = mouse_pos[1]

		x = int(x / self.grid.tile_size)
		y = int(y / self.grid.tile_size)
		return x,y

	def nextState(self, value, i, j):
		if value == 1: # Cell is alive
			if self.neighborCount(i,j) == 2 or self.neighborCount(i,j) == 3:
				return 1	# cell value  stays the same. The cell survives
			else:
				return 0

		else:# Cell is dead
			if self.neighborCount(i,j) == 3:
				return 1
			else:
				return 0

	def neighborCount(self, y,x):
		top_left = 0
		top_right = 0
		bot_left = 0
		bot_right = 0
		up = 0
		down = 0
		left = 0
		right = 0

		if not (x == 0 or y == 0 or x == 99 or y == 69):
			top_left = self.grid.matrix[y-1][x-1]
			top_right = self.grid.matrix[y-1][x+1]
			bot_left = self.grid.matrix[y+1][x-1]
			bot_right = self.grid.matrix[y+1][x+1]
			up = self.grid.matrix[y-1][x]
			down = self.grid.matrix[y+1][x]
			left = self.grid.matrix[y][x-1]
			right = self.grid.matrix[y][x+1]

		return top_left + top_right + bot_left + bot_right + up + down + left + right

