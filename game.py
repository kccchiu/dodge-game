import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

RED =(255,0,0)
player_pos = [400,300]
player_size = 50

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))
	pygame.display.update()