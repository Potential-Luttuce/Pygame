# game functions to make game work
# helps reduce clutter in main.py

import sys
import pygame

def check_keydown_events(event, player):
    # respond to key presses
    if event.key == pygame.K_RIGHT:
        player.moving_right = True
        player.moving_left = False
    elif event.key == pygame.K_LEFT:
        player.moving_left = True
        player.movinf_right = False
    elif event.key == pygame.K_UP:
        player.moving_up = True
        player.moving_down = False
    elif event.key == pygame.K_DOWN:
        player.moving_down = True
        player.moving_up = False

def check_keyup_events(event, player):
    # respond to key releasses
        if event.key == pygame.K_RIGHT:
            player.moving_right = False
            player.moving_left = False
        elif event.key == pygame.K_LEFT:
            player.moving_left = False
            player.moving_right = False
        elif event.key == pygame.K_UP:
            player.moving_up = False
            player.moding_down = False
        elif event.key == pygame.K_DOWN:
            player.moving_down = False
            player.moving_up = False

def check_events(player):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, player)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, player)   

def update_screen(game_settings,screen, player, background):
    # Update images on the screen and flip to the new screen.
    screen.blit(background, (0,0))
    player.blitme()
    # Make the most recently drawn screen visible.
    pygame.display.flip()