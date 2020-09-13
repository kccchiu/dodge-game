import sys
sys.path.insert(0, '../')
from player import HumanPlayer
from screen import Screen
from game import Game, HardGame, BossGame
import pygame
from main import play_game

if __name__ == "__main__":
	pygame.init()

	screen = Screen()
	player = HumanPlayer(screen.width/2, screen.height-100)
	game = BossGame()

	play_game(screen, player, game)
