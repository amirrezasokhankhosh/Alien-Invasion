import sys
import pygame
from Settings import Settings
import Game_functions
from Ship import Ship
from pygame.sprite import Group
from Game_stats import Game_stats
from Button import Button
from Scoreboard import Scoreboard

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    # Initialize game IO.
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Draw a ship
    ship = Ship(screen, ai_settings)

    # Make 2 group to store bullets and aliens in.
    bullets = Group()
    aliens = Group()

    # Create instance to store game statics
    stats = Game_stats(ai_settings)

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    #craate scoreboard 
    scoreboard = Scoreboard(ai_settings , screen , stats)


    Game_functions.create_fleet(ai_settings, screen, ship, aliens)
    # Start the main loop for the game. 
    while True:
        # Watch for keyboard and mouse events.
        Game_functions.check_events(ai_settings, screen, stats, scoreboard, play_button, ship, aliens , bullets)
        if stats.game_active == True:
            ship.update()
            Game_functions.update_bullets(ai_settings, screen, stats, scoreboard, ship, aliens, bullets )
            Game_functions.update_aliens(ai_settings, stats, screen, ship, aliens  , bullets)

        Game_functions.update_screen(ai_settings, screen, stats, scoreboard,ship, aliens, bullets, play_button)


run_game()  
