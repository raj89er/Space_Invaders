import pygame

# Initialize Pygame
pygame.init()

# create the display, with a resolution of 800px height and 600px width
screen = pygame.display.set_mode((800, 600))

# add fuctionality to the close button
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

