import pygame

pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

player = pygame.image.load("resources/images/dude.png")

while 1:
    screen.fill(0)
    screen.blit(player, (100, 100))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
