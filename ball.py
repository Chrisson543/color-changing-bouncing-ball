import pygame
import random
pygame.init()


class Ball:
    def __init__(self, screen):
        self.screen = screen
        self.x = screen.get_width() / 2
        self.y = screen.get_height() / 2
        self.radius = 10
        self.v_x = 0
        self.v_y = 0
        self.bounce_force = 20
        self.gravity = 1
        self.fall = False
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.screen_color = (0, 0, 0)

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def update(self):
        self.screen.fill(self.screen_color)
        self.draw()
        self.x = self.x
        self.y = self.y
        self.v_y += self.gravity
        self.y += self.v_y
        if (self.y + self.radius) >= self.screen.get_height():
            self.v_y = 0
            self.screen_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.v_y -= self.bounce_force