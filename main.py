# This is a following of a video from https://www.youtube.com/watch?v=qPtKv9fSHZY&ab_channel=DotCSV with
# any corrections :)

# Imports
import numpy as np
import pygame

# Init
pygame.init()

# Screen values
width, height = 1000, 1000
screen = pygame.display.set_mode((height, width))

# Background painting
bg = 25, 25, 25
screen.fill(bg)

# Number of cells
nxC, nyC = 25, 25

# Cell dimensions
dimCW = width / nxC
dimCH = height / nyC

# Cell state (1 -> alive 0 -> dead)
gameState = np.zeros((nxC, nyC))  # np.zero creates a multidimensional array with zeros

# Main loop
while True:
    for y in range(0, nxC):
        for x in range(0, nyC):
            # Calculate number of neighbors
            n_neigh = gameState[(x - 1) % nxC, (y - 1) % nyC] + \
                      gameState[x % nxC, (y - 1) % nyC] + \
                      gameState[(x + 1) % nxC, (y - 1) % nyC] + \
                      gameState[(x - 1) % nxC, y % nyC] + \
                      gameState[(x + 1) % nxC, y % nyC] + \
                      gameState[(x - 1) % nxC, (y + 1) % nyC] + \
                      gameState[x % nxC, (y + 1) % nyC] + \
                      gameState[(x + 1) % nxC, (y + 1) % nyC]

            # Background grill
            poly = [(x * dimCW, y * dimCH),
                    ((x + 1) * dimCW, y * dimCH),
                    ((x + 1) * dimCW, (y + 1) * dimCH),
                    (x * dimCW, (y + 1) * dimCW)]
            # Print grill
            pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
    # Display game
    pygame.display.flip()
