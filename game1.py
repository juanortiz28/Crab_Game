import time
import pygame
from settings2 import Settings
import sys
from finish_line import FinishLine
from Tittle_Buttons import Start_Game1
from Tittle_Buttons import Winner
from Tittle_Buttons import Home
from Tittle_Buttons import Start_Over
from Tittle_Buttons import Guess_Correct
from Tittle_Buttons import Correct_Guess_Counter
from crabs import Crabs_New
from game2 import Game2
import sound_effects as se

#TODO: FIX HOW THE SCORE GOES UP SO MUCH

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
        self.star_over = Start_Over(self, 'Press T to go again')
        self.sb = Correct_Guess_Counter(self)
        self.game2 = Game2()
        self.home = Home(self, 'Click for CrabGame')
        self.guess_text = Guess_Correct(self, 'Correct Guesses:')
    def run_game1(self):
        """Runs the game with a while loop"""
        while True:
            self._check_events1()
            if self.settings.race:
                self.crabs_new.update()
            self._update_screen2()


    def _check_events1(self):
        """checks for key and mouse presses and then calls a function to check what to do"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events1(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_pos = pygame.mouse.get_pos()
                self._check_buttons()


    def winner_crab(self):
        """after a crab reaches the top, it will read which guess did you make, and then sho"""
        if self.settings.winner_Crab == 'RED':
            self.winner = Winner(self, 'RED WINS!')
            self.winner.draw_start_button()
            self.home.draw_button()
            self.star_over.draw_button()
            self.guess_text.draw_button()
            if self.settings.guess == 'Red':
                self.settings.correct_guesses += 1
                self.settings.guess = False
            self.sb.prep_start()
            self.sb.show_score()
            se.sponge.stop()

        elif self.settings.winner_Crab == 'BLUE':
            self.winner = Winner(self, 'BLUE WINS!')
            self.winner.draw_start_button()
            self.home.draw_button()
            self.star_over.draw_button()
            self.guess_text.draw_button()
            if self.settings.guess == 'Blue':
                self.settings.correct_guesses += 1
                self.settings.guess = False
            self.sb.prep_start()
            self.sb.show_score()
            se.sponge.stop()



        elif self.settings.winner_Crab == 'GREEN':
            self.winner = Winner(self, 'GREEN WINS!')
            self.winner.draw_start_button()
            self.home.draw_button()
            self.star_over.draw_button()
            self.guess_text.draw_button()
            if self.settings.guess == 'Green':
                self.settings.correct_guesses += 1
                self.settings.guess = False
            self.sb.prep_start()
            self.sb.show_score()
            se.sponge.stop()
            se.halo.play()


    def _check_keydown_events1(self, event):
        """reacts to keypresses down"""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_g:
            self.settings.guess = 'Green'
            self.begin_race()


        elif event.key == pygame.K_r:
            self.settings.guess = 'Red'
            self.begin_race()


        elif event.key == pygame.K_b:
            self.settings.guess = 'Blue'
            self.begin_race()


        elif event.key == pygame.K_t:
            self.restart()


    def begin_race(self):
        se.sponge.play()
        se.halo.stop()
        time.sleep(4)
        self.settings.game_active = True
        self.settings.race = True

    def restart(self):
        self.settings.game_active = False
        self.settings.race = False
        self.settings.guess = False
        self.settings.winner_Crab = False
        self.crabs_new.center_crab()
        self.crabs_new.blitme()
        se.sponge.stop()

    def _check_buttons(self):
        """checks to see when buttons have been pressed so that the new game can begin"""
        home_button = self.home.rect.collidepoint(self.mouse_pos)
        if home_button and not self.settings.game_active:
            se.halo.stop()
            self.game2.run_game2()
        blue_crab = self.crabs_new.rect_blue.collidepoint(pygame.mouse.get_pos())
        red_crab = self.crabs_new.rect_red.collidepoint(pygame.mouse.get_pos())
        green_crab = self.crabs_new.rect_green.collidepoint(pygame.mouse.get_pos())
        if blue_crab and not self.settings.game_active:
            self.settings.guess = 'Blue'
            self.begin_race()

        if red_crab and not self.settings.game_active:
            self.settings.guess = 'Red'
            self.begin_race()

        if green_crab and not self.settings.game_active:
            self.settings.guess = 'Green'
            self.begin_race()


    def _update_screen2(self):
        """updates the screen"""
        self.screen.blit(self.image, (0, 0))
        self.crabs_new.blitme()
        self.FinishLine.draw_button()
        self.crabs_new.check_edges()
        self.winner_crab()

        if not self.settings.game_active:
            self.start_button.draw_start_button()
            self.home.draw_button()
        pygame.display.flip()

if __name__ == '__main__':
    ai = Game1()
    ai.run_game1()