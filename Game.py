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
        
    player = Player("TVBoi", 4, 30, [900/4, 700/2])
    player2 = Player("Frank", 4, 30, [900*3/4, 700/2])
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
                if event.key == pygame.K_j:
                    player2.goKey("left")
                elif event.key == pygame.K_l:
                    player2.goKey("right")
                elif event.key == pygame.K_i:
                    player2.goKey("up")
                elif event.key == pygame.K_k:
                    player2.goKey("down")
                elif event.key == pygame.K_o:
                    player2.punch()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.goKey("sleft")
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.goKey("sright")
                elif event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    player.goKey("sup")
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.goKey("sdown")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.goKey("sleft")
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.goKey("sright")
                elif event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    player.goKey("sup")
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.goKey("sdown")
                if event.key == pygame.K_j:
                    player2.goKey("sleft")
                elif event.key == pygame.K_l:
                    player2.goKey("sright")
                elif event.key == pygame.K_i:
                    player2.goKey("sup")
                elif event.key == pygame.K_k:
                    player2.goKey("sdown")


        counter = 0;
        
        
        player.update(fieldSize)
        player2.update(fieldSize)
        
        screen.blit(bgimage, bgrect)
    
        screen.blit(player.image, player.rect)
        screen.blit(player2.image, player2.rect)
        pygame.display.flip()
        clock.tick(60)
