import pygame
from settings import BULLET_IMAGE, BULLET_HIT_SOUND, ENEMY_BULLET, SCREEN_HEIGHT


class Bullets(pygame.sprite.Sprite):
    def __init__(self, level, x, y):
        super().__init__()
        self.level = level
        self.image = BULLET_IMAGE
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.y -= 5
        if self.rect.bottom < 0:
            self.kill()

        if pygame.sprite.spritecollide(self, self.level.alien_group, dokill=False):
            self.kill()
            self.level.alien.health -= 10
            BULLET_HIT_SOUND.play()

        if pygame.sprite.spritecollide(self, self.level.spacerock_group, dokill=False):
            self.kill()
            BULLET_HIT_SOUND.play()


class EnemyBullets(pygame.sprite.Sprite):
    def __init__(self, level, x, y) -> None:
        super().__init__()
        self.level = level
        self.image = ENEMY_BULLET
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.y += 5
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

        if pygame.sprite.spritecollide(self, self.level.player_group, dokill=False):
            self.kill()
            self.level.player.health -= 5
            BULLET_HIT_SOUND.play()

        if pygame.sprite.spritecollide(self, self.level.spacerock_group, dokill=False):
            self.kill()
            BULLET_HIT_SOUND.play()
