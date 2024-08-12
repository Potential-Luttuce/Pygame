import pygame

class Settings():
    # class to store settings of game
    def __init__(self):
        # set games settings
        self.screen_width = 1000
        self.screen_height = 650
        self.background = pygame.image.load('images/background.png')
        #self.bg_color = (230,230,230) # whtite bg
        #self.bg_img = pygame.image.load('images/ship.bmp')

        # Ship settings
        self.player_speed_factor = 2.5