import pygame
import random
import sys

# 1. Setup Configuration
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Dodger")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Player properties
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - player_size * 2
player_speed = 7

# Enemy properties
enemy_size = 50
enemy_x = random.randint(0, WIDTH - enemy_size)
enemy_y = 0
enemy_speed = 5

score = 0
font = pygame.font.SysFont("monospace", 35)

# 2. Main Game Loop
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movement Logic
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Enemy Logic
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = 0 - enemy_size
        enemy_x = random.randint(0, WIDTH - enemy_size)
        score += 1
        enemy_speed += 0.2 # Make it harder over time

    # Collision Detection
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)
    
    if player_rect.colliderect(enemy_rect):
        print(f"Game Over! Your score: {score}")
        running = False

    # 3. Drawing
    pygame.draw.rect(screen, BLUE, player_rect)
    pygame.draw.rect(screen, RED, enemy_rect)

    # Display Score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60) # Limits the game to 60 frames per second
