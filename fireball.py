import pygame
import settings
from pygame.sprite import Sprite
import dragon

class Fireball(Sprite):
	'''Class dedicated to manage fireball weapon.'''
	
	def __init__(self, ai_settings, screen, dragon):
		'''Creating object of fireball in actualposition of dragon'''
		super(Fireball, self).__init__()
		self.screen = screen
		
		
		#Creating a fireball in point (0,0), and definition of good position for it
		self.image = ai_settings.fireball_image
		self.rect = self.image.get_rect()
		self.rect.centery = dragon.rect.centery
		self.rect.right = dragon.rect.right
		
		#placing a fireball is defined as float.
		self.x = float(self.rect.x)
		
		self.speed_factor = ai_settings.fireball_speed_factor
		self.orient = dragon.orient
		
	def update(self):
		'''moving a fireball on screen.'''
		if self.orient == 1:
			self.x += self.speed_factor
			#actualizaton of fireball place
			self.rect.x = self.x
		
		
	def draw_fireball(self):
		'''Showing the fireball under a dragon.'''
		self.screen.blit(self.image, self.rect)
		

