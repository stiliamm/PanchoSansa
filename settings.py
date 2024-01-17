import pygame
pygame.mixer.init()
pygame.font.init()

RESOLUTION = SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
FPS = 120
PLAYER_POSITION = (int(SCREEN_WIDTH / 2), SCREEN_HEIGHT - 100)
ALIEN_POSITION = (int(SCREEN_WIDTH / 2), SCREEN_HEIGHT - 500)
ALIEN_COOLDOWN = 500
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROTATION = 0.002
SPACESHIP_IMG = pygame.image.load("./static/graphics/spaceship_yellow.png")
BACKGROUND = pygame.image.load("./static/graphics/moon.png")
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ROWS = 5
COLS = 5
GAME_SOUND = pygame.mixer.music.load("./static/audio/Cosmico_Theme.wav")
BULLET_SOUND = pygame.mixer.Sound("./static/audio/Cosmico_BulletHitSound.wav")
BULLET_HIT_SOUND = pygame.mixer.Sound(
    "./static/audio/Cosmico_BulletHitSound2.wav")
GAME_WIN_SOUND = pygame.mixer.Sound("./static/audio/Cosmico_GameWinSound.wav")
FIRE_SOUND = pygame.mixer.Sound("./static/audio/Fire.wav")
ROCK_IMAGE = pygame.image.load("./static/graphics/spacerock.png")
ALIEN_IMAGE = pygame.image.load("./static/graphics/alien5.png")
BULLET_IMAGE = pygame.image.load("./static/graphics/bullet.png")
WINNER_FONT = pygame.font.SysFont('Eight-Bit Madness', 50)
MENU_FONT = pygame.font.SysFont('Eight-Bit Madness', 36)
ENEMY_BULLET = pygame.image.load("./static/graphics/02.png")
