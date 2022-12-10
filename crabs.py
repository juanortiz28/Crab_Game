import pygame
import random
from settings2 import Settings
from pygame.sprite import Sprite


class CrabsGame2:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.angle = ai_game.angle
        self.screen_rect = ai_game.screen.get_rect()
        self.width, self.height = self.screen.get_size()
        self.speed = 0.5

        self.image_green_og = pygame.image.load('images/green.png')
        self.image_red_og = pygame.image.load('images/red.png')
        self.image_green = self.image_green_og
        self.image_red = self.image_red_og
        self.rect_red = self.image_red.get_rect()
        self.rect_green = self.image_green.get_rect()
        self.image_red_rot = pygame.transform.rotate(self.image_red, self.angle)
        self.image_green_rot = pygame.transform.rotate(self.image_green, self.angle)
        self.rot_rect_red = self.image_red_rot.get_rect(center=self.rect_red.center)
        self.rot_rect_green = self.image_green_rot.get_rect(center=self.rect_green.center)

        self.rect_red = self.rot_rect_red
        self.rect_green = self.rot_rect_green

        self.rect_red.bottomleft = self.screen_rect.bottomleft
        self.rect_green.bottomright = self.screen_rect.bottomright


        self.rect_green.x = float(self.rect_green.x)
        self.rect_green.y = float(self.rect_green.y)
        self.rect_red.x = float(self.rect_red.x)
        self.rect_red.y = float(self.rect_red.y)
        self.red_height = self.rect_red.height



        self.moving_up_red = False
        self.moving_down_red = False
        self.moving_up_green = False
        self.moving_down_green = False
        self.moving_left_red = False
        self.moving_right_red = False
        self.moving_left_green = False
        self.moving_right_green = False

    def update(self):
        if self.moving_down_red and self.rect_red.bottom < self.screen_rect.bottom:
            self.rect_red.y += 2
        if self.moving_up_red and self.rect_red.top > 0:
            self.rect_red.y -= 2

        if self.moving_down_green and self.rect_green.bottom < self.screen_rect.bottom:
            self.rect_green.y += 2
        if self.moving_up_green and self.rect_green.top > 0:
            self.rect_green.y -= 2

        if self.moving_right_red and self.rect_red.right < self.screen_rect.right:
            self.rect_red.x += 2
        if self.moving_left_red and self.rect_red.left > 0:
            self.rect_red.x -= 2

        if self.moving_right_green and self.rect_green.right < self.screen_rect.right:
            self.rect_green.x += 2
        if self.moving_left_green and self.rect_green.left > 0:
            self.rect_green.x -= 2

        self.rect_red.y = self.rect_red.y
        self.rect_red.x = self.rect_red.x
        self.rect_green.y = self.rect_green.y
        self.rect_green.x = self.rect_green.x

    def center_crab(self):
        self.rect_green.midright = self.screen_rect.midright
        self.rect_green.x = float(self.rect_green.x)
        self.rect_green.y = float(self.rect_green.y)
        self.rect_red.midleft = self.screen_rect.midleft
        self.rect_red.x = float(self.rect_red.x)
        self.rect_red.y = float(self.rect_red.y)


    def blitme(self):
        self.screen.blit(self.image_red, self.rect_red)
        self.screen.blit(self.image_green, self.rect_green)



class Crabs_New:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.width, self.height = self.screen.get_size()
        self.speed = 0.5


        self.image_blue = pygame.image.load('images/blue.png')
        self.image_green = pygame.image.load('images/green.png')
        self.image_red = pygame.image.load('images/red.png')
        self.rect_blue = self.image_blue.get_rect()
        self.rect_red = self.image_red.get_rect()
        self.rect_green = self.image_green.get_rect()

        self.rect_blue.midbottom = self.screen_rect.midbottom
        self.rect_red.bottomleft = self.screen_rect.bottomleft
        self.rect_green.bottomright = self.screen_rect.bottomright

        self.rect_blue.x = float(self.rect_blue.x)
        self.rect_blue.y = float(self.rect_blue.y)
        self.rect_green.x = float(self.rect_green.x)
        self.rect_green.y = float(self.rect_green.y)
        self.rect_red.x = float(self.rect_red.x)
        self.rect_red.y = float(self.rect_red.y)

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


        self.rect_blue.x = self.rect_blue.x
        self.rect_blue.y = self.rect_blue.y
        self.rect_red.y = self.rect_red.y
        self.rect_red.x = self.rect_red.x
        self.rect_green.y = self.rect_green.y
        self.rect_green.x = self.rect_green.x

    def center_crab(self):
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
        self.screen.blit(self.image_blue, self.rect_blue)
        self.screen.blit(self.image_red, self.rect_red)
        self.screen.blit(self.image_green, self.rect_green)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect_blue.top == screen_rect.top:
            self.settings.winner_Crab = 'BLUE'
            self.settings.race = False
        if self.rect_red.top == screen_rect.top:
            self.settings.winner_Crab = 'RED'
            self.settings.race = False
        if self.rect_green.top == screen_rect.top:
            self.settings.winner_Crab = 'GREEN'
            self.settings.race = False

class SeaShells(Sprite):
    """a class to represent a single alien in the fleet"""

    def __init__(self, ai_game):
        """initialize the alien with its position"""
        super().__init__()
        self.screen = ai_game.screen

        self.ogimage = pygame.image.load('images/shell.png')
        self.image = self.ogimage
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right > screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """move right"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

