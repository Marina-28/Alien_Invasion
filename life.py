import pygame
from pygame.sprite import Sprite

class Life(Sprite):
	"""Class for controlling ship."""
	def __init__(self, ai_game):
		"""Initializes the ship and sets its initial position."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()
		
		# Loads an image of the ship and gets a rectangle.
		self.image = pygame.image.load('images/ship_life.bmp')
		self.rect = self.image.get_rect()

		# Each new ship appears at the bottom of the screen
		self.rect.midbottom = self.screen_rect.midbottom

		self.moving_right = False
		self.moving_left = False

		self.x = float(self.rect.x)

		
	def blitme(self):
		"""Draw the ship in its current position."""
		self.screen.blit(self.image, self.rect)
