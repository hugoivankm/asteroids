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
    player = Player(x, y, PLAYER_RADIUS)

    while (True):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        black = (0, 0, 0)
        screen.fill(black)
        
        player.update(dt)
        player.draw(screen)
        
        pg.display.flip()
        dt = clock.tick(FPS) / 1000
    

if __name__ == "__main__":
    main()
