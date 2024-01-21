import pygame
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FIRE_SOUND, ALIEN_IMAGE, ALIEN_COOLDOWN
from bullets import EnemyBullets
from spaceship import Spaceship


class Aliens(Spaceship):
    def __init__(self, level, position: tuple):
        super().__init__(level, position)
        self.level = level
        self.image = ALIEN_IMAGE
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH)
        self.rect.y = random.randint(0, SCREEN_HEIGHT)
        self.rect.center = position
        self.health = 100
        self.speedx = 2
        self.last_shot = pygame.time.get_ticks()

    def _movement(self):
        if self.rect.left <= 0:
            self.speedx = abs(self.speedx)
        elif self.rect.right >= SCREEN_WIDTH:
            self.speedx = -abs(self.speedx)
        self.rect.x += self.speedx

    def _shoot(self):
        time_now = pygame.time.get_ticks()

        if time_now - self.last_shot > ALIEN_COOLDOWN:
            alien_bullet = EnemyBullets(
                self.level, self.rect.centerx, self.rect.bottom)
            self.level.enemy_bullets_group.add(alien_bullet)
            pygame.mixer.Sound.set_volume(FIRE_SOUND, 0.05)
            FIRE_SOUND.play()
            self.last_shot = time_now

    def update(self):
        self._movement()
        self._shoot()
        self._health_bar()
