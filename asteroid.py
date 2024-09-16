from constants import *
from circleshape import CircleShape
import pygame as pg

class Asteroid (CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pg.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)