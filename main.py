# This is a following of a video from https://www.youtube.com/watch?v=qPtKv9fSHZY&ab_channel=DotCSV with
# any corrections :)

# Imports
import numpy as np
import pygame
import time

# Constants
pauseExec = True
running = True

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
while running:

    newGameState = np.copy(gameState)

    screen.fill(bg)
    time.sleep(0.1)

    # Register keyboard and mouse events
    event = pygame.event.get()

    for action in event:
        if action.type == pygame.KEYDOWN:
            if action.key == pygame.K_SPACE:
                pauseExec = not pauseExec

            if action.key == pygame.K_q:
                running = not running

        mouseClick = pygame.mouse.get_pressed()

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[celX, celY] = not mouseClick[2]

    for y in range(0, nxC):
        for x in range(0, nyC):

            if not pauseExec:

                # Calculate number of neighbors
                n_neigh = gameState[(x - 1) % nxC, (y - 1) % nyC] + \
                          gameState[x % nxC, (y - 1) % nyC] + \
                          gameState[(x + 1) % nxC, (y - 1) % nyC] + \
                          gameState[(x - 1) % nxC, y % nyC] + \
                          gameState[(x + 1) % nxC, y % nyC] + \
                          gameState[(x - 1) % nxC, (y + 1) % nyC] + \
                          gameState[x % nxC, (y + 1) % nyC] + \
                          gameState[(x + 1) % nxC, (y + 1) % nyC]

                # Rule 1: A dead cell with three alive neighbor revives
                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1

                # Rule 2: A living cell with less than two or more than three living neighbors dies.
                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0

            # Background grill
            poly = [(x * dimCW, y * dimCH),
                    ((x + 1) * dimCW, y * dimCH),
                    ((x + 1) * dimCW, (y + 1) * dimCH),
                    (x * dimCW, (y + 1) * dimCW)]
            # Print grill and cells
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    # Actualize the game
    gameState = np.copy(newGameState)

    # Display game
    pygame.display.flip()
