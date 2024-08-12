# main game file

import pygame
from settings import Settings
from player import Player
import game_functions as gf
from temple import Temple 

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width,game_settings.screen_height))
    pygame.display.set_caption("Game Title") # title

    # Load the background image
    background = pygame.image.load('images/background.png')
    background = pygame.transform.scale(background, 
            (game_settings.screen_width,game_settings.screen_height))
    
    # make ship
    player = Player(game_settings, screen)
    temple = Temple(game_settings, screen)
    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(player)
        gf.check_events(temple)
        temple.update()
        player.update()
        gf.update_screen(game_settings, screen, temple, background)


run_game()