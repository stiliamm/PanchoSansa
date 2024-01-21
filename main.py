import pygame
import sys
from settings import *
from spaceship import Spaceship
from aliens import Aliens
from rocks import SpaceRocks
from level import Level


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(RESOLUTION)
        self.background = BACKGROUND
        self.background = pygame.transform.scale(self.background, RESOLUTION)
        self.in_menu = True
        self.is_running = True
        self._new_game()

    def _new_game(self):
        self.level = Level(self)

    def _game_music(self):
        self.game_music = GAME_SOUND
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def _stop_game_on_event(self, text):
        pygame.mixer.music.stop()
        GAME_WIN_SOUND.play()
        draw_text = WINNER_FONT.render(text, 1, BLACK)
        self.screen.fill(WHITE)
        self.screen.blit(draw_text, (SCREEN_WIDTH/2 - draw_text.get_width() /
                                     2, SCREEN_HEIGHT/2 - draw_text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(5000)
        self._new_game()

    def main_menu(self):
        self.screen.blit(self.background, (0, 0))
        self.font = MENU_FONT
        self.text = self.font.render("Press ENTER to start", True, WHITE)
        self.text_rect = self.text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(self.text, self.text_rect)
        pygame.display.flip()

    def update(self):
        self.clock.tick(FPS)
        self.level.update()
        pygame.display.set_caption('Panchosansa')
        pygame.display.flip()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.level.draw()

    def events_handle(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and (
                    event.key == pygame.K_RETURN and self.in_menu):
                self.in_menu = False
            elif event.type == pygame.KEYDOWN and (
                    event.key == pygame.K_ESCAPE and self.is_running):
                self.in_menu = True

    def run(self):
        while self.is_running:
            self.events_handle()
            if self.in_menu:
                self.main_menu()
            else:
                self.level.next_level()
                self.update()
                self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()
