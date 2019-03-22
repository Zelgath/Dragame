import pygame
import settings
from random import randint
from random import randrange
from pygame.sprite import Sprite

class Freezer(Sprite):
	'''Class defining the freezer monster.'''
	def __init__(self, ai_settings, screen):
		'''Initialization of freezer and it's first position.'''
		super(Freezer, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		#Loading Freezer png and defining it as a rectangle
		self.image = pygame.image.load('images\lodek.png')
		self.rect = self.image.get_rect()
		
		#Positioning of Freezer in the right corner
		self.rect.x = 1150
		self.rect.y = randrange(100, 700, 50)
		
		
		#Freezer speed factor
		self.speed_factor = randint(3, 6)
		
		#Making float from position of freezer
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		
		
	def update(self):
		'''moving a freezer on a screen'''
		self.x -= self.speed_factor
		#actualization of freezer place
		self.rect.x = self.x 
		
		
	def draw_freezer(self):
		'''Showing freezer in it's actual position'''
		self.screen.blit(self.image, self.rect)
	
