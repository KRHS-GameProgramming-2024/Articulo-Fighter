import pygame, sys, math, random
from Arm import *
from leg import *
from Player import *

pygame.init()

clock = pygame.time.Clock();

size = [900, 700]
screen = pygame.display.set_mode(size)
