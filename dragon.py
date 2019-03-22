import pygame


class Dragon():
	
	def __init__(self, ai_settings, screen):
		'''Initialization of the dragon and it's start position.'''
		self.screen = screen
		self.ai_settings = ai_settings
		
		#Loading image of the dragon and aquiring it's rectangle.
		self.image = pygame.image.load('images\dragon.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#Every new dragon is apearing on the left side of the screen.
		self.rect.centery = self.screen_rect.centery
		self.rect.left = self.screen_rect.left
		
		#center point of the dragon is stored as float.
		self.center = float(self.rect.centery)
		self.center_x = float(self.rect.left)
		
		#Orientation of the dragon
		self.orient = 1
		
		#Options showing the movement of the dragon.
		self.moving_up = False
		self.moving_down = False
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		'''Actualization of position of the dragon based on the options which are showing the movement of dragon'''
		if self.moving_up and self.rect.top > 0:
			self.center -= self.ai_settings.dragon_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.center -= -(self.ai_settings.dragon_speed_factor)
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center_x -= -(self.ai_settings.dragon_speed_factor)
			self.orient = 1
			self.image = pygame.image.load('images\dragon.png')
		if self.moving_left and self.rect.left > 0:
			self.image = pygame.image.load('images\dragon_l.png')
			self.orient = -1
			self.center_x -= self.ai_settings.dragon_speed_factor
			
		#Actualization of the rect object based on value self.center.
		self.rect.centery = self.center
		self.rect.left = self.center_x
		
		
		
	def blitme(self):
		'''Showing the dragon in it's actual position.'''
		self.screen.blit(self.image, self.rect)

	def center_dragon(self):
		self.rect.centery = self.screen_rect.centery
		self.rect.left = self.screen_rect.left
