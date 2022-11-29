import pygame

class Background1:
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.og_image1 = pygame.image.load('images/ocean.png')
        self.image = self.og_image1


class Crabs:
    def __init__(self, ai_game):
        super().__init__()
        self.screen2 = ai_game.screen
        self.red = pygame.image.load('images/red.png')
        self.red1 = self.red

