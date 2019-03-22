import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from dragon import Dragon
from freezer import Freezer
import game_functions as gf
from game_stats import GameStats
from button import Button
from score import Score


clock = pygame.time.Clock()
clock.tick(40)

def run_game():
	#Initialization of game and creation of object = screen
	pygame.init()
	
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	screen_rect = screen.get_rect()
	pygame.display.set_caption("DraGame")
	
	#Creating button Game
	play_button = Button(ai_settings, screen, "Play Game")
	
	#Creating an object to capture statistical data
	stats = GameStats(ai_settings)
	#Creating a scoreboard
	points_txt = str(ai_settings.points)
	dragons_left_txt = str(stats.dragons_left)
	score_board = Score(ai_settings, screen, "lifes: " + dragons_left_txt, "Score:    " + points_txt) 
	
	#Creating the dragon.
	dragon = Dragon(ai_settings, screen)
	#Creating a group dedicated to store fireballs
	fireballs = Group()
	#creating a freezers group
	freezers = Group()
	
	
	#Starting the main loop of the game.
	while True:
		gf.check_events(ai_settings, screen, stats, play_button, dragon, fireballs)
		points_txt = str(ai_settings.points)
		dragons_left_txt = str(stats.dragons_left)
		if stats.game_active:
			dragon.update()	
			time_1 = pygame.time.get_ticks()
			time_2 = int(time_1/10)
			if time_2 % 100 in range(0, 3):
				new_freezer = Freezer(ai_settings, screen)
				freezers.add(new_freezer)
			gf.update_freezers(ai_settings, stats, screen, dragon, freezers, fireballs, score_board)		
			
			gf.update_fireballs(ai_settings, screen, dragon, freezers, fireballs)
		gf.update_screen(ai_settings, screen, stats, dragon, freezers, fireballs, play_button, score_board)
				
run_game()
