import pygame.font
import settings2

class Tittle_Button:
    """this draws the "Crab Game" text rectangle in the beginning of the game!"""
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 350, 80
        self.button_color = (11, 226, 245)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.Font('font/ModernWarfare-OV7KP.ttf', 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.blit(self.msg_image, self.msg_image_rect)

class Correct_Guess_Counter:
    """a class to report scoring"""
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.x, self.y = self.screen.get_size()
        #font settings
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font('font/ModernWarfare-OV7KP.ttf', 20)
        #prepare initial score image
        self.prep_start()
    def prep_start(self):
        """render score image"""
        score_str = str(self.settings.correct_guesses)
        self.score_image = self.font.render(score_str, True, self.text_color, None)
        #display the score at top right
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = self.y / 2
    def show_score(self):
        """draw score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
class Start_Game1:
    """This class creates the button for Crab Race which tells you to choose a crab! it will load in the middle of the screen"""
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 500, 80
        self.button_color = (0, 0, 0)
        self.text_color = (255,255,255)
        self.font = pygame.font.Font('font/ModernWarfare-OV7KP.ttf', 80)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_start_button(self):
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Winner:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 300, 80
        self.button_color = (0, 0, 0)
        self.text_color = (255,255,255)
        self.font = pygame.font.Font('font/ModernWarfare-OV7KP.ttf', 80)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_start_button(self):
        self.screen.blit(self.msg_image, self.msg_image_rect)



class Home:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 100, 50
        self.button_color = (0,0,0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font('font/ModernWarfare-OV7KP.ttf', 25)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = 10
        self.rect.y = 10
        self.rect.left = self.screen_rect.left + 130
        self.rect.top = 20
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.blit(self.msg_image, self.msg_image_rect)

class Guess_Correct:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        x, y = self.screen.get_size()
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 100, 50
        self.button_color = (0,0,0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font('font/ModernWarfare-OV7KP.ttf', 18)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = 10
        self.rect.y = 10
        self.rect.right = self.screen_rect.right - 70
        self.rect.top = (y // 2) - 40
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.blit(self.msg_image, self.msg_image_rect)

class Start_Over:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 200, 50
        self.button_color = (0,0,0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font('font/ModernWarfare-OV7KP.ttf', 18)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = 10
        self.rect.y = 10
        self.rect.right = self.screen_rect.right - 50
        self.rect.top = 20
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.blit(self.msg_image, self.msg_image_rect)

# print(pygame.font.get_fonts())