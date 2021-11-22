import sys
import pygame
import numpy as np
import time
import random

BLACK = (0, 0, 0)
WHITE = (230, 230, 230)
YELLOW = (210, 210, 0)
blockSize = 15
Start = 0

pygame.init()
n = int(input("Qual deverá ser a dimensão do tabuleiro?\n"))
modo = int(input("Qual modo?\n 1- Todas começam desligadas \n 2- Aleatório\n"))
WINDOW_WIDTH = blockSize*n
WINDOW_HEIGHT = blockSize*n
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT+60))
CLOCK = pygame.time.Clock()
StartButton = pygame.Rect(WINDOW_WIDTH/2-45,WINDOW_HEIGHT+20, 90, 30)
SCREEN.fill(BLACK)

#Botão de iniciar
pygame.draw.rect(SCREEN, (100,100,100), StartButton, 0)
smallfont = pygame.font.SysFont('Arial',28)
text = smallfont.render('Start' , True , WHITE)
SCREEN.blit(text , (WINDOW_WIDTH/2-30,WINDOW_HEIGHT+15))



def main(): 
	global SCREEN, CLOCK, WINDOW_WIDTH, WINDOW_HEIGHT, StartButton, Start, matrix, newMatrix, n
	if modo == 1:
		matrix = np.zeros((n,n))
	else:
		matrix = np.random.randint(0,2,(n,n))
	
	while True:
		drawGame()
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:  # Trocar cor do quadrado ou iniciar
				pos = pygame.mouse.get_pos()
				if pos[1] >= WINDOW_HEIGHT:
					Start = 1 - Start
				else:
					matrix[pos[0]//blockSize,pos[1]//blockSize] = 1 - matrix[pos[0]//blockSize,pos[1]//blockSize]
				

		pygame.display.update()
	
def drawGame():
	global SCREEN, CLOCK, WINDOW_WIDTH, WINDOW_HEIGHT, StartButton, Start, matrix, newMatrix, n
	
	
	# time.sleep(0.05)  Se achar rápido demais só descomentar
	
	#Colorindo os blocos
	for x in range(n):
		for y in range(n):
			rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
			pygame.draw.rect(SCREEN, YELLOW if matrix[x,y] else BLACK , rect, 0)
	#Grid base	
	for x in range(0, WINDOW_WIDTH, blockSize):
		for y in range(0, WINDOW_HEIGHT, blockSize):
			rect = pygame.Rect(x, y, blockSize, blockSize)
			pygame.draw.rect(SCREEN, WHITE, rect, 1)

		
			
	if Start:	# Iteração do jogo
		newMatrix = np.zeros((n,n))
		for x in range(n):
			for y in range (n):
				if matrix[x,y]:
					if getNeighbors(x,y) == 2 or getNeighbors(x,y) == 3:
						newMatrix[x,y] = 1
					else:
						newMatrix[x,y] = 0
				elif getNeighbors(x,y) == 3:
					newMatrix[x,y] = 1
		matrix = newMatrix
			
def getNeighbors(x,y): # Retorna a quantidade de vizinhos, PS: o tabuleiro está modelado de forma cíclica, significando que a celula da extrema esquerda é adjacente a celula da extrema direita
	return matrix[(x-1)%n,(y-1)%n] +  matrix[x%n,(y-1)%n] +  matrix[(x+1)%n,(y-1)%n] +  matrix[x%n,(y+1)%n] +  matrix[(x-1)%n,(y+1)%n] +  matrix[(x+1)%n,(y+1)%n] +  matrix[(x-1)%n,y%n] +  matrix[(x+1)%n,y%n] 
	
if __name__ == '__main__':
    sys.exit(main())
