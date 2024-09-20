from constants import *
from circleshape import CircleShape
import pygame as pg
import random

class Asteroid (CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pg.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        
        is_small = (self.radius <= ASTEROID_MIN_RADIUS) 
        if is_small:
            return 
        
        random_angle = random.uniform(20, 50)
        
        plus_rotated_vector = self.velocity.rotate(random_angle)
        minus_rotated_vector = self.velocity.rotate(-random_angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        first = Asteroid(self.position.x, self.position.y, new_radius)
        first.velocity = plus_rotated_vector * 1.2
        
        second = Asteroid(self.position.x, self.position.y, new_radius)
        second.velocity = minus_rotated_vector * 1.2
        
        
        