import random

import pygame
from settings2 import Settings
import sys
from finish_line import FinishLine
from Tittle_Buttons import Start_Game1
from Tittle_Buttons import Red_R
from Tittle_Buttons import Green_G
from Tittle_Buttons import Blue_B
from crabs import Crabs
from crabs import Crabs_New

from pygame.locals import*

# from Title_Menu import CrabGame
from home import Home

class Game1:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.bg_color = (0, 0, 255)
        self.settings = Settings()
        self.image = pygame.image.load('images/sky.jpg')
        self.crabs = Crabs(self)
        self.crabs_new = Crabs_New(self)
        self.x, self.y = self.screen.get_size()
        self.image = pygame.transform.scale(self.image, (self.x, self.y))
        self.FinishLine = FinishLine(self, 'Finish Line!')
        self.start_button = Start_Game1(self, 'Choose your crab! Key press or Click on it')
        self.crab_r = Red_R(self, 'R')
        self.crab_g = Green_G(self, 'G')
        self.crab_b = Blue_B(self, 'B')

        self.home = Home(self, 'Home!')
#TODO: ADD A TEXT BOX SAYING "CORRECT GUESSES:" FOLLOWED BY ANOTHER BOX WITH THE NUMBER OF CORRECT GUESSES THAT UPDATES EACH TIME THE USER GUESSES CORRECTLY
#TODO: ADD LIKE THREE LIVES TO GUESS CORRECTLY OTHERWISE THE GAME ENDS
#TODO: BEFORE EVEYTHING STARTS, CHOOSE YOUR GUESS THEN THEY START
#todo:
#TODO: JUST FINISH THIS GAME WITH THE GAME STOPPING ONCE ONE CRAB REACHES THE TOP AND THEN BLIT AN IMAGE OF THE WINNING CRAB UNDER A TEXT BOX SAYING "WINNER!!!"
#TODO: ADD SOUND THAT STARTS ONCE THE GAME STARTS, AND THEN ONCE THE WINNER IS ANNOUNCED PLAY ANOTHER CELEBRATION SONG
    def run_game1(self):
        while True:
            self._check_events1()
            if self.settings.game_active:
                self.crabs.update()
                self.crabs_new.update()
            self._update_screen2()


                # self.crabs.check_top()
                # pygame.display.flip()

    def _check_events1(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events1(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_pos = pygame.mouse.get_pos()
                self._check_buttons()

    # def create_crabs(self):
    #     self.red_crab_x = self.x / 6
    #     self.red_crab_y = self.y -50
    #     self.screen.blit(self.red_crab, (self.red_crab_x, self.red_crab_y))
    #     self.blue_crab_x = self.x / 2 - 30
    #     self.blue_crab_y = self.y - 50
    #     self.screen.blit(self.blue_crab, (self.blue_crab_x, self.blue_crab_y))
    #     self.green_crab_x = self.x - 300
    #     self.green_crab_y = self.y - 50
    #     self.screen.blit(self.green_crab, (self.green_crab_x, self.green_crab_y))
    # def crabs_go_up(self):
    #     self.blue_crab_y -= random.randint(0,10)
    #     self.green_crab_y -= random.randint(0, 10)
    #     self.red_crab_y -= random.randint(0, 10)


    # def check_finish_line(self):
    #     if pygame.sprite.spritecollideany(self.crabs.red_crab, self.FinishLine.):



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
        # elif event.key ==

    def _check_buttons(self):
        """checks to see when buttons have been pressed so that the new game can begin"""
        home_button = self.home.rect.collidepoint(self.mouse_pos)
        # if home_button and not self.settings.game_active:
        #     self.settings.game_active = True
        #
        #     self.menu.__init__()
        #     self.menu.run_game()
        """I can not get the home thing to work"""
        start_button = self.start_button.rect.collidepoint(self.mouse_pos)
        blue_crab = self.crabs_new.rect_blue.collidepoint(pygame.mouse.get_pos())
        if blue_crab and not self.settings.game_active:
            self.settings.game_active = True
            self.settings.guess = 'RED'
            #TODO: FIX CAUSE it only reacts when i click at (0,0)
        # elif start_button and not self.settings.game_active:
        #     self.settings.game_active = True
        #     self.settings.guess = True
        #     print(self.crabs.red_crab.get_rect())
        # if button_clicked1 and not self.settings.game_active:
        #     self.settings.game_active = True
        #     se.background_lobby_sound.set_volume(0)
        #     self.game1.run_game1()
    # def start_game(self):
    #     self.screen.draw.text()

    def _update_screen2(self):
        self.screen.fill(self.bg_color)
        self.screen.blit(self.image, (0, 0))
        # self.crabs.create_crabs()
        self.crabs_new.blitme()
        self.FinishLine.draw_button()
        self.home.draw_button()
        # self.create_crabs()
        # self.screen.blit(self.red_crab, (self.x / 6, self.y - 50))
        # self.screen.blit(self.red_crab, (self.x / 2 - 30, 0))
        # self.screen.blit(self.red_crab, (self.x - 300, 0))


        # self.screen.blit(self.images_crabs.red, (0, 0))
        if not self.settings.game_active:
            self.start_button.draw_start_button()
            self.crab_r.draw_start_button()
            self.crab_g.draw_start_button()
            self.crab_b.draw_start_button()

        pygame.display.flip()

if __name__ == '__main__':
    ai = Game1()
    ai.run_game1()