import pygame
from settings import SPACESHIP_IMG, SCREEN_WIDTH, BULLET_SOUND, RED, GREEN
from bullets import Bullets


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, game, position: tuple):
        super().__init__()
        self.game = game
        self.image = SPACESHIP_IMG
        self.image = pygame.transform.rotate(
            pygame.transform.scale(self.image, (50, 50)), 180)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.health = 100
        self.last_shot = pygame.time.get_ticks()

    def _movement(self):
        speed = 4
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= speed
        if keys[pygame.K_d] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += speed

    def _shoot(self):
        cooldown = 200
        time_now = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and time_now - self.last_shot > cooldown:
            bullet = Bullets(self.game, self.rect.centerx, self.rect.top)
            self.game.bullet_group.add(bullet)
            BULLET_SOUND.play()
            self.last_shot = time_now

    def _health_bar(self):
        bar_width = self.rect.width
        bar_height = 10
        bar_x = self.rect.x
        bar_y = self.rect.bottom + 5

        health_perc = max(0, self.health / 100.0)
        green_width = int(bar_width * health_perc)
        pygame.draw.rect(self.game.screen, RED,
                         (bar_x, bar_y, bar_width, bar_height))
        pygame.draw.rect(self.game.screen, GREEN,
                         (bar_x, bar_y, green_width, bar_height))

    def update(self):
        self._movement()
        self._shoot()
        self._health_bar()
