import pygame
import sys
from ball import Ball

pygame.init()

screen_width = 800
screen_height = 600
screen_dim = (screen_width, screen_height)
screen_color = [0, 0, 0]
screen = pygame.display.set_mode(screen_dim)
clock = pygame.time.Clock()

ball1 = Ball(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    ball1.update()
    pygame.display.update()
    clock.tick(60)
