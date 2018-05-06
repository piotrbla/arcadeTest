import pygame
from pygame.locals import *


def do_quit():
    pygame.quit()
    exit(0)


pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
keys = [False, False, False, False]
player_position = [100, 100]

player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")

while 1:
    screen.fill(0)
    for x in range(width // grass.get_width() + 1):
        for y in range(height // grass.get_height() + 1):
            screen.blit(grass, (x * 100, y * 100))
    screen.blit(castle, (0, 30))
    screen.blit(castle, (0, 135))
    screen.blit(castle, (0, 240))
    screen.blit(castle, (0, 345))
    screen.blit(player, player_position)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            do_quit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            elif event.key == K_a:
                keys[1] = True
            elif event.key == K_s:
                keys[2] = True
            elif event.key == K_d:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            elif event.key == pygame.K_a:
                keys[1] = False
            elif event.key == pygame.K_s:
                keys[2] = False
            elif event.key == pygame.K_d:
                keys[3] = False
            elif event.key == pygame.K_ESCAPE:
                do_quit()
    if keys[0]:
        player_position[1] -= 5
    elif keys[2]:
        player_position[1] += 5
    if keys[1]:
        player_position[0] -= 5
    elif keys[3]:
        player_position[0] += 5
