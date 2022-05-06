import pygame.font
from pygame.sprite import Group

from life import Life

class Scoreboard():
    """A class for displaying game information."""

    def __init__(self, ai_game):
        """Initializes the scoring attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.ai_game = ai_game

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 36)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_lifes()
    
    def prep_score(self):
        """Converts the current account into a graphical representation."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True,
        self.text_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.bottom = 25

    def prep_high_score(self):
        """Converts the high score into a graphical representation."""
        rounded_high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(rounded_high_score)
        self.high_score_image = self.font.render(high_score_str, True,
        self.text_color, self.settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = 20
        self.high_score_rect.bottom = 25
    
    def prep_level(self):
        """Converts the level into a graphical representation."""
        level_str = str(self.stats.level) + " LVL"
        self.level_image = self.font.render(level_str, True,
        self.text_color, self.settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.bottom = 50
    
    def prep_lifes(self):
        """Display numb of ships on the screen."""
        self.lifes = Group()
        for life_numb in range(self.stats.ships_left):
            s = Life(self.ai_game)
            s.rect.x = 530 + life_numb * s.rect.width
            s.rect.y = 10
            self.lifes.add(s)

    def show_score(self):
        """Displays the score on the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.lifes.draw(self.screen)