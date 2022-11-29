import pygame.font

class Crab_Race:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 300, 80
        self.button_color = (11, 226, 245)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont('comicsansms', 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.bottomleft = self.screen_rect.bottomleft
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

