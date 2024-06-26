import pygame, sys, math

class Fighter():
    def __init__(self, name, speed = [0,0], startPos = [0,0]):
        self.baseImage = pygame.image.load("Images/Player/"+name+"/"+name+".png")
        self.punchImage = pygame.image.load("Images/Player/"+name+"/"+name+"Punching.png")
        self.jumpImage = pygame.image.load("Images/Player/"+name+"/"+name+"Jumping.png")
        self.image = self.baseImage
        self.rect = self.image.get_rect(center = startPos)
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.rad = (self.rect.height/2 + self.rect.width/2)/2
        
        self.health = 100
        
        #self.rect = self.rect.move(startPos)
        
        self.gravity = 1.25
        self.jumping = False

        self.punching = False
        self.punchingTimer = 0
        self.punchingTimerMax = 12
        self.heading = "standing" 

    def update(self, size):
        self.speedy += self.gravity
        self.move()
        self.worldCollide(size)
        
        if self.jumping:
            if self.speedy >0: #falling
                self.image = self.baseImage
            
        
        if self.punching:
            self.punchingTimer += 1
            if self.punchingTimer >= self.punchingTimerMax:
                self.image = self.baseImage
                self.punching = False
                self.punchingTimer = 0
                
    def fighterCollide(self, other):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            if not self.punching and other.punching:
                                self.health -= 15
                            elif self.punching and other.punching:
                                self.health -= 1
                            if self.punching:
                                self.punchingTimer = self.punchingTimerMax
                            return True
        return False    
    
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
        self.image = self.punchImage
        self.punchTimer = 0;
        self.punching = True
    
    def jump(self):
        self.image = self.jumpImage
        self.jumping = True
