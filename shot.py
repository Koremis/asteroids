import pygame
from circleshape import CircleShape
from constants import *


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.SHOT_RADIUS = SHOT_RADIUS

    def draw(self, screen):
        return pygame.draw.circle(
            screen, (255, 255, 255),
            (self.position.x, self.position.y), self.SHOT_RADIUS
        )

    def update(self, dt):
        self.position += self.velocity * PLAYER_SHOOT_SPEED * dt
        return self.position

