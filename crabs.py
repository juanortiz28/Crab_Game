import pygame
from pygame.sprite import Sprite
import random
from settings2 import Settings

class Crabs:
    def __init__(self, ai_gamne):
        super().__init__()
        self.screen = ai_gamne.screen
        self.speed = 0.5
        self.settings = Settings()
        self.red_crab = pygame.image.load('images/red.png')
        self.green_crab = pygame.image.load('images/green.png')
        self.blue_crab = pygame.image.load('images/blue.png')
        self.rect_red = self.red_crab.get_rect()
        self.rect_blue = self.blue_crab.get_rect()
        self.rect_green = self.green_crab.get_rect()
        self.x, self.y = self.screen.get_size()
        self.red_crab_x = 0
        self.red_crab_y = self.y - 50
        self.blue_crab_x = self.x / 2 - 30
        self.blue_crab_y = self.y - 50
        self.green_crab_x = self.x - 70
        self.green_crab_y = self.y - 50
        self.rect_red = pygame.Rect(0,0,self.red_crab_x, self.red_crab_y)

    def create_crabs(self):
        self.screen.blit(self.red_crab, (self.red_crab_x, self.red_crab_y))
        self.screen.blit(self.blue_crab, (self.blue_crab_x, self.blue_crab_y))
        self.screen.blit(self.green_crab, (self.green_crab_x, self.green_crab_y))
    def check_top(self):
        screen_rect = self.screen.get_rect()
        if self.rect_blue <= screen_rect.top:
            print("YESSSSS")
    def update(self):
        """adjust the speed based on the screen size"""
        if self.y <= 720:
            self.blue_crab_y -= self.speed * random.randint(-2, 2) + 1/4
            self.green_crab_y -= self.speed * random.randint(-2, 2) + 1/4
            self.red_crab_y -= self.speed * random.randint(-2, 2) + 1/4
        elif self.y > 720:
            self.blue_crab_y -= random.randint(-2, 2) + 0.5
            self.green_crab_y -= random.randint(-2, 2) + 0.5
            self.red_crab_y -= random.randint(-2, 2) + 0.5
# class Red(Sprite):
#     def __init__(self, ai_game):
#         super().__init__()
#         self.screen = ai_game.screen
#         self.settings = ai_game.settings
#         self.red_og = pygame.image.load('images/red.png')
#         self.red = self.red_og
#         self.rect = self.red.get_rect()
#         self.rect.x = self.rect.width
#         self.rect.y = self.rect.bottom - 20
#         self.y = float(self.rect.y)
#         self.x = float(self.rect.x)

class Crabs_Game2:
    def __init__(self, ai_gamne):
        super().__init__()
        self.screen = ai_gamne.screen
        self.speed = 0.5
        self.red_crab = pygame.image.load('images/red.png')
        self.green_crab = pygame.image.load('images/green.png')
        self.blue_crab = pygame.image.load('images/blue.png')
        self.rect_red = self.red_crab.get_rect()
        self.rect_blue = self.blue_crab.get_rect()
        self.rect_green = self.green_crab.get_rect()
        self.x, self.y = self.screen.get_size()

    def create_crabs(self):
        self.screen.blit(self.red_crab, (0, self.y / 2))
        self.screen.blit(self.blue_crab, (self.x - 70, self.y / 2))

class Crabs_New:
    def __init__(self, ai_game):
        """ship's starting position"""
        self.screen = ai_game.screen
        # self.angle = ai_game.angle
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.width, self.height = self.screen.get_size()
        self.speed = 0.5

        #load up ship

        self.image_blue = pygame.image.load('images/blue.png')
        self.image_green = pygame.image.load('images/green.png')
        self.image_red = pygame.image.load('images/red.png')
        self.rect_blue = self.image_blue.get_rect()
        self.rect_red = self.image_red.get_rect()
        self.rect_green = self.image_green.get_rect()

        # start each ship at the bottom
        self.rect_blue.midbottom = self.screen_rect.midbottom
        self.rect_red.bottomleft = self.screen_rect.bottomleft
        self.rect_green.bottomright = self.screen_rect.bottomright

        #store a decimal value for the ship's horizontal position
        self.rect_blue.x = float(self.rect_blue.x)
        self.rect_blue.y = float(self.rect_blue.y)
        self.rect_green.x = float(self.rect_green.x)
        self.rect_green.y = float(self.rect_green.y)
        self.rect_red.x = float(self.rect_red.x)
        self.rect_red.y = float(self.rect_red.y)

        #movement
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """update the crab's's position based on random int"""

        if self.height <= 720:
            self.rect_blue.y -= random.randint(0,3) - 1
            self.rect_red.y -= random.randint(0,3) - 1
            self.rect_green.y -= random.randint(0,3) - 1
        elif self.height > 720:
            self.rect_blue.y -= random.randint(0, 3) - 1
            self.rect_red.y -= random.randint(0, 3) - 1
            self.rect_green.y -= random.randint(0, 3) - 1


        #update rect object from self.x
        self.rect_blue.x = self.rect_blue.x
        self.rect_blue.y = self.rect_blue.y
        self.rect_red.y = self.rect_red.y
        self.rect_red.x = self.rect_red.x
        self.rect_green.y = self.rect_green.y
        self.rect_green.x = self.rect_green.x
    def center_ship(self):
        """center after collision"""
        self.rect_blue.midbottom = self.screen_rect.midbottom
        self.rect_blue.x = float(self.rect_blue.x)
        self.rect_blue.y = float(self.rect_blue.y)
        self.rect_green.bottomright = self.screen_rect.bottomright
        self.rect_green.x = float(self.rect_green.x)
        self.rect_green.y = float(self.rect_green.y)
        self.rect_blue.bottomleft = self.screen_rect.bottomleft
        self.rect_red.x = float(self.rect_red.x)
        self.rect_red.y = float(self.rect_red.y)
    def blitme(self):
        """draw ship at current location"""
        self.screen.blit(self.image_blue, self.rect_blue)
        self.screen.blit(self.image_red, self.rect_red)
        self.screen.blit(self.image_green, self.rect_green)
    def check_edges(self):
        #return true if alien is at edge of screen
        screen_rect = self.screen.get_rect()

        if self.rect_blue.top == screen_rect.top:
            self.settings.guess = 'BLUE'
            self.settings.game_active = False
        elif self.rect_red.top == screen_rect.top:
            self.settings.guess = 'RED'
            self.settings.game_active = False
        elif self.rect_green.top == screen_rect.top:
            self.settings.guess = 'GREEN'
            self.settings.game_active = False


