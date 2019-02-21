import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
girlImg = pygame.image.load('pinkgirl.png')
girlx = 10
girly = 10
direction = 'right'

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        girlx += 5
        if girlx == 280:
            direction = 'down'
    elif direction == 'down':
        girly += 5
        if girly == 220:
            direction = 'left'
    elif direction == 'left':
        girlx -= 5
        if girlx == 10:
            direction = 'up'
    elif direction == 'up':
        girly -= 5
        if girly == 10:
            direction = 'right'

    DISPLAYSURF.blit(girlImg, (girlx, girly))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
