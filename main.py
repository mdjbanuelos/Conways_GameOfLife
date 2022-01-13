import pygame, sys
import grid
import gameOfLife

# Constants
HEIGHT = 700
WIDTH = 1000

screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True

grid = grid.Grid(10,WIDTH,HEIGHT)
gameOfLife = gameOfLife.GameOfLife(grid)

while running:
	screen.fill("White")
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			gameOfLife.DRAWING = True
		if event.type == pygame.MOUSEBUTTONUP:
			gameOfLife.DRAWING = False

	gameOfLife.update(pygame.mouse.get_pos())
	gameOfLife.draw(screen)

	pygame.display.update()

pygame.quit()
sys.exit()