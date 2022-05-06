
import sys
from time import sleep
import pygame

from settings import Settings

from ship import Ship

from bullet import Bullet

from alien import Alien

from game_stats import GameStats

from button import Button

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

		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

		self.stats = GameStats(self)
		self.button = Button(self, "start")

		self._create_fleet()

	def run_game(self):
		"""Start the main game cycle."""
		while True:
			# Keyboard and mouse event tracking.
			self._check_events()
			if self.stats.game_active:
				self.ship.update()
				self._update_bullets()
				self._update_aliens()
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
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_button(mouse_pos)

	def _check_keydown_events(self, event):
		"""Responds to key presses."""
		if event.key == pygame.K_RIGHT:
			# Move the ship to the right/left
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_ESCAPE:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

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
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.aliens.draw(self.screen)

		if self.stats.game_active == False:
			self.button.draw_button()
		# Displays the last screen drawn.
		pygame.display.flip()
	
	def _fire_bullet(self):
		"""Creating a new bullet and adding its in group."""
		if (len(self.bullets) < self.settings.bullets_allowed):
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)
	
	def _remove_bullets(self):
		"""Removes bullets if they are above the screen."""
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)
	
	def _update_bullets(self):
		"""Updates projectile positions and destroys old projectiles."""
		self.bullets.update()
		self._remove_bullets()
		# check for hits on aliens.
		self._check_bullet_alien_collision()
		

	def _create_fleet(self):
		"""Creates fleet of aliens."""
		alien = Alien(self)
		alien_width = alien.rect.width
		alien_height = alien.rect.height

		available_space_x = self.settings.screen_width
		number_aliens_x = available_space_x // (2 * alien_width)

		#Define number of rows.
		ship_height = self.ship.rect.height
		available_space_y = self.settings.screen_height - (2 * ship_height)
		number_rows = available_space_y // (2 * alien_height)

		# Creating the first row of aliens.
		for row_number in range(number_rows):
			for alien_number in range(number_aliens_x):
				self._create_alien(alien_number, row_number)
	
	def _create_alien(self, alien_number, row_number):
		"""Creates the alien and append it in row."""
		alien = Alien(self)
		alien_width = alien.rect.width
		alien_height = alien.rect.height
		alien.x = 1 + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = 10 + 2 * alien_height * row_number
		self.aliens.add(alien)

	# def _create_fleet(self):
	# 	"""Creates fleet of aliens."""
	# 	alien = Alien(self)
	# 	alien_width = alien.rect.width
	# 	alien_height = alien.rect.height

	# 	available_space_x = self.settings.screen_width - (2 * alien_width)
	# 	number_aliens_x = available_space_x // (2 * alien_width)

	# 	#Define number of rows.
	# 	ship_height = self.ship.rect.height
	# 	available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
	# 	number_rows = available_space_y // (2 * alien_height)

	# 	# Creating the first row of aliens.
	# 	for row_number in range(number_rows):
	# 		for alien_number in range(number_aliens_x):
	# 			self._create_alien(alien_number, row_number)
	
	# def _create_alien(self, alien_number, row_number):
	# 	"""Creates the alien and append it in row."""
	# 	alien = Alien(self)
	# 	alien_width = alien.rect.width
	# 	alien_height = alien.rect.height
	# 	alien.x = alien_width + 2 * alien_width * alien_number
	# 	alien.rect.x = alien.x
	# 	alien.rect.y = alien_height + 2 * alien_height * row_number
	# 	self.aliens.add(alien)

	def _update_aliens(self):
		"""Updates aliens' position."""
		self.aliens.update()
		self._check_fleet_edges()
		# Check contact alien with ship
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()
		self._check_aliens_bottom()

	def _check_fleet_edges(self):
		"""Reacts when the alien reaches the edge of the screen."""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break
	
	def _change_fleet_direction(self):
		"""Lowering the entire fleet and changing the direction of the fleet."""
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1

	def _check_bullet_alien_collision(self):
		"""Processing projectile-alien collisions."""
		collision = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
		if not self.aliens:
			self.bullets.empty()
			self._create_fleet()
			self.settings.increase_speed()
	
	def _ship_hit(self):
		"""Handles the ship's collision with the alien."""
		if self.stats.ships_left > 0:
			self.stats.ships_left -= 1
			self.aliens.empty()
			self.bullets.empty()
			self._create_fleet()
			self.ship.center_ship()
			sleep(0.5)
		else:
			self.stats.game_active = False
			pygame.mouse.set_visible(True)
	
	def _check_aliens_bottom(self):
		"""Checks to see if the aliens have reached the bottom edge of the screen."""
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
				self._ship_hit()
				break
	def _check_button(self, mouse_pos):
		"""Starts a new game when you press Play."""
		if self.button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
			self.stats.reset_stats()
			self.stats.game_active = True
			self.aliens.empty()
			self.bullets.empty()
			self._create_fleet()
			self.ship.center_ship()
			pygame.mouse.set_visible(False)



if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()


