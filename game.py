import pygame as pg
import sys
import random

pg.init()

#pre game set up
WIDTH = 800
HEIGHT = 600
screen = pg.display.set_mode((WIDTH, HEIGHT))

game_over = False

RED =(255,0,0)
BLUE = (0,0,255)
BG_COLOR = (0,0,0)

player_size = 50
player_pos = [WIDTH/2, HEIGHT-(2*player_size)]

enemy_size = 50
enemy_pos = [random.randrange(0,WIDTH), 0]


while not game_over:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()

		if event.type == pg.KEYDOWN:
			#if key is press grab x and y cord
			x = player_pos[0]
			y = player_pos[1]
			
			if event.key == pg.K_LEFT:
				x -= player_size
			elif event.key == pg.K_RIGHT:
				x += player_size

			player_pos = [x,y]
			
	screen.fill(BG_COLOR)

	pg.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

	pg.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))
	pg.display.update()