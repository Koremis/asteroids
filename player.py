import pygame
from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED
)

class Player(CircleShape):
    def __init__(self, x, y):
        print("Player init")
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

        # in the player class
    def triangle(self):
        print("Player triangle")
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        print("Hello from Player draw")
        points = self.triangle()
        return pygame.draw.polygon(screen, (255, 255, 255), points, 2)

    def rotate(self, dt):
        return PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            turn_left = self.rotate(dt) - (self.rotate(dt) * 2)
            turn_left += self.rotation
            return turn_left
        if keys[pygame.K_s]:
            turn_right = self.rotate(dt)
            turn_right += self.rotation
            return turn_right
