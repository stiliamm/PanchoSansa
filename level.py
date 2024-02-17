import pygame
from spaceship import Spaceship
from aliens import Aliens
from rocks import SpaceRocks
from settings import *


class Level:
    def __init__(self, game, lvl_number: int) -> None:
        self.game = game
        self.lvl_number = lvl_number
        self.player_group = pygame.sprite.GroupSingle()
        self.bullet_group = pygame.sprite.Group()
        self.alien_group = pygame.sprite.Group()
        self.spacerock_group = pygame.sprite.Group()
        self.enemy_bullets_group = pygame.sprite.Group()
        self.player = Spaceship(self, PLAYER_POSITION)
        self.player_group.add(self.player)
        self.alien = Aliens(self, ALIEN_POSITION)
        self.alien_group.add(self.alien)
        self.spacerock = SpaceRocks()
        self.spacerock_group.add(self.spacerock)
        self.game._game_music()
        self.font = MENU_FONT

    def next_level(self):
        if pygame.sprite.spritecollide(self.player, self.spacerock_group, dokill=True) or self.player.health == 0:
            self.player.kill()
            self.game._stop_game_on_event("YOU LOOSE!")

        if self.alien.health == 0:
            self.alien.kill()
            self.game._stop_game_on_event("YOU WIN!")

    def update(self):
        self.player_group.update()
        self.alien_group.update()
        self.bullet_group.update()
        self.spacerock_group.update()
        self.enemy_bullets_group.update()

    def draw(self):
        self.player_group.draw(self.game.screen)
        self.bullet_group.draw(self.game.screen)
        self.alien_group.draw(self.game.screen)
        self.spacerock_group.draw(self.game.screen)
        self.enemy_bullets_group.draw(self.game.screen)
        level_text = self.font.render(f"Level: {self.lvl_number}", True, WHITE)
        self.game.screen.blit(level_text, (250, 550))
