import pygame
import sys
from finish_line import FinishLine
from background1 import Crabs


class Game1:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.bg_color = (0, 0, 255)
        self.FinishLine = FinishLine(self, 'Finish Line!')
        self.images_crabs = Crabs(self)

    def run_game1(self):
        while True:
            # self.screen.fill(self.bg_color)
            self.FinishLine.draw_button()
            self._check_events1()
            self._update_screen2()
            pygame.display.flip()

    def _check_events1(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events1(event)

    def _check_keydown_events1(self, event):
        if event.key == pygame.K_q:
            sys.exit()

    def _update_screen2(self):
        self.screen.fill(self.bg_color)
        self.screen.blit(pygame.transform.scale(self.images_crabs.red, (1500, 900)), (0, 0))
        # if not self.settings.game_active:
        #     self.play_button.draw_button()
        #     self.crab_race_button.draw_button()
        #     self.crab_game_button.draw_button()
        pygame.display.flip()

