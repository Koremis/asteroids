import pygame
from shot import *

from asteroid import Asteroid
from asteroid_field import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Shot.containers = (updatable, drawable, shots)
    # shot = Shot(player.position.x, player.position.y)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        for obj in updatable:
            obj.update(dt)
        for ast in asteroids:
            if ast.collided(player):
                # screen.fill((0, 0, 0))
                print("Game over!")
                pygame.quit()
                quit()
            for shot in shots:
                if ast.collided(shot):
                    ast.kill()
                    shot.kill()

        screen.fill((0, 0, 0))
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
