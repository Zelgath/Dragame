class GameStats():
	'''Statistical data in game.'''
	
	def __init__(self, ai_settings):
		'''Initialization of statistical data.'''
		self.ai_settings = ai_settings
		self.reset_stats()
		self.game_active = False
		
	def reset_stats(self):
		'''Initialization of statistical data which can change during the game.'''
		self.dragons_left = self.ai_settings.dragon_limit
		



