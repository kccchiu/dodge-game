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
YELLOW = (255,255,0)
BG_COLOR = (0,0,0)

player_size = 50
player_pos = [WIDTH/2, HEIGHT-(2*player_size)]

enemy_size = 50
enemy_pos = [random.randrange(0,WIDTH-enemy_size), 0]
enemy_list = [enemy_pos]
SPEED = 20

score = 0

clock = pg.time.Clock()

myFont = pg.font.SysFont("monospac", 35)

def set_level(score, SPEED):
	if score <20:
		SPEED = 10
	elif score <40:
		SPEED = 15
	elif score <60:
		SPEED = 20
	else:
		SPEED = 25
	return SPEED

def drop_enemy(enemy_list):
	'''
	keep adding enemy until we have 10
	starting position is 0
	appened x and y to enemies list
	'''
	delay = random.random() #generate random decimal from 0 to 1
	if len(enemy_list) < 10 and delay< 0.1: #only 1/10 of the time will appened
		x_pos = random.randint(0, WIDTH-enemy_size)
		y_pos = 0
		enemy_list.append([x_pos,y_pos])

def draw_enemies(enemy_list):
	'''
	draw enemies from the enemies list
	'''
	for enemy_pos in enemy_list:
		pg.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

def collision_check(enemy_list, player_pos):
	for enemy_pos in enemy_list:
		if detect_collusion(player_pos, enemy_pos):
			return True
	return False

def detect_collusion(player_pos, enemy_pos):
	'''
	get position from player and enemy
	if player x or y position collide with enemy position
	'''
	p_x = player_pos[0]
	p_y = player_pos[1]

	e_x = enemy_pos[0]
	e_y = enemy_pos[1]

	if (e_x >= p_x and e_x < (p_x+player_size)) or (p_x >= e_x and p_x < (e_x+enemy_size)):
		if (e_y >= p_y and e_y < (p_y+player_size)) or (p_y >= e_y and p_y < (e_y+enemy_size)):
			return True
	return False

def update_enemy_position(enemy_list, score):
	for idx, enemy_pos in enumerate(enemy_list): #add index for pop
		#update position of enemies
		if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT: 
			enemy_pos[1] += SPEED #enemy falling by 6

		else:
			enemy_list.pop(idx)
			score += 1
	return score


while not game_over:
	for event in pg.event.get():

		if event.type == pg.QUIT: #quit game
			sys.exit()

		if event.type == pg.KEYDOWN:
			#if key is press grab x and y cord
			x = player_pos[0]
			y = player_pos[1]
			
			if event.key == pg.K_LEFT:  #move left and right based on key press
				x -= player_size
			elif event.key == pg.K_RIGHT:
				x += player_size

			player_pos = [x,y] #update player position
			
	screen.fill(BG_COLOR) #cover up the background

	if detect_collusion(player_pos, enemy_pos):
		game_over = True
		# break #exit when touch

	drop_enemy(enemy_list)
	score = update_enemy_position(enemy_list, score)
	
	SPEED = set_level(score, SPEED)

	text = "Score: " + str(score)
	label = myFont.render(text, 1 , YELLOW)
	screen.blit(label, (WIDTH-200, HEIGHT-40))

	if collision_check(enemy_list, player_pos):
		game_over = True
		break
	draw_enemies(enemy_list)

	pg.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

	clock.tick(30)

	pg.display.update()