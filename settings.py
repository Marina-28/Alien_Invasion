class Settings():
	"""Class for storing game settings."""
	def __init__(self):
		"""Initializing game settings."""
		self.screen_width = 1400
		self.screen_height = 800
		self.bg_color = (190, 0, 255)
		self.ship_speed = 1.5

		self.bullet_speed = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)