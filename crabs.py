import pygame


class Red:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.red_og = pygame.image.load('images/red.png')
        self.red = self.red_og
        self.rect_red = self.red.get_rect()
        self.rect_red.center = self.screen_rect.center
        self.x = float(self.rect_red.x)
        self.y = float(self.rect_red.y)
        self.moving_down = False
        self.moving_up = True

    def update(self):
        if self.moving_down and self.rect_red.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect_red.top > 0:
            self.y -= self.settings.ship_speed