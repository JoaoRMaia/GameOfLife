BLACK = (0, 0, 0)
WHITE = (230, 230, 230)
YELLOW = (210, 210, 0)
blockSize = 15

def main():
	global SCREEN, CLOCK, WINDOW_WIDTH, WINDOW_HEIGHT, matrix, n
	n = int(input("Qual deverá ser a dimensão do tabuleiro?\n"))
	WINDOW_WIDTH = 15*n
	WINDOW_HEIGHT = 15*n
	matrix = np.zeros((n,n))
	pygame.init()
	SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
	CLOCK = pygame.time.Clock()
	SCREEN.fill(BLACK)
	while True:
		drawGame()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.update()
	
def drawGame():
	for x in range(n):
		for y in range(n):
			if matrix[x,y]:
				rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
				pygame.draw.rect(SCREEN, YELLOW, rect, 0)
			
	for x in range(0, WINDOW_WIDTH, blockSize):
		for y in range(0, WINDOW_HEIGHT, blockSize):
			rect = pygame.Rect(x, y, blockSize, blockSize)
			pygame.draw.rect(SCREEN, WHITE, rect, 1)
			
			
if __name__ == '__main__':
    import sys
    import pygame
    import numpy as np
    sys.exit(main())
