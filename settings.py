class Settings():
	"""Class for storing game settings."""
	def __init__(self):
		"""Initializing game settings."""
		self.screen_width = 1400
		self.screen_height = 800
		self.bg_color = (190, 0, 255)
		self.ship_limit = 3

		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 5

		self.fleet_drop_speed = 30

		self.speedup_scale = 1.1

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Initializes dynamic settings."""
		self.ship_speed = 1.5
		self.bullet_speed = 3.0
		self.alien_speed = 5.0
		self.fleet_direction = 1
		self.alien_points = 50
	
	def increase_speed(self):
		"""Increase speed"""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		self.alien_points *= 2