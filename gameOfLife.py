class GameOfLife:
	def __init__(self, grid):
		self.DRAWING = False
		self.grid = grid

	def update(self, mouse_pos):
		if self.DRAWING:
			print("Drawing")
			x, y = self.get_tile_pos(mouse_pos)
			print(x)
			print(y)
			self.grid.matrix[y][x] = 1


	def draw(self, screen):
		self.grid.draw(screen)

	def get_tile_pos(self, mouse_pos):
		x = mouse_pos[0]
		y = mouse_pos[1]

		x = int(x / self.grid.tile_size)
		y = int(y / self.grid.tile_size)
		return x,y