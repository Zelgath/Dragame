import pygame.font

class Score():
	
	def __init__(self, ai_settings, screen, msg, msg_2):
		'''Initialization of scoreboard atributes'''
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		#definition of dimensions and properties of scoreboard
		self.width, self.height = 200, 100
		self.button_color = (0, 0 , 255)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 25)
		
		#Creating rect of button and center it
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.x = 0
		self.rect.y = 0
		
		self.prep_msg(msg, msg_2)
		
	
	def prep_msg(self, msg, msg_2):
		'''Placing a comunicat in generated screen and centerizing text on button.'''
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_2_image = self.font.render(msg_2, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_2_image_rect = self.msg_2_image.get_rect()
		self.msg_image_rect.x = 0
		self.msg_image_rect.y = 0
		self.msg_2_image_rect.x = 0
		self.msg_2_image_rect.y = 50
		
	def draw_score(self):
		#Showing the empty button, and communicate on it
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
		self.screen.blit(self.msg_2_image, self.msg_2_image_rect)

