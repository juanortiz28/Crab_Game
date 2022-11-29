import pygame.font

class Home:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 70, 70
        self.button_color = (0,0,0)
        self.text_color = (11, 226, 245)
        self.font = pygame.font.SysFont('felixtitling', 15)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = 10
        self.rect.y = 10
        # self.rect.topleft = self.screen_rect.topleft
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

