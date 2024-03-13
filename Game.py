import pygame, sys, math, random
from Arm import *
from leg import *
from Player import *
from Fighter import *

pygame.init()

clock = pygame.time.Clock();

size = [900, 700]
fieldSize = [900, 525]
screen = pygame.display.set_mode(size)

counter = 0;
player = Player(4, 30, [900/2, 700/2])

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit();
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.goKey("left")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.goKey("right")
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                player.goKey("up")
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.goKey("down")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.goKey("sleft")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.goKey("sright")
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                player.goKey("sup")
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.goKey("sdown")


    player.update(fieldSize)
    
    bgimage = pygame.image.load("Images/Stages/temp_background.png")
    bgrect = bgimage.get_rect()
            
    screen.blit(bgimage, bgrect)
    screen.blit(player.image, player.rect)
    pygame.display.flip()
    clock.tick(60)
