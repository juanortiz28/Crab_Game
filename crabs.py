import pygame
import random
from settings2 import Settings
from pygame.sprite import Sprite


class CrabsGame2:

    def __init__(self, ai_game):
        """ship's starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.width, self.height = self.screen.get_size()
        self.speed = 0.5

        # load up ship

        self.image_green = pygame.image.load('images/green.png')
        self.image_red = pygame.image.load('images/red.png')
        # self.red_crab_rot = pygame.transform.rotate(self.image_red, -90)
        # self.green_crab_rot = pygame.transform.rotate(self.image_green, 90)
        self.rect_red = self.image_red.get_rect()
        self.rect_green = self.image_green.get_rect()

        # start each ship at the bottom
        self.rect_red.midleft = self.screen_rect.midleft
        self.rect_green.midright = self.screen_rect.midright

        # store a decimal value for the ship's horizontal position

        self.rect_green.x = float(self.rect_green.x)
        self.rect_green.y = float(self.rect_green.y)
        self.rect_red.x = float(self.rect_red.x)
        self.rect_red.y = float(self.rect_red.y)
        self.red_height = self.rect_red.height


        # movement

        self.moving_up_red = False
        self.moving_down_red = False

        self.moving_up_green = False
        self.moving_down_green = False

    def update(self):
        """update the ship's position based on the movement flag"""
        #update the ships x value, not rect
        if self.moving_down_red and self.rect_red.bottom < self.screen_rect.bottom:
            self.rect_red.y += 1
        if self.moving_up_red and self.rect_red.top > 0:
            self.rect_red.y -= 1

        if self.moving_down_green and self.rect_green.bottom < self.screen_rect.bottom:
            self.rect_green.y += 1
            print(self.moving_down_green)
        if self.moving_up_green and self.rect_green.top > 0:
            print(self.moving_up_green)
            self.rect_green.y -= 1

        self.rect_red.y = self.rect_red.y
        self.rect_red.x = self.rect_red.x
        self.rect_green.y = self.rect_green.y
        self.rect_green.x = self.rect_green.x

        w_red, h_red = pygame.display.get_surface().get_size()
        self.rect_red.y = self.rect_red.y % h_red

    def center_crab(self):
        """center after collision"""
        self.rect_green.midright = self.screen_rect.midright
        self.rect_green.x = float(self.rect_green.x)
        self.rect_green.y = float(self.rect_green.y)
        self.rect_red.midleft = self.screen_rect.midleft
        self.rect_red.x = float(self.rect_red.x)
        self.rect_red.y = float(self.rect_red.y)


    def blitme(self):
        """draw ship at current location"""
        self.screen.blit(self.image_red, self.rect_red)
        self.screen.blit(self.image_green, self.rect_green)



class Crabs_New:
    def __init__(self, ai_game):
        """ship's starting position"""
        self.screen = ai_game.screen
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
            self.rect_blue.y -= random.randint(0, 3) - 1
            self.rect_red.y -= random.randint(0,3) - 1
            self.rect_green.y -= random.randint(0,3) - 1
        elif self.height > 720:
            self.rect_blue.y -= random.randint(0, 2) - 0.4
            self.rect_red.y -= random.randint(0, 2) - 0.4
            self.rect_green.y -= random.randint(0, 2) - 0.4


        #update rect object from self.x
        self.rect_blue.x = self.rect_blue.x
        self.rect_blue.y = self.rect_blue.y
        self.rect_red.y = self.rect_red.y
        self.rect_red.x = self.rect_red.x
        self.rect_green.y = self.rect_green.y
        self.rect_green.x = self.rect_green.x

    def center_crab(self):
        """center after collision"""
        self.rect_blue.midbottom = self.screen_rect.midbottom
        self.rect_blue.x = float(self.rect_blue.x)
        self.rect_blue.y = float(self.rect_blue.y)
        self.rect_green.bottomright = self.screen_rect.bottomright
        self.rect_green.x = float(self.rect_green.x)
        self.rect_green.y = float(self.rect_green.y)
        self.rect_red.bottomleft = self.screen_rect.bottomleft
        self.rect_red.x = float(self.rect_red.x)
        self.rect_red.y = float(self.rect_red.y)

    def blitme(self):
        """draw ship at current location"""
        self.screen.blit(self.image_blue, self.rect_blue)
        self.screen.blit(self.image_red, self.rect_red)
        self.screen.blit(self.image_green, self.rect_green)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect_blue.top == screen_rect.top:
            self.settings.winner_Crab = 'BLUE'
            self.settings.race = False
        elif self.rect_red.top == screen_rect.top:
            self.settings.winner_Crab = 'RED'
            self.settings.race = False
        elif self.rect_green.top == screen_rect.top:
            self.settings.winner_Crab = 'GREEN'
            self.settings.race = False

    # def center_red(self):
    #     self.rect_red.bottomleft = self.screen_rect.bottomleft
    #     self.rect_red.x = float(self.rect_red.x)
    #     self.rect_red.y = float(self.rect_red.y)
    #
    # def center_blue(self):
    #     self.rect_blue.midbottom = self.screen_rect.midbottom
    #     self.rect_blue.x = float(self.rect_blue.x)
    #     self.rect_blue.y = float(self.rect_blue.y)
    # def center_green(self):
    #     self.rect_green.bottomright = self.screen_rect.bottomright
    #     self.rect_green.x = float(self.rect_green.x)
    #     self.rect_green.y = float(self.rect_green.y)
    #
    #
    # # def check_edges(self):
    # #     screen_rect = self.screen.get_rect()
    # #     if self.rect_blue.top == screen_rect.top:
    # #         # self.center_blue()
    # #         self.settings.laps_blue -= 1
    # #         if self.settings.laps_blue == 0:
    # #             self.settings.race = False
    # #             self.settings.guess = 'BLUE'
    # #
    # #     if self.rect_red.top == screen_rect.top:
    # #         self.settings.laps_red -= 1
    # #         self.center_red()
    # #         if self.settings.laps_red == 0:
    # #             self.settings.race = False
    # #             self.settings.guess = 'RED'
    # #
    # #     if self.rect_green.top == screen_rect.top:
    # #         self.settings.laps_green -= 1
    # #         self.center_green()
    # #         if self.settings.laps_green == 0:
    # #             self.settings.race = False
    # #             self.settings.guess = 'RED'
    # def reset_laps(self):
    #     self.settings.laps_red = 3
    #     self.settings.laps_blue = 3
    #     self.settings.laps_green = 3


class SeaShells(Sprite):
    """a class to represent a single alien in the fleet"""

    def __init__(self, ai_game):
        """initialize the alien with its position"""
        super().__init__()
        self.screen = ai_game.screen
        # self.settings = ai_game.settings

        # load the seashell image with its rect things
        self.ogimage = pygame.image.load('images/shell.png')
        self.image = self.ogimage
        self.rect = self.image.get_rect()
        # start each alien top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # store alien's  x- position
        self.x = float(self.rect.x)

    def check_edges(self):
        # return true if alien is at edge of screen
        screen_rect = self.screen.get_rect()
        if self.rect.right > screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """move right"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

