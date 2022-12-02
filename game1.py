import random

import pygame
from settings2 import Settings
import sys
from finish_line import FinishLine
from Tittle_Buttons import Start_Game1
from Tittle_Buttons import Winner
from crabs import Crabs_New
# from Title_Menu import CrabGame
from home import Home
from game2 import Game2


class Game1:
    def __init__(self):
        """initializes the game, as well as the other modules and instances"""
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.bg_color = (0, 0, 255)
        self.settings = Settings()
        self.image = pygame.image.load('images/sky.jpg')
        self.crabs_new = Crabs_New(self)
        self.x, self.y = self.screen.get_size()
        self.image = pygame.transform.scale(self.image, (self.x, self.y))
        self.FinishLine = FinishLine(self, 'Finish Line!')
        self.start_button = Start_Game1(self, 'Choose your crab!')
        self.game2 = Game2()
        self.home = Home(self, 'CrabGame')
#TODO: ADD A TEXT BOX SAYING "CORRECT GUESSES:" FOLLOWED BY ANOTHER BOX WITH THE NUMBER OF CORRECT GUESSES THAT UPDATES EACH TIME THE USER GUESSES CORRECTLY
#TODO: ADD LIKE THREE LIVES TO GUESS CORRECTLY OTHERWISE THE GAME ENDS
#TODO: ADD SOUND THAT STARTS ONCE THE GAME STARTS, AND THEN ONCE THE WINNER IS ANNOUNCED PLAY ANOTHER CELEBRATION SONG
    def run_game1(self):
        """Runs the game with a while loop"""
        while True:
            self._check_events1()
            if self.settings.game_active:
                self.crabs_new.update()
            self._update_screen2()


    def _check_events1(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events1(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_pos = pygame.mouse.get_pos()
                self._check_buttons()


    def winner_crab(self):
        if self.settings.guess == 'RED':
            self.winner = Winner(self, 'RED WINS!')
            self.winner.draw_start_button()
        elif self.settings.guess == 'BLUE':
            self.winner = Winner(self, 'BLUE WINS!')
            self.winner.draw_start_button()
        elif self.settings.guess == 'GREEN':
            self.winner = Winner(self, 'GREEN WINS!')
            self.winner.draw_start_button()


    def check_finish_line(self):
        if self.crabs_new.rect_red.collidepoint(self.FinishLine.rect):
            self.settings.game_active = True
    def _check_keydown_events1(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_g:
            self.settings.game_active = True
            self.settings.guess = 'Green'
        elif event.key == pygame.K_r:
            self.settings.game_active = True
            self.settings.guess = 'Red'
        elif event.key == pygame.K_b:
            self.settings.game_active = True
            self.settings.guess = 'Blue'
        elif event.key == pygame.K_t:
            self.crabs_new.center_ship()
            self.crabs_new.blitme()
        # elif event.key ==

    def _check_buttons(self):
        """checks to see when buttons have been pressed so that the new game can begin"""
        home_button = self.home.rect.collidepoint(self.mouse_pos)
        if home_button and not self.settings.game_active:
            self.settings.game_active = True
            self.game2.run_game2()
        """I can not get the home thing to work"""
        start_button = self.start_button.rect.collidepoint(self.mouse_pos)
        blue_crab = self.crabs_new.rect_blue.collidepoint(pygame.mouse.get_pos())
        red_crab = self.crabs_new.rect_red.collidepoint(pygame.mouse.get_pos())
        green_crab = self.crabs_new.rect_green.collidepoint(pygame.mouse.get_pos())
        if blue_crab and not self.settings.game_active:
            self.settings.game_active = True
        if red_crab and not self.settings.game_active:
            self.settings.game_active = True
        if green_crab and not self.settings.game_active:
            self.settings.game_active = True

    def _update_screen2(self):
        self.screen.fill(self.bg_color)
        self.screen.blit(self.image, (0, 0))
        self.crabs_new.blitme()
        self.FinishLine.draw_button()
        self.home.draw_button()
        self.crabs_new.check_edges()
        self.winner_crab()

        # if not self.settings.game_active:
        #     self.start_button.draw_start_button()

        pygame.display.flip()

if __name__ == '__main__':
    ai = Game1()
    ai.run_game1()