import pygame

import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, (255, 255, 255), self.position, self.radius, 2
        )

    def split(self, dt):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        rand_angle = random.uniform(20, 50)
        child_radius = self.radius - ASTEROID_MIN_RADIUS

        child1 = Asteroid(self.position.x, self.position.y, child_radius)
        child1_angle = self.velocity.rotate(rand_angle)
        child1.velocity = child1_angle * 1.2

        child2 = Asteroid(self.position.x, self.position.y, child_radius)
        child2_angle = self.velocity.rotate(-rand_angle)
        child2.velocity = child2_angle * 1.2

    def update(self, dt):
        self.position += self.velocity * dt
        return self.position
