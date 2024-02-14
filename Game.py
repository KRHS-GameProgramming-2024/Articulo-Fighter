import pygame, sys, math, random
from Arm import *
from leg import *
from Player import *

pygame.init()

clock = pygame.time.Clock();

size = [900, 700]
screen = pygame.display.set_mode(size)

bgimage = pygame.image.load("Images/Stages/temp_background.png")
bgrect = bgimage.get_rect()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit();
            
    screen.blit(bgimage, bgrect)
    pygame.display.flip()
    clock.tick(60)
