# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Shot
from constants import *
from player import Player


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    delta = 0

    # create group
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create player and add to group
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # create asteroid and add to group
    Asteroid.containers = (updatable, drawable, asteroid_group)
    AsteroidField.containers = (updatable)

    asteroid_field = AsteroidField()

    Shot.containers = (shot_group, drawable, updatable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for object in drawable:
            object.draw(screen)
        for object in updatable:
            object.update(delta)
        for object in asteroid_group:
            if object.collide_with(player):
                print("Game over!")
                return
            for bullet in shot_group:
                if object.collide_with(bullet):
                    object.split()
                    bullet.kill()

        pygame.display.flip()

        delta = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
