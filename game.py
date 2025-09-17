import pygame
import math

pygame.init()

screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

surfaces = []
buttons = []
messages = []

keyA = False
keyD = False
keyW = False
keyS = False

class SurfaceImage:
    def __init__(self,image,x,y):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()   
        self.rect.left = x
        self.rect.y = y
        surfaces.append(self)

    def draw(self):
        screen.blit(self.image,self.rect)
    
    def upkeep(self):
        None

class SurfaceButton(SurfaceImage):
    def __init__(self,image,x,y,message):
        super().__init__(image,x,y)
        self.message = message
        buttons.append(self)
    
    def press(self):
        messages.append(self.message)    

class Character(SurfaceImage):
    def __init__(self,image,x,y):
        super().__init__(image,x,y)
        self.image = pygame.transform.scale2x(self.image)
        self.frameNum = 0
        self.animationNum = 0
        self.rect.width = (42) 
        self.rect.height = 67


    def draw(self):
        self.rect.width = 42
        if self.animationNum == 0 or self.animationNum == 3:
            self.rect.width = 49
        screen.blit(self.image,self.rect,(math.floor(self.frameNum) * self.rect.width,self.animationNum * self.rect.height,self.rect.width,self.rect.height))

    def upkeep(self):
        self.frameNum = 0


class Player(Character):
    def __init__(self,image,x,y):
        super().__init__(image,x,y)
        self.speed = 2

    def draw(self):
        self.rect.width = 42
        if self.animationNum == 0 or self.animationNum == 3:
            self.rect.width = 48
        screen.blit(self.image,self.rect,(math.floor(self.frameNum) * self.rect.width,self.animationNum * self.rect.height,self.rect.width,self.rect.height))

    def upkeep(self):

        if keyA:
            self.animationNum = 2
            self.rect.left -= self.speed
        elif keyW:
            self.animationNum = 0
            self.rect.top -= self.speed
        elif keyS:
            self.animationNum = 3
            self.rect.top += self.speed
        elif keyD:
            self.animationNum = 1
            self.rect.left += self.speed


        if keyA or keyW or keyS or keyD:
            self.frameNum += 0.1
        else:
            self.frameNum = 0

        if self.frameNum >= 3:
            self.frameNum = 0
        

bg = SurfaceImage("assets/background.png",0,0)
startButton = SurfaceButton("assets/startButton.png",100,100,"start")

while True:

    if "start" in messages:
        messages.remove("start")
        grid = SurfaceImage("assets/grid.png",50,50)
        yugi = Player('assets/characters/yugi.png',100,100)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for button in buttons:
                if button.rect.collidepoint(pos):
                    surfaces.remove(button)
                    buttons.remove(button)
                    button.press()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                keyA = True
            if event.key == pygame.K_d:
                keyD = True
            if event.key == pygame.K_w:
                keyW = True
            if event.key == pygame.K_s:
                keyS = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                keyA = False
            if event.key == pygame.K_d:
                keyD = False
            if event.key == pygame.K_w:
                keyW = False
            if event.key == pygame.K_s:
                keyS = False

    for surface in surfaces:
        surface.upkeep()
        surface.draw()
   
    pygame.display.update()
    clock.tick(60)