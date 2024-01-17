import pygame
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, ROCK_IMAGE


class SpaceRocks(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ROCK_IMAGE
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-self.rect.height, -50)
        self.speedy = 5
        self.health = 50

    def update(self):
        self.rect.y += self.speedy
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randint(-self.rect.height, -50)
