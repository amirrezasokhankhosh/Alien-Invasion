import sys
import pygame
from Bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        # CHECK FOR QUIT
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event ,ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def upgrade_screen(ai_settings, screen, ship, bullets):
    # Set background
    screen.fill(ai_settings.background_color)
    # Draw the ship
    ship.blitme()
    # Redraw bullets 
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # Make the most recently drawn screen visible.
    pygame.display.flip()


def check_keydown_events(event , ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # Move ship to right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move ship to lefts
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        # Stop going left
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        # Stop going left
        ship.moving_left = False

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullets(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings , screen , ship)
        bullets.add(new_bullet)