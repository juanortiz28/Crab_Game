import pygame.font

class Tittle_Button:
    """this draws the "Crab Game" text rectangle in the beginning of the game!"""
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 300, 80
        self.button_color = (11, 226, 245)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont('felixtitling', 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

# class Start_Game1:
#     """a class to report scoring"""
#     def __init__(self, ai_game):
#         self.screen = ai_game.screen
#         self.screen_rect = self.screen.get_rect()
#         self.settings = ai_game.settings
#         self.stats = ai_game.stats
#         self.x, self.y = self.screen.get_size()
#         #font settings
#         self.text_color = (30, 30, 30)
#         self.font = pygame.font.SysFont(None, 48)
#         #prepare initial score image
#         self.prep_start()
#     def prep_start(self):
#         """render score image"""
#         score_str = str(self.stats.score)
#         self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
#         #display the score at top right
#         self.score_rect = self.score_image.get_rect()
#         self.score_rect.right = self.screen_rect.right - 20
#         self.score_rect.top = 20
#     def show_score(self):
#         """draw score to the screen"""
#         self.screen.blit(self.score_image, self.score_rect)
#TODO: CREATE THIS INTO THE CORRECT GUESS COUNTER
class Start_Game1:
    """This class creates the button for Crab Race which tells you to choose a crab! it will load in the middle of the screen"""
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 500, 80
        self.button_color = (0, 0, 0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont('felixtitling', 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_start_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class Red_R:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 70, 60
        self.button_color = (0, 0, 0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont('felixtitling', 24)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.bottomleft = self.screen_rect.bottomleft
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_start_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
class Green_G:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 70, 60
        self.button_color = (0, 0, 0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont('felixtitling', 24)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.bottomright = self.screen_rect.bottomright
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_start_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class Blue_B:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 70, 60
        self.button_color = (0, 0, 0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont('felixtitling', 24)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midbottom = self.screen_rect.midbottom
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_start_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


# print(pygame.font.get_fonts())