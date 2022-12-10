import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = (0,0,0)

        #create a bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0, 0, 2.0, 15)
        self.rect.midtop = ai_game.crabs_2.rect_red.midtop

        #store the bullet's position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        self.y -= 0.5
        self.rect.y = self.y
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

class Bullet_2(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = (0,0,0)

        #create a bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0, 0, 2.0, 15)
        self.rect.midtop = ai_game.crabs_2.rect_green.midtop

        #store the bullet's position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        self.y -= 0.5
        self.rect.y = self.y
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

