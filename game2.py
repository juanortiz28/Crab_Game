import pygame
import sys
from crabs import CrabsGame2
from crabs import SeaShells
from settings2 import Settings


class Game2:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.seashells = pygame.sprite.Group()
        self._create_shell_grid()
        self.bg_color = (0,0,0)
        self.crabs_2 = CrabsGame2(self)
#TODO: MAKE A GRID IN THE MIDDLE OF SHELLS WHERE THEY HAVE TO SHOOT THEM AND THEY GET POINTS WITH THE GOAL OF HITTING THE OTHER CRAB AND KILLING THEM (3 LIVES MAX)
#TODO: IF THEY DIE THEN RESET THE GAME, IF THEY DESTROY THE WHOLE GRID THEN MAKE IT WAIT LIKE TWO SECONDS BEFORE REAPERING AGAIN
#TODO: MAKE A SCORE BOX FOR BOTH CRABS

    def run_game2(self):
        while True:
            self._check_events2()
            self._update_screen2()
            self.crabs_2.update()

    def _create_shell_grid(self):
        red = pygame.image.load('images/red.png')
        red_height = red.get_height()
        shells = SeaShells(self)
        shells_width, shells_height = shells.rect.size
        space_x = self.settings.screen_width - (2* shells_width)
        number_shells_x = space_x // (2 * shells_width)
        # redheight = self.crabs_2.red_height
        space_y = (self.settings.screen_height - red_height)
        number_rows = space_y // (2 * shells_height)
        for row in range(number_rows):
            for shell_number in range(number_shells_x):
                self._create_shells(shell_number, row)

    def _create_shells(self, shell_number, row):
        #create an alien and place it in the row
        shell = SeaShells(self)
        shell_width, shell_height = shell.rect.size
        shell.x = shell_width + 2 * shell_width * shell_number
        shell.rect.x = shell.x
        shell.rect.y = shell_height + 2 * shell.rect.height * row
        self.seashells.add(shell)
    def _check_events2(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events2(event)
            if event.type == pygame.KEYUP:
                self._check_keyup_events2(event)
    def _check_keydown_events2(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_w:
            self.crabs_2.moving_up_red = True
        if event.key == pygame.K_x:
            self.crabs_2.moving_down_red = True
        if event.key == pygame.K_UP:
            self.crabs_2.moving_up_green = True
        if event.key == pygame.K_DOWN:
            self.crabs_2.moving_down_green = True

    def _check_keyup_events2(self, event):
        if event.key == pygame.K_w:
            self.crabs_2.moving_up_red = False
        if event.key == pygame.K_x:
            self.crabs_2.moving_down_red = False
        if event.key == pygame.K_UP:
            self.crabs_2.moving_up_green = False

        if event.key == pygame.K_DOWN:
            self.crabs_2.moving_down_green = False


    def _update_screen2(self):
        """updates the screen"""
        self.screen.fill((0, 0, 255))
        self.seashells.draw(self.screen)
        self.crabs_2.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    ai = Game2()
    ai.run_game2()