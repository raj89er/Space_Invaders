
import pygame
import random

# Initialize Pygame
pygame.init()

# Create the display window with a resolution of 800x600 pixels
screen = pygame.display.set_mode((800, 600))

# Set the window title and icon
pygame.display.set_caption("Space Invaders v 0.1")
icon = pygame.image.load("./images/icon.png")
pygame.display.set_icon(icon)

# Load images for player/enemy
playerImg = pygame.image.load("./images/spaceship.png")
enemyImg = pygame.image.load("./images/ufo01.png")

# Player properties
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Enemy properties
num_enemies = 5  # Number of enemies to spawn
enemies = []  # List to hold enemy objects

for _ in range(num_enemies):
    enemyX = random.randint(0, 736)
    enemyY = random.randint(50, 450)
    enemies.append((enemyX, enemyY))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

# Game Loop
running = True
while running:
    screen.fill((6, 57, 112)) # Fill the background with a blue color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle player controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                pass
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                playerY_change -= 0.1
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change -= 0.1
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_change += 0.1
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change += 0.1
        if event.type == pygame.KEYUP:
        #     # if event.key/ == pygame.K_BACKSPACE:
        #     #     pass
            if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_change = 0

    # Update player's position based on movement
    playerX += playerX_change
    playerY += playerY_change
    
    # Boundary checking for player
    playerX = min(max(playerX, 0), 736)
    playerY = min(max(playerY, 0), 568)


    # Draw the player & enemy on the screen
    player(playerX, playerY)
    # enemy(enemyX, enemyY)
    for enemyX, enemyY in enemies:
        enemy(enemyX, enemyY)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
