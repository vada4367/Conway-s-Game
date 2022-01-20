# Импорт библиотек
import pygame
from pygame import color
from pygame.constants import WINDOWHITTEST
from pygame import RESIZABLE
import random
from pygame.time import Clock
pygame.init()
pygame.display.set_caption("Game life by god (vadim)")
clock = pygame.time.Clock()
WHITE = (200, 200, 200)
DARK = (70, 70, 70)
LIGHTGRAY = (150, 150, 150)
sc = pygame.display.set_mode((900, 600))

matrix = []
lif = []
unlif = []

start = False

dx = None
dy = None

def clear():
	matrix.clear()
	for i in range(0, 60):
		line = []
		for i in range(0, 90):
			line.append(0)
		matrix.append(line)

def printmat():
	for i in range(0, 60):
		for g in range(0, 90):
			if matrix[i][g] == 1:
				pygame.draw.rect(sc, DARK, (g * 10, i * 10, 10, 10))
	for i in range(1, 60):
		pygame.draw.line(sc, LIGHTGRAY, (0, i * 10), (900, i * 10))
	for i in range(1, 90):
		pygame.draw.line(sc, LIGHTGRAY, (i * 10, 0), (i * 10, 600))

def upd():
	for i in range(1, 59):
		for g in range(1, 89):
			kl = 0
			if matrix[i][g] == 0:

				if matrix[i - 1][g - 1] == 1:
					kl += 1
				if matrix[i - 1][g] == 1:
					kl += 1
				if matrix[i - 1][g + 1] == 1:
					kl += 1
				if matrix[i][g - 1] == 1:
					kl += 1
				if matrix[i][g + 1] == 1:
					kl += 1
				if matrix[i + 1][g - 1] == 1:
					kl += 1
				if matrix[i + 1][g] == 1:
					kl += 1
				if matrix[i + 1][g + 1] == 1:
					kl += 1

				if kl == 3:
					lif.append([i, g])

			if matrix[i][g] == 1:
				
				if matrix[i - 1][g - 1] == 1:
					kl += 1
				if matrix[i - 1][g] == 1:
					kl += 1
				if matrix[i - 1][g + 1] == 1:
					kl += 1
				if matrix[i][g - 1] == 1:
					kl += 1
				if matrix[i][g + 1] == 1:
					kl += 1
				if matrix[i + 1][g - 1] == 1:
					kl += 1
				if matrix[i + 1][g] == 1:
					kl += 1
				if matrix[i + 1][g + 1] == 1:
					kl += 1

				if kl == 2 or kl == 3:
					lif.append([i, g])
				else:
					unlif.append([i, g])
	for i in range(0, len(lif)):
		x = lif[i][1]
		y = lif[i][0]
		matrix[y][x] = 1
	for i in range(0, len(unlif)):
		x = unlif[i][1]
		y = unlif[i][0]
		matrix[y][x] = 0

def rand():
	clear()
	s = int(input("Шанс %:"))
	zak = int((5104 // 100) * s)
	i = 0
	while i <= zak:
		y = random.randint(1, 58)
		x = random.randint(1, 88)
		if not matrix[y][x]:
			matrix[y][x] = 1
		else:
			i -= 1
		i += 1


clear()

while True:
	
	sc.fill(WHITE)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_c and not start:
				clear()
			if event.key == pygame.K_s:
				if not start:
					start = True
				else:
					start = False
			if event.key == pygame.K_x:
				sss()
			if event.key == pygame.K_l:
				name = str(input("Whats name save?: "))
				file = open(name, 'r')
				matrix = file.read()
				file.close()
			if event.key == pygame.K_r:
				rand()

	if not start:
		pressed = pygame.mouse.get_pressed()
		if pressed[0] and dx == None and dy == None:
			pos = pygame.mouse.get_pos()
				
			x = pos[0]
			y = pos[1]

			dx = x // 10
			dy = y // 10

			if matrix[dy][dx] == 0:
				matrix[dy][dx] = 1
			else:
				matrix[dy][dx] = 0

	if start:
		upd()
		lif.clear()
		unlif.clear()

	dx = None
	dy = None
	print(matrix)
	printmat()
	pygame.display.update()
	clock.tick(10)