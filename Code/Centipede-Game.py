import pygame
from sys import exit

pygame.init()
# Display a window of size 1000x1000 pixels can be changed later
screen = pygame.display.set_mode((1000,1000))

# Keeps the window open and allows for quitting
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()