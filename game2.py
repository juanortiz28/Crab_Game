import pygame
import sys
from crabs import Crabs_Game2


class Game2:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.red_crab = pygame.image.load('images/red.png')
        self.red_crab = pygame.transform.rotate(self.red_crab, -90)
        self.bg_color = (0,0,0)
        self.crabs = Crabs_Game2(self)
#TODO: MAKE A GRID IN THE MIDDLE OF SHELLS WHERE THEY HAVE TO SHOOT THEM AND THEY GET POINTS WITH THE GOAL OF HITTING THE OTHER CRAB AND KILLING THEM (3 LIVES MAX)
#TODO: IF THEY DIE THEN RESET THE GAME, IF THEY DESTROY THE WHOLE GRID THEN MAKE IT WAIT LIKE TWO SECONDS BEFORE REAPERING AGAIN
#TODO: MAKE A SCORE BOX FOR BOTH CRABS

    def run_game2(self):
        while True:
            self.screen.fill(self.bg_color)
            self.crabs.create_crabs()
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

if __name__ == '__main__':
    ai = Game2()
    ai.run_game2()