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

mode = "screen"

while True:
    mimage = pygame.image.load("Images/loading screens/Menu.png")
    mrect = mimage.get_rect()
    mbimage = pygame.image.load("Images/loading screens/Menubuttons.png")
    mbrect = mbimage.get_rect()
    mb2image = pygame.image.load("Images/loading screens/Menubuttons - copy.png")
    mb2rect = mb2image.get_rect()
    
    while mode == "screen":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == pygame.K_SPACE:
                    mode = "game"
        
        
        
        screen.blit(mimage, mrect)
        screen.blit(mbimage, mbrect)
        screen.blit(mb2image, mb2rect)
        
        pygame.display.flip()
        clock.tick(60)
        
    player = Player("TVBoi", 4, 30, [900/2, 700/2])
    bgimage = pygame.image.load("Images/Stages/temp_background.png")
    bgrect = bgimage.get_rect()
    
    while mode == "game":
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.goKey("left")
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.goKey("right")
                elif event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    player.goKey("up")
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.goKey("down")
                elif event.key == pygame.K_e:
                    player.punch()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.goKey("sleft")
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.goKey("sright")
                elif event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    player.goKey("sup")
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.goKey("sdown")

        counter = 0;
        
        
        player.update(fieldSize)
        
        
        screen.blit(bgimage, bgrect)
    
        screen.blit(player.image, player.rect)
        pygame.display.flip()
        clock.tick(60)
