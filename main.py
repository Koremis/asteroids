from constants import (
SCREEN_WIDTH,
SCREEN_HEIGHT)
from player import Player
import pygame


def main():
    pygame.init()
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    #updatable.add(player, asteroid, asteroid_field, shot)
    updatable.add(player)
    #drawable.add(player, shots, asteroid)
    drawable.add(player)
    Player.containers = (updatable, drawable)
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        updatable.update(dt)
        for draw in drawable:
            draw.draw(screen)
        dt = clock.tick(60) / 1000
        pygame.display.flip()


if __name__ == "__main__":
    main()
