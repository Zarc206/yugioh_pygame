import pygame
import random
pygame.init()

screen = pygame.display.set_mode((1200,800))
clock = pygame.time.Clock()

font = pygame.font.Font(None,50)

messages = []
drawings = []
buttons = []

refineries = [(5,5),(13,8),(22,31), (33,13), (20,16), (35,35), (42,20)]
generators = [(33,20), (31,20),(29,20)]
landingPads = [(33,24),(33,23),(32,24),(32,23),(30,24),(30,23),(29,23),(29,24)]
buildings = [(35,18),(34,18),(33,18),(32,18),(31,18),(30,18),(29,18),(28,18),(27,18),(35,19),(35,20),(35,21),(35,22),(35,23),(35,24),(35,25),(35,26),(34,26),(33,26),(32,26),(31,26),(30,26),(29,26),(28,26),(27,26),(27,19),(27,20),(27,21),(27,22),(27,23),(27,24),(27,25),(27,26)]

selectorCoordinates = [20,20]

class Drawing:
    def __init__(self,x,y,w,h,img):
        self.image = pygame.image.load(img)
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.rect = pygame.Rect(x,y,w,h)
        drawings.append(self)

    def draw(self):
        screen.blit(self.image,(self.x,self.y))

class ClickDrawing(Drawing):
    def __init__(self,x,y,w,h,img,message):
        super().__init__(x,y,w,h,img)
        self.message = message
        buttons.append(self)


    def __init__(self,name,img):
        self.name = name
        self.image = img
    
class Text:
    def __init__(self,text,color,x,y):
        self.text = font.render(text,None,color)
        self.x = x
        self.y = y
        drawings.append(self)
    
    def draw(self):
        screen.blit(self.text,(self.x,self.y))

def createMap():

    for ii in range(43):
        for i in range(53):
            if (i,ii) in buildings:
                sand = Drawing(850 + 28 * ii - 28 * i,-700 + 20 * ii + 20 * i,56,74,"assets/building.webp")
            else:
                sand = Drawing(850 + 28 * ii - 28 * i,-700 + 20 * ii + 20 * i,56,74,"assets/sand.webp")
                if (i,ii) in refineries:
                    refinery = Drawing(850 + 28 * ii - 28 * i + 8,-700 + 20 * ii + 20 * i,49,40,"assets/refinery.webp")
                if (i,ii) in generators:
                    generator = Drawing(850 + 28 * ii - 28 * i + 8,-700 + 20 * ii + 20 * i - 10,49,40,"assets/generator.webp")
                if (i,ii) in landingPads:
                    landingPad = Drawing(850 + 28 * ii - 28 * i,-700 + 20 * ii + 20 * i,56,74,"assets/landingPad.webp")

createMap()

selector = Drawing(850 + 28 * 20 - 28 * 20,-700 + 20 * 20 + 20 * 20,56,74,"assets/selector.webp")

peopleIndicator = Drawing(200,0,200,50,"assets/peopleIndicator.png")
peopleText = Text(str(buildings.__len__()) + "/" + str(buildings.__len__()),"white",300,8)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.message != None:
                        if button.rect.collidepoint(event.pos):
                            messages.append(button.message)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                selectorCoordinates[1] += 1
            if event.key == pygame.K_UP:
                selectorCoordinates[1] -= 1
            if event.key == pygame.K_LEFT:
                selectorCoordinates[0] -= 1
            if event.key == pygame.K_RIGHT:
                selectorCoordinates[0] += 1
            selector.x =  850 + 28 * selectorCoordinates[0] - 28 * selectorCoordinates[1]
            selector.y = -700 + 20 * selectorCoordinates[0] + 20 * selectorCoordinates[1]
    
    for drawing in drawings:
        drawing.draw()






    pygame.display.update()
    clock.tick(60)

pygame.quit()