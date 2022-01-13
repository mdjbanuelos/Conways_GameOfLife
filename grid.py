import pygame

class Grid:

	def __init__(self, tile_size, width, height):
		self.tile_size = int(tile_size)
		self.width = int(width)
		self.height = int(height)
		self.matrix = [[0 for tile in range(int(self.width/self.tile_size))] for row in range(int(self.height/self.tile_size))]
		print("Height: " + str(len(self.matrix)))
		print("Width: " + str(len(self.matrix[0])))
	def draw(self, screen):
		for row_index, row in enumerate(self.matrix):
			pygame.draw.line(screen, "Black", (0, row_index * self.tile_size), (self.width, row_index * self.tile_size))
			for col_index, col in enumerate(row):
				pygame.draw.line(screen, "Black", (self.tile_size * col_index, row_index * self.tile_size), (self.tile_size * col_index, row_index * self.tile_size + self.tile_size))
				if self.matrix[row_index][col_index] == 1:
					pygame.draw.rect(screen, "Black", (col_index * self.tile_size, row_index * self.tile_size,self.tile_size, self.tile_size))
	def get_grid(self):
		return self.matrix