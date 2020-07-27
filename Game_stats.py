class Game_stats():
    def __init__(self, ai_settings):
        super().__init__()
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.score = 0
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit

    def reset_level_score(self):
        self.level = 1
        self.score = 0
