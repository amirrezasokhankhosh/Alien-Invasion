import sys
import pygame
from Settings import Settings
from Ship import Ship
import Game_functions
from pygame.sprite import Group


def run_game():
    # Initialize game and create a screen object.
    pygame.init()

    # Initialize game IO.
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Draw a ship
    ship = Ship(screen, ai_settings)

    # Make a group to store bullets in.
    bullets = Group()

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        Game_functions.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        Game_functions.update_bullets(bullets)
        Game_functions.upgrade_screen(ai_settings, screen, ship , bullets)


run_game()
