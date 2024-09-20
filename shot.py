from constants import *
from circleshape import CircleShape
import pygame as pg

class Shot(CircleShape):
    def __init__(self, position):
        super().__init__(position.x, position.y, radius=SHOT_RADIUS)
        
    def draw(self, screen):
        pg.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)