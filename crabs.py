import pygame
from pygame.sprite import Sprite
import random


class Red(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.red_og = pygame.image.load('images/red.png')
        self.red = self.red_og
        self.rect = self.red.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.bottom - 20
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)



    def update(self):
        self.y -= random.randint(0,20)
        self.rect.y = self.y