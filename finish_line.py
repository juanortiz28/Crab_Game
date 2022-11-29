import pygame.font



class FinishLine:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = self.screen.get_size()
        self.button_color = (11, 226, 245)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont('comicsansms', 20)
        self.rect = pygame.Rect(0, 0, self.width, 30)
        self.rect.top = self.screen_rect.top
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)