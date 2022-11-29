import pygame
import sys


class Game2:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.bg_color = (0,0,0)

    def run_game2(self):
        while True:
            self.screen.fill(self.bg_color)
            self._check_events2()
            pygame.display.flip()

    def _check_events2(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events2(event)
    def _check_keydown_events2(self, event):
        if event.key == pygame.K_q:
            sys.exit()