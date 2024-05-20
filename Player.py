import pygame, sys, math
from Fighter import *

class Player(Fighter):
    def __init__(self, name, maxSpeed=4, jumpHieght=15, startPos=[0,0]):
        Fighter.__init__(self, name, [0,0], startPos)
        self.maxSpeed = maxSpeed
        self.jumpHieght = jumpHieght
        
        
    def goKey(self, direction):
        if direction == "left":
            self.heading = "moving left"

        elif direction == "right":
            self.heading = "moving right"
        elif direction == "up" and not self.jumping:
            self.jump()
            self.speedy = -self.jumpHieght
        elif direction == "down":
            self.speedy = self.maxSpeed
        elif direction == "sleft":
            self.heading = "stoping left"
        elif direction == "sright":
            self.heading = "stoping right"
        elif direction == "sup":
            self.speedy += 0
        elif direction == "sdown":
            self.speedy = 0
            
    def update(self, size):
        Fighter.update(self, size)
        
        if self.heading == "moving left" and self.speedx > -self.maxSpeed:
            self.speedx -= 1
            
        if self.heading == "moving right" and self.speedx < self.maxSpeed:
            self.speedx += 1
            
            
        if self.heading == "stoping left" and self.speedx < 0:
            self.speedx += 1
        elif self.heading == "stoping left":
            self.heading = "standing"
            
        if self.heading == "stoping right" and self.speedx > 0:
            self.speedx -= 1
        elif self.heading == "stoping right":
            self.heading = "standing"
    
        

    
