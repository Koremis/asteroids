import pygame

from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        print("Hello from Asteroid init")

    def draw(self, screen):
        print("Hello from Asteroid draw")
        return pygame.draw.circle(
            screen, (255, 255, 255), self.position, self.radius, 2
        )

    def update(self, dt):
        self.position += self.velocity * dt
        return self.position
