import pygame

# Initialize Pygame
pygame.init()

# create the display, with a resolution of 800px width and 600px heigth
screen = pygame.display.set_mode((800, 600))

# TItle and Icon
pygame .display.set_caption("Space Invaders v 0.1")
icon= pygame.image.load("./images/icon.png")
pygame.display.set_icon(icon)

# draw player on display on x and y coordinates relative to the top left corner
playImg = pygame.image.load("./images/spaceship.png")
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0


def player(x,y):
    screen.blit(playImg, (x, y))

# Game Loop
running = True
while running:
    
    #background fill in RGB. placed on top to ensure it's the base layer
    screen.fill((6,57,112))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        # controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                pass
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change -= 0.1
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change += 0.1
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                playerY_change -= 0.1
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_change += 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_BACKSPACE:
                pass
            if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change
    
    player(playerX, playerY)

    pygame.display.update()
