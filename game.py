import pygame
import sys
from background1 import Background1
from Tittle_Buttons import Tittle_Button
from Game1_Button import Crab_Race
from settings import Settings

from Game2_Button import Crab_Game
from game1 import Game1
from game2 import Game2
import sound_effects as se
#Help from Sebasteon Allen
#Help from Alexandra Adelman
#Help from Hava Szarafinski
#Help from Matt McClelland
#Yohan Afewerki
#Help from Peter Lee
#Help from Nick Zolovick

class MainGame:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.screen = pygame.display.set_mode((500, 300))
        self.x, self.y = self.screen.get_size()
        # print(self.x, self.y)

        self.crab_race_button = Crab_Race(self, 'Crab Race')
        self.bg_color = (11, 226, 245)
        self.game1 = Game1()
        self.game2 = Game2()
        self.crab_game_button = Crab_Game(self, 'Crab Game')
        pygame.display.set_caption("Crab Game")
        self.background1 = Background1(self)
        self.play_button = Tittle_Button(self, 'Crab Game!')
        se.halo.play().set_volume(2)
    def run_game(self):
        """runs the game"""
        while True:
            self._check_events()
            self._update_screen()
            pygame.display.flip()

    def _check_events(self):
        """responds to key presses"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)


    def _check_keydown_events(self, event):
        """responds to keydown events"""
        if event.key == pygame.K_q:
            sys.exit()

    def _check_play_button(self, mouse_pos):
        """checks to see when buttons have been pressed so that the new game can begin"""
        button_clicked1 = self.crab_race_button.rect.collidepoint(mouse_pos)
        button_clicked2 = self.crab_game_button.rect.collidepoint(mouse_pos)

        if button_clicked2 and not self.settings.game_active:
            self.settings.game_active = True
            se.halo.set_volume(1)
            self.game2.run_game2()
        if button_clicked1 and not self.settings.game_active:
            self.settings.game_active = True
            se.halo.set_volume(1)
            self.game1.run_game1()


    def _update_screen(self):
        """controls screen updates to include images and buttons"""
        self.screen.blit(pygame.transform.scale(self.background1.image, (self.x, self.y)), (0, 0))
        if not self.settings.game_active:
            self.play_button.draw_button()
            self.crab_race_button.draw_button()
            self.crab_game_button.draw_button()
        pygame.display.flip()


if __name__ == '__main__':
    ai = MainGame()
    ai.run_game()
