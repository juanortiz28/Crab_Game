import pygame
from settings2 import Settings
import sys
from finish_line import FinishLine
# from Title_Menu import CrabGame
from home import Home
import crabs

class Game1:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.bg_color = (0, 0, 255)
        self.settings = Settings()
        self.image = pygame.image.load('images/sky.jpg')
        self.x, self.y = self.screen.get_size()
        self.image = pygame.transform.scale(self.image, (self.x, self.y))
        # self.menu = CrabGame()
        self.FinishLine = FinishLine(self, 'Finish Line!')
        self.red_crab = pygame.image.load('images/red.png')
        self.green_crab = pygame.image.load('images/green.png')
        self.blue_crab = pygame.image.load('images/blue.png')

        self.home = Home(self, 'Home!')

    def run_game1(self):
        while True:
            self._check_events1()
            self._update_screen2()
            pygame.display.flip()

    def _check_events1(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events1(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_buttons(mouse_pos)

    def create_crabs(self):
        self.red_crab_x = self.x / 6
        self.red_crab_y = self.y -50
        self.screen.blit(self.red_crab, (self.red_crab_x, self.red_crab_y))
        self.blue_crab_x = self.x / 2 - 30
        self.blue_crab_y = self.y - 50
        self.screen.blit(self.blue_crab, (self.blue_crab_x, self.blue_crab_y))
        self.green_crab_x = self.x - 300
        self.green_crab_y = self.y - 50
        self.screen.blit(self.green_crab, (self.green_crab_x, self.green_crab_y))
    # def crabs_go_up(self):
    #     while




    def _check_keydown_events1(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        # elif event.key ==

    def _check_buttons(self, mouse_pos):
        """checks to see when buttons have been pressed so that the new game can begin"""
        home_button = self.home.rect.collidepoint(mouse_pos)
        # if home_button and not self.settings.game_active:
        #     self.menu.run_game()
        """I can not get the home thing to work"""
        # if button_clicked1 and not self.settings.game_active:
        #     self.settings.game_active = True
        #     se.background_lobby_sound.set_volume(0)
        #     self.game1.run_game1()

    def _update_screen2(self):
        self.screen.fill(self.bg_color)
        self.screen.blit(self.image, (0, 0))
        self.create_crabs()
        # self.screen.blit(self.red_crab, (self.x / 6, self.y - 50))
        # self.screen.blit(self.red_crab, (self.x / 2 - 30, 0))
        # self.screen.blit(self.red_crab, (self.x - 300, 0))


        # self.screen.blit(self.images_crabs.red, (0, 0))
        if not self.settings.game_active:
          self.FinishLine.draw_button()
          self.home.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    ai = Game1()
    ai.run_game1()