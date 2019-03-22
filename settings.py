import pygame


class Settings():
	'''Class dedicated to store every setting of a game.'''
	
	def __init__(self):
		'''Initialization of game settings.'''
		#Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg = pygame.image.load('images/bg.bmp')
		
		#Settings of dragon.
		self.dragon_speed_factor = 8
		self.dragon_limit = 5
		self.points = 0
		
		#Settings of fireball.
		self.fireball_speed_factor = 15
		self.fireballs_allowed = 8
		self.fireball_image = pygame.image.load('images/fireball.png')
		

		
		
	
