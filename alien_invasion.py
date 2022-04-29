import sys

import pygame

class AlienInvasion:
	"""Class to control game resources and behavior."""
	
	def __init__(self):
		"""Initialize of game and creating game resources."""
		pygame.init()

		self.screen = pygame.display.set_mode((1200, 800))
		pygame.display.set_caption("Alien Invasion")

	def run_game(self):
		"""Start the main game cycle."""
		while True:
			# Keyboard and mouse event tracking.
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			#Displays the last screen drawn.
			pygame.display.flip()

if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()



