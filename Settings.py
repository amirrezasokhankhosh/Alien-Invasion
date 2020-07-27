class Settings():
    def __init__(self):
        super().__init__()
        # SCREEN SETTINGS
        self.screen_width = 1200
        self.screen_height = 600
        self.background_color = (230, 230, 230)
        # SHIP SETTINGS
        self.ship_speed_factor = 1.5
        # BULLET SETTINGS
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3