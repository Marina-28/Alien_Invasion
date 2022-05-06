import pygame.font

class Button():
    """A class for creating a button."""
    def __init__(self, ai_game, msg):
        """Initializes button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Button params
        self.width, self.height = 200, 50
        self.button_color = (107, 246, 17)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Сообщение кнопки создается только один раз.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Converts msg to a rectangle and centers the text."""
        self.msg_image = self.font.render(msg, True, self.text_color,
        self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        """Display an empty button and display a message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)