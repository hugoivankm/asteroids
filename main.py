import pygame as pg
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape


def main():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()
    dt = 0
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    
    updatable = pg.sprite.Group()
    drawable = pg.sprite.Group()
    asteroids = pg.sprite.Group()
    
    Player.containers = (updatable, drawable)
    player = Player(x, y, PLAYER_RADIUS)
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    
    
    while (True):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
     
        for obj in updatable:
            obj.update(dt)
        
        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("Game Over!")
                sys.exit(0)
                return        
        
        screen.fill("black")
            
        for obj in drawable:
            obj.draw(screen)
        
        pg.display.flip()
        
        # limit framerate
        dt = clock.tick(FPS) / 1000
    

if __name__ == "__main__":
    main()
