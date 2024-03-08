import pygame, sys, math
from PlayerCollide import *

class Player(Fighter):
    def __init__(self, maxSpeed=4, startPos=[0,0]):
        Fighter.__init__(self, "Images/Player/TVBoi/TV_boy.png", [0,0], startPos)
        self.maxSpeed = maxSpeed
        
    def goKey(self, direction):
        if direction == "left":
            self.speedx = -self.maxSpeed
        elif direction == "right":
            self.speedx = self.maxSpeed
        elif direction == "up":
            self.speedy = -self.maxSpeed
        elif direction == "down":
            self.speedy = self.maxSpeed
        elif direction == "sleft":
            self.speedx = 0
        elif direction == "sright":
            self.speedx = 0
        elif direction == "sup":
            self.speedy = 0
        elif direction == "sdown":
            self.speedy = 0

