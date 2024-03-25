import pygame

# Initialize Pygame
pygame.init()

# create the display, with a resolution of 800px height and 600px width
screen = pygame.display.set_mode((800, 600))

# TItle and Icon
pygame .display.set_caption("Space Invaders v 0.1")
icon= pygame.image.load("./images/icon.png")
pygame.display.set_icon(icon)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #background fill in RGB
    screen.fill((6,57,112))
    pygame.display.update()
