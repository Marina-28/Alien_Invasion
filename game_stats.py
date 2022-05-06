class GameStats():
    """Tracking stats for the game Alien Invasion."""

    def __init__(self, ai_game):
        """Initializes statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
    
    def reset_stats(self):
        """Initializes statistics that change during the game."""
        self.ships_left = self.settings.ship_limit