import sys
import pygame
from Settings import Settings
import Game_functions
from Ship import Ship
from pygame.sprite import Group
from Game_stats import Game_stats


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

    # Make 2 group to store bullets and aliens in.
    bullets = Group()
    aliens = Group()

    # Create instance to store game statics
    stats = Game_stats(ai_settings)

    Game_functions.create_fleet(ai_settings, screen, ship, aliens)
    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        Game_functions.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active == True:
            ship.update()
            Game_functions.update_bullets(ai_settings, screen, ship, aliens, bullets)
            Game_functions.update_aliens(ai_settings, stats, screen, ship, aliens  , bullets)
        
        Game_functions.upgrade_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
