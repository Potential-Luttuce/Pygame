import pygame

player_w = 45
player_h = 60

class Player():
    
    def __init__(self, game_settings,screen):
        self.screen = screen
        self.game_settings = game_settings
        # # load player img and get it rect
        # alienplayer = pygame.image.load('images/alienplayer.bmp')
        # playerplayer = pygame.image.load('images/player.bmp')
       
        self.playerImage = pygame.image.load('images/player2.png')
        self.playerImage = pygame.transform.scale(self.playerImage, (player_w, player_h)) 

        #For testing - eventually will just be player
        # if self.playerImage == alienplayer:
        #     self.playerImage = pygame.transform.scale(elf.playerImage, (45,35)) # alien
        #     #print('show alien player please')
        # elif self.playerImage == playerplayer:
        #     #print('player player')
        #     self.playerImage = pygame.transform.scale(self.playerImage, (40,60)) # player
        
        self.rect = self.playerImage.get_rect()
        self.screen_rect = screen.get_rect()
        # new player at bottom of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the player's center.
        self.center = float(self.rect.centerx)
        
        #move ment flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # direction flags
        self.looking_l = True
        self.looking_r = False
        self.looking_u = False
        self.looking_d = True

    def update(self):
        #update player movement
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.playerImage = pygame.image.load('images/right_player2.png')
            self.playerImage = pygame.transform.scale(self.playerImage, (player_w, player_h)) 
            self.center += self.game_settings.player_speed_factor
            #self.rect.centerx +=5
        elif self.moving_left and self.rect.left > 0:
            self.playerImage = pygame.image.load('images/left_player2.png')
            self.playerImage = pygame.transform.scale(self.playerImage, (player_w, player_h)) 
            self.center -= self.game_settings.player_speed_factor
        elif self.moving_up:
            self.rect.centery -=10
            self.playerImage = pygame.image.load('images/back_player2.png')
            self.playerImage = pygame.transform.scale(self.playerImage, (player_w, player_h))
        elif self.moving_down:
            self.rect.centery +=10
            self.playerImage = pygame.image.load('images/player2.png')
            self.playerImage = pygame.transform.scale(self.playerImage, (player_w, player_h))
        self.rect.centerx = self.center

    def blitme(self):
        # Draw the player at its current location
        self.screen.blit(self.playerImage, self.rect)
        # draw border around element
        #pygame.draw.rect(self.screen, (255,255,255), self.rect, 1)
