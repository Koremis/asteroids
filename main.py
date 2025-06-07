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
    game_over = False

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Shot.containers = (updatable, drawable, shots)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_p]:
                pygame.time.delay(100)
                pause(clock, screen, drawable, updatable, game_over)
            if keys[pygame.K_q]:
                pygame.quit()
                quit()

        for obj in updatable:
            obj.update(dt)

        for ast in asteroids:
            if ast.collided(player):
                pygame.time.delay(100)
                game_over = True
                pause(clock, screen, drawable, updatable, game_over)

            for shot in shots:
                if ast.collided(shot):
                    shot.kill()
                    ast.split(ast)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


def pause(clock, screen, drawable, updatable, game_over):

    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        screen.fill("black")

        if game_over:
            if keys[pygame.K_r]:
                main()
                return
            if keys[pygame.K_q]:
                pygame.quit()
                quit()
            for obj in updatable:
                obj.kill()
            for obj in drawable:
                obj.kill()
            """
            render game over text including directions for closing game
            or restarting
            """

        if not game_over:
            """
            render paused text including directions for closing game
            or restarting
            """
        if (
            keys[pygame.K_w] or
            keys[pygame.K_a] or
            keys[pygame.K_r] or
            keys[pygame.K_s]
        ):
            paused = False

        if keys[pygame.K_r]:
            main()
            return
        if keys[pygame.K_q]:
            pygame.quit()
            quit()

        pygame.display.flip()
        clock.tick(15)


if __name__ == "__main__":
    main()
