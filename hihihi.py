import pygame
import random
import sys

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Đua Xe")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (169, 169, 169)

player_width = 50
player_height = 100
player_speed = 7
lane_width = 150

font = pygame.font.SysFont("Arial", 24)
game_over_font = pygame.font.SysFont("Arial", 48)

def show_score(score):
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

def show_game_over(score):
    game_over_text = game_over_font.render("Game Over!", True, RED)
    score_text = font.render(f"Final Score: {score}", True, BLACK)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 3))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))

def reset_game():
    global player_x, player_y, enemy_x, enemy_y, enemy_speed, score
    player_x = SCREEN_WIDTH // 2 - player_width // 2
    player_y = SCREEN_HEIGHT - player_height - 20
    enemy_x = random.randint(50, SCREEN_WIDTH - player_width - 50)
    enemy_y = -player_height
    enemy_speed = 5
    score = 0

def game_loop():
    global player_x, player_y, enemy_x, enemy_y, enemy_speed, score
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(GRAY)
        pygame.draw.rect(screen, WHITE, (50, 0, SCREEN_WIDTH - 100, SCREEN_HEIGHT))
        pygame.draw.line(screen, BLACK, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT), 5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 50:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width - 50:
            player_x += player_speed

        enemy_y += enemy_speed

        if enemy_y > SCREEN_HEIGHT:
            enemy_y = -player_height
            enemy_x = random.randint(50, SCREEN_WIDTH - player_width - 50)
            score += 1
            enemy_speed += 0.2  
        if (player_x < enemy_x + player_width and
            player_x + player_width > enemy_x and
            player_y < enemy_y + player_height and
            player_y + player_height > enemy_y):
            show_game_over(score)
            pygame.display.flip()
            pygame.time.wait(1000)  
            return  

        pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))
        pygame.draw.rect(screen, RED, (enemy_x, enemy_y, player_width, player_height))
        show_score(score)

        pygame.display.flip()
        clock.tick(60)

while True:
    reset_game()
    game_loop() 