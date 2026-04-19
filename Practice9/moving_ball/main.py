import pygame
from ball import Ball

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))

red = (255, 0 , 0 )

ball = Ball()
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    ball.move(keys, width, height)

    screen.fill(red)
    ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()