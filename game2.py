import pygame
import sys
from crabs import CrabsGame2
from settings2 import Settings
from Tittle_Buttons import Home
from Tittle_Buttons import Start_Game2
from bullets import Bullet
from bullets import Bullet_2
import sound_effects as se


class Game2:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.angle = -90
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.title = Start_Game2(self, 'Go ahead and move around and shoot!')
        self.game1_button = Home(self, 'CrabRace!')
        self.bg_color = (0,0,0)
        self.bullets = pygame.sprite.Group()
        self.bullets_2 = pygame.sprite.Group()
        self.crabs_2 = CrabsGame2(self)

    def run_game2(self):
        while True:
            self._check_events2()
            self._update_screen2()
            self.crabs_2.update()
            self._update_bullets()
            self._update_bullets_2()
    def _fire_bullets(self):
        if len(self.bullets) < 4:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            se.bullet.play()

    def _fire_bullets_2(self):
        if len(self.bullets_2) < 4:
            new_bullet_2 = Bullet_2(self)
            self.bullets_2.add(new_bullet_2)
            se.bullet.play()

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_bullets_2(self):
        self.bullets_2.update()
        for bullet in self.bullets_2.copy():
            if bullet.rect.bottom <= 0:
                self.bullets_2.remove(bullet)

    def _check_events2(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events2(event)
            if event.type == pygame.KEYUP:
                self._check_keyup_events2(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_pos = pygame.mouse.get_pos()
    def _check_keydown_events2(self, event):
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        if event.key == pygame.K_w:
            self.crabs_2.moving_up_red = True
        if event.key == pygame.K_s:
            self.crabs_2.moving_down_red = True
        if event.key == pygame.K_a:
            self.crabs_2.moving_left_red = True
        if event.key == pygame.K_d:
            self.crabs_2.moving_right_red = True
        if event.key == pygame.K_UP:
            self.crabs_2.moving_up_green = True
        if event.key == pygame.K_DOWN:
            self.crabs_2.moving_down_green = True
        if event.key == pygame.K_RIGHT:
            self.crabs_2.moving_right_green = True
        if event.key == pygame.K_LEFT:
            self.crabs_2.moving_left_green = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()
        elif event.key == pygame.K_RSHIFT:
            self._fire_bullets_2()

    def _check_keyup_events2(self, event):
        if event.key == pygame.K_w:
            self.crabs_2.moving_up_red = False
        if event.key == pygame.K_a:
            self.crabs_2.moving_left_red = False
        if event.key == pygame.K_d:
            self.crabs_2.moving_right_red = False
        if event.key == pygame.K_s:
            self.crabs_2.moving_down_red = False
        if event.key == pygame.K_UP:
            self.crabs_2.moving_up_green = False
        if event.key == pygame.K_DOWN:
            self.crabs_2.moving_down_green = False
        if event.key == pygame.K_LEFT:
            self.crabs_2.moving_left_green = False
        if event.key == pygame.K_RIGHT:
            self.crabs_2.moving_right_green = False

    def _update_screen2(self):
        """updates the screen"""
        self.screen.fill((0, 0, 255))
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for bullet in self.bullets_2.sprites():
            bullet.draw_bullet()
        self.crabs_2.blitme()
        self.title.draw_start_button()
        pygame.display.flip()

if __name__ == '__main__':
    ai = Game2()
    ai.run_game2()