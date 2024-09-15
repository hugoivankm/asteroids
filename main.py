import pygame as pg
from constants import *
from player import Player



def main():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()
    dt = 0
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    
    updatable = pg.sprite.Group()
    drawable = pg.sprite.Group()
    
    Player.containers = (updatable, drawable)
    player = Player(x, y, PLAYER_RADIUS)

    while (True):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
     
        for obj in updatable:
            obj.update(dt)
        
        screen.fill("black")
            
        for obj in drawable:
            obj.draw(screen)
        
        pg.display.flip()
        
        # limit framerate
        dt = clock.tick(FPS) / 1000
    

if __name__ == "__main__":
    main()
