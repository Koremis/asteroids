
import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # print("Hello from CircleShape init")
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        # print(self.position)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collided(self, other):
        distance = pygame.math.Vector2.distance_to(
            self.position, other.position)
        combined_radius = self.radius + other.radius
        if distance <= combined_radius:
            return True
