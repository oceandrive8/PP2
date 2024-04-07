import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (135, 206, 235)

# Screen dimensions
W= 400
H= 600

# Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over= font.render("Game Over", True, BLUE)

# Load background image
bg = pygame.image.load("materials/AnimatedStreet.png")

# Create a window
DISPLAYSURF = pygame.display.set_mode((W, H))
pygame.display.set_caption("Racing Game")

# Background music
pygame.mixer.music.load("materials/background.wav")
pygame.mixer.music.play(-1)

# Classes as actions
class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.image = pygame.image.load("materials/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), 0)
        self.speed = speed
        self.lap_count = 0  # Count of laps completed by the enemy, it's essential for level

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > H:
            self.rect.top = 0
            self.rect.center = (random.randint(40, W- 40), 0)
            self.lap_count += 1

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("materials/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < W:
            self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self, speed, weight):
        super().__init__()
        self.weight = weight  # Assigning different weights
        self.image = pygame.image.load("materials/Coin.png")
        self.speed = speed
        # Scale the image based on weight
        if self.weight == 1:
            self.image = pygame.transform.scale(self.image, (30, 30))
        elif self.weight == 2:
            self.image = pygame.transform.scale(self.image, (40, 40))
        elif self.weight == 3:
            self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), random.randint(-600, 0))

    def move(self):
        self.rect.move_ip(0, self.speed)

    def reset_position(self):
        self.rect.center = (random.randint(40, W - 40), random.randint(-600, 0))
        self.weight = random.choice([1, 1, 1, 2, 2, 3])  # Assigning different weights

def generate_coins(num_coins, speed):
    coins = pygame.sprite.Group()
    for _ in range(num_coins):
        coin = Coin(speed, random.choice([1, 1, 1, 2, 2, 3]))
        coins.add(coin)
    return coins

def increase_enemy_speed(enemy_group, new_speed):
    for enemy in enemy_group:
        enemy.speed = new_speed

# Initialize game objects
P1 = Player()
E1 = Enemy(speed=5)
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

SPEED = 5  # Set common speed for coins and enemies
coins = generate_coins(5, SPEED)  # Generate initial coins

# Game variables
LEVEL = 1
coin_score = 0  # Number of collected coins
COINS_TO_INCREASE_SPEED = 5  # Number of coins needed to increase enemy speed
ENEMY_SPEED_INCREMENT = 1  # Amount to increase enemy speed by

# Adding a new User event for increasing speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == INC_SPEED:
            SPEED += 0.5
            LEVEL += 1

    DISPLAYSURF.blit(bg, (0, 0))

    # Move and draw enemies
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # Check for collisions with enemies
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('materials/crash.wav').play()
        time.sleep(1)
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Move and draw coins
    for coin in coins:
        coin.move()
        DISPLAYSURF.blit(coin.image, coin.rect)
        if coin.rect.top > H:
            coin.reset_position()

    # Check for collisions with coins
    for coin in coins:
        if pygame.sprite.collide_rect(P1, coin):
            coin.reset_position()  # Reset coin position
            coin_score += coin.weight  # Increment coin score based on the coin's weight
            if coin_score >= COINS_TO_INCREASE_SPEED:
                increase_enemy_speed(enemies, E1.speed + ENEMY_SPEED_INCREMENT)
                COINS_TO_INCREASE_SPEED += 10  # Increase the threshold for next speed increase

    # Display level and coin score
    level_text = font_small.render(f"Level: {LEVEL}", True, BLACK)
    DISPLAYSURF.blit(level_text, (10, 10))
    coin_score_text = font_small.render(f"Coins: {coin_score}", True, BLACK)
    coin_score_rect = coin_score_text.get_rect()
    coin_score_rect.topright = (W - 10, 10)
    DISPLAYSURF.blit(coin_score_text, coin_score_rect)

    pygame.display.flip()
    FramePerSec.tick(FPS)

pygame.quit()
sys.exit()




