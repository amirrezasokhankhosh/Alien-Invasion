import pygame


class Ship():
    def __init__(self, screen, ai_settings):
        super().__init__()
        # Initial ai_ settings
        self.ai_settings = ai_settings
        # Initial screen
        self.screen = screen
        # Load the image
        self.image = pygame.image.load("Images/ship.bmp")
        # Adjust the position on the screen
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Set center
        self.center = float(self.rect.centerx)
        # Flags for moving the ship
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
