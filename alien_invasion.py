import sys

import pygame

from settings import Settings

from ship import Ship

class AlienInvasion:
	"""Class to control game resources and behavior."""
	
	def __init__(self):
		"""Initialize of game and creating game resources."""
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		
		pygame.display.set_caption("Alien Invasion")
		
		self.bg_color = (self.settings.bg_color)
		self.ship = Ship(self)


	def run_game(self):
		"""Start the main game cycle."""
		while True:
			# Keyboard and mouse event tracking.
			self._check_events()
			self.ship.update()
			self._update_screen()
			
	
	def _check_events(self):
		"""Handles keystrokes and mouse events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		"""Responds to key presses."""
		if event.key == pygame.K_RIGHT:
			# Move the ship to the right/left
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_ESCAPE:
			sys.exit()

	def _check_keyup_events(self, event):
		"""Respond to key release."""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _update_screen(self):
		"""Updates the images on the screen and displays a new screen."""
		# Fill the screen with a specific color
		self.screen.fill(self.bg_color)
		self.ship.blitme()
		# Displays the last screen drawn.
		pygame.display.flip()

if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()



