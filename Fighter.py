import pygame, sys, math

class Fighter():
    def __init__(self, name, speed = [0,0], startPos = [0,0]):
        self.baseImage = pygame.image.load("Images/Player/"+name+"/"+name+".png")
        self.punchImages = pygame.image.load("Images/Player/"+name+"/"+name+"Punching.png")
        self.image = self.baseImage
        self.rect = self.image.get_rect()
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.rad = (self.rect.height/2 + self.rect.width/2)/2
        
        self.rect = self.rect.move(startPos)
        
        self.gravity = 1.25
        self.jumping = False

        self.punching = False
        self.punchingTimer = 0
        self.punchingTimerMax = 12

    def update(self, size):
        self.speedy += self.gravity
        self.move()
        self.worldCollide(size)
        
        if self.punching:
            self.punchingTimer += 1
            if self.punchingTimer >= self.punchingTimerMax:
                self.image = self.baseImage
                self.punching = False
                self.punchingTimer = 0
    
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)

    def worldCollide(self, size):
        width = size[0]
        height = size[1]
        if self.rect.bottom > height:
            self.speedy = 0;
            self.jumping = False
            self.rect.bottom = height
        if self.rect.right > width:
            self.speedx = 0;
            self.rect.right = width
        if self.rect.left < 0:
            self.speedx = 0;
            self.rect.left = 0


    def getDist(self, other):
        x1 = self.rect.centerx
        x2 = other.rect.centerx
        y1 = self.rect.centery
        y2 = other.rect.centery
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
        
    def punch(self):
        self.image = self.punchImages
        self.punching = True
    
