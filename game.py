import pygame
import random
import math
pygame.init()

screen = pygame.display.set_mode((1200,800))
clock = pygame.time.Clock()

font = pygame.font.Font(None,50)

messages = []
drawings = []
buttons = []
conditions = []

refineryCords = [(5,5),(13,8),(22,31), (33,13), (21,17), (35,35), (42,20)]
refineries = []
generatorCords = [(33,20), (31,20),(29,20)]
generators = []
landingPadCords = [(33,24),(33,23),(32,24),(32,23),(30,24),(30,23),(29,23),(29,24)]
landingPads = []
housingCords = [(35,18),(34,18),(33,18),(32,18),(31,18),(30,18),(29,18),(28,18),(27,18),(35,19),(35,20),(35,21),(35,22),(35,23),(35,24),(35,25),(35,26),(34,26),(33,26),(32,26),(31,26),(30,26),(29,26),(28,26),(27,26),(27,19),(27,20),(27,21),(27,22),(27,23),(27,24),(27,25),(27,26)]
houses = []
UIs = []

selectorCoordinates = [20,20]

totalPeople = housingCords.__len__() * 2
availablePeople = housingCords.__len__() * 2
availablePower = 0
usedPower = 0


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

class ConditionalDrawing(Drawing):
    def __init__(self,x,y,w,h,img,condition):
        super().__init__(x,y,w,h,img)
        self.condition = condition

    def draw(self):

        if self.condition in conditions:
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
        self.color = color
        self.x = x
        self.y = y
        drawings.append(self)
    
    def draw(self):
        screen.blit(self.text,(self.x,self.y))

    def change(self,text):
        self.text = font.render(text,None,self.color)

class BuildingUI(ConditionalDrawing):
    def __init__(self,condition,buildingCords,buildings):
        super().__init__(10,100,400,600,"assets/menu.png",condition)
        self.buildingCords = buildingCords
        self.buildings = buildings
        self.personIndecator = pygame.image.load("assets/peopleIndicator.png")
        UIs.append(self)

    def draw(self):
        
        buildingNumber = 0

        for i in range(self.buildingCords.__len__()):
            if self.buildingCords[i] == (selectorCoordinates[1],selectorCoordinates[0]):
                buildingNumber = i

        if self.condition in conditions:
            text = font.render(str(self.buildings[buildingNumber].allocated) + "/" + str(self.buildings[buildingNumber].capacity),None,"white")
            screen.blit(self.image,(self.x,self.y))
            screen.blit(self.personIndecator,(100,150))
            screen.blit(text,(200,160))

    def p(self):
        None
    def o(self):
        None
    def l(self):
        None
    def t(self):
        None

class HouseUI(BuildingUI):
    def __init__(self,condition,buildingCords,buildings):
        super().__init__(condition,buildingCords,buildings)
    
    def draw(self):
        
        buildingNumber = 0

        for i in range(self.buildingCords.__len__()):
            if self.buildingCords[i] == (selectorCoordinates[1],selectorCoordinates[0]):
                buildingNumber = i

        if self.condition in conditions:
            text = font.render(str(self.buildings[buildingNumber].allocated) + "/" + str(self.buildings[buildingNumber].capacity),None,"white")
            screen.blit(self.image,(self.x,self.y))
            screen.blit(self.personIndecator,(100,150))
            screen.blit(text,(200,160))

class LandingPadUI(BuildingUI):
    def __init__(self,condition,buildingCords,buildings):
        super().__init__(condition,buildingCords,buildings)
    
    def draw(self):
        
        buildingNumber = 0

        for i in range(self.buildingCords.__len__()):
            if self.buildingCords[i] == (selectorCoordinates[1],selectorCoordinates[0]):
                buildingNumber = i

        if self.condition in conditions:
            text = font.render(str(self.buildings[buildingNumber].allocated) + "/" + str(self.buildings[buildingNumber].capacity),None,"white")
            screen.blit(self.image,(self.x,self.y))
            screen.blit(self.personIndecator,(100,150))
            screen.blit(text,(200,160))   

            buildingNumber = -1
            for i in range(self.buildingCords.__len__()):
                if self.buildingCords[i] == (selectorCoordinates[1],selectorCoordinates[0]):
                    buildingNumber = i
            if buildingNumber > -1:
                building = self.buildings[buildingNumber]
                spiceBar = pygame.image.load("assets/spiceBar.png")
                screen.blit(spiceBar,(60,620),(0,0,300 * building.spiceStorage/building.spiceCapacity,30))  
            
            transportIcon = pygame.image.load("assets/addIcon.png")
            tText = font.render("T",None,"white")
            screen.blit(transportIcon,(180,650))
            screen.blit(tText,(190,660))  

    def t(self):
        buildingNumber = -1
        for i in range(self.buildingCords.__len__()):
            if self.buildingCords[i] == (selectorCoordinates[1],selectorCoordinates[0]):
                buildingNumber = i
        if buildingNumber > -1 and not jet.transporting and self.buildings[buildingNumber].spiceStorage > 0:
            jet.transporting = True
            jet.target = self.buildings[buildingNumber]

class GeneratorUI(BuildingUI):
    def __init__(self,condition,buildingCords,buildings):
        super().__init__(condition,buildingCords,buildings)
    
    def draw(self):
        
        buildingNumber = 0
        for i in range(self.buildingCords.__len__()):
            if self.buildingCords[i] == (selectorCoordinates[1],selectorCoordinates[0]):
                buildingNumber = i

        if self.condition in conditions:
            text = font.render(str(self.buildings[buildingNumber].allocated) + "/" + str(self.buildings[buildingNumber].capacity),None,"white")
            icon1 = pygame.image.load("assets/removeIcon.png")
            icon1text = font.render("O",False,"white")
            icon2 = pygame.image.load("assets/addIcon.png")
            icon2text = font.render("P",False,"white")
            screen.blit(self.image,(self.x,self.y))
            screen.blit(self.personIndecator,(50,150))
            screen.blit(text,(150,160))
            screen.blit(icon1,(270,150))
            screen.blit(icon1text,(280,160))
            screen.blit(icon2,(340,150))
            screen.blit(icon2text,(350,160))

    def p(self):
        buildingNumber = -1
        for i in range(self.buildingCords.__len__()):
            if self.buildingCords[i] == (selectorCoordinates[1],selectorCoordinates[0]):
                buildingNumber = i
        if buildingNumber > -1:
            if self.buildings[buildingNumber].allocated < self.buildings[buildingNumber].capacity:
                self.buildings[buildingNumber].allocated += 1
                for house in houses:
                    if house.allocated > 0:
                        house.allocated -= 1
                        break

    def o(self):
        buildingNumber = 0
        for i in range(self.buildingCords.__len__()):
            if self.buildingCords[i] == (selectorCoordinates[1],selectorCoordinates[0]):
                buildingNumber = i
        
        if self.buildings[buildingNumber].allocated > 0:
            self.buildings[buildingNumber].allocated -= 1
            for house in houses:
                if house.allocated < house.capacity:
                    house.allocated += 1
                    break

class RefineryUI(BuildingUI):
    def __init__(self,condition,buildingCords,buildings):
        super().__init__(condition,buildingCords,buildings)
    
    def draw(self):
        
        buildingNumber = 0

        for i in range(self.buildingCords.__len__()):
            if self.buildingCords[i] == (selectorCoordinates[1],selectorCoordinates[0]):
                buildingNumber = i

        if self.condition in conditions:
            electricCounter = pygame.image.load("assets/electricIndicator.png")
            electricText = font.render(str(5 * self.buildings[buildingNumber].powered) + "/5",None,"white")
            text = font.render(str(self.buildings[buildingNumber].allocated) + "/" + str(self.buildings[buildingNumber].capacity),None,"white")
            icon1 = pygame.image.load("assets/removeIcon.png")
            icon1text = font.render("O",False,"white")
            icon2 = pygame.image.load("assets/addIcon.png")
            icon2text = font.render("P",False,"white")
            screen.blit(self.image,(self.x,self.y))
            screen.blit(electricCounter,(50,250))
            screen.blit(self.personIndecator,(50,150))
            screen.blit(text,(150,160))
            screen.blit(electricText,(150,260))
            screen.blit(icon1,(270,150))
            screen.blit(icon1text,(280,160))
            screen.blit(icon2,(340,150))
            screen.blit(icon2text,(350,160))
            
            
            if self.buildings[buildingNumber].powered:
                powerIcon = pygame.image.load("assets/removeIcon.png")
            else:
                powerIcon = pygame.image.load("assets/addIcon.png")
            powerText = font.render("L",False,"white")
            screen.blit(powerIcon,(310, 250))
            screen.blit(powerText,(320,260))

            building = self.buildings[buildingNumber]

            spiceBar = pygame.image.load("assets/spiceBar.png")
            screen.blit(spiceBar,(60,620),(0,0,300 * building.spiceStorage/building.spiceCapacity,30))
            transportIcon = pygame.image.load("assets/addIcon.png")
            tText = font.render("T",None,"white")
            screen.blit(transportIcon,(180,650))
            screen.blit(tText,(190,660))

    
    def p(self):
        buildingNumber = -1
        for i in range(self.buildingCords.__len__()):
            if self.buildingCords[i] == (selectorCoordinates[1],selectorCoordinates[0]):
                buildingNumber = i
        if buildingNumber > -1:
            if self.buildings[buildingNumber].allocated < self.buildings[buildingNumber].capacity:
                self.buildings[buildingNumber].allocated += 1
                for house in houses:
                    if house.allocated > 0:
                        house.allocated -= 1
                        break

    def o(self):
        buildingNumber = -1
        for i in range(self.buildingCords.__len__()):
            if self.buildingCords[i] == (selectorCoordinates[1],selectorCoordinates[0]):
                buildingNumber = i
        
        if self.buildings[buildingNumber].allocated > 0:
            self.buildings[buildingNumber].allocated -= 1
            for house in houses:
                if house.allocated < house.capacity:
                    house.allocated += 1
                    break
    def l(self):
        buildingNumber = -1
        for i in range(self.buildingCords.__len__()):
            if self.buildingCords[i] == (selectorCoordinates[1],selectorCoordinates[0]):
                buildingNumber = i
        
        if self.buildings[buildingNumber].powered:
            self.buildings[buildingNumber].powered = False
        else:
            if usedPower <= availablePower - 5:
                self.buildings[buildingNumber].powered = True

    def t(self):
        
        buildingNumber = -1

        for i in range(self.buildingCords.__len__()):
            if self.buildingCords[i] == (selectorCoordinates[1],selectorCoordinates[0]):
                buildingNumber = i

        if buildingNumber > -1:
            building = self.buildings[buildingNumber]
            
            if not building.transport.transporting and building.spiceStorage > 0:
                building.transport.cords[0] = building.cords[0]
                building.transport.cords[1] = building.cords[1]
                building.transport.storage = building.spiceStorage
                building.spiceStorage = 0
                building.transport.transporting = True
                building.transport.target = landingPads[math.floor(random.random() * landingPads.__len__())] 
                count = 0
                while building.transport.target.spiceCapacity - building.transport.target.spiceStorage < building.transport.storage:
                    building.transport.target = landingPads[math.floor(random.random() * landingPads.__len__())] 
                    count += 1
                    if count > 16:
                        building.transport.storage = building.transport.target.spiceCapacity - building.transport.target.spiceStorage 
                    
class InteractTile:
    def __init__(self,cords,capacity,allocated):
        self.cords = [850 + 28 * cords[1] - 28 * cords[0],-700 + 20 * cords[1] + 20 * cords[0]]
        self.capacity = capacity
        self.allocated = allocated
        self.powered = False

class Transport():
    def __init__(self):
        self.transporting = False
        self.target = None
        self.speed = 1
        self.image = pygame.image.load("assets/transport.webp")
        drawings.append(self)
        self.cords = [0,0]
        self.storage = 0

    def draw(self):
        if self.transporting:
            if self.target.cords[0] - self.cords[0] == 0:
                slope = 1
            else:
                slope = (self.target.cords[1] - self.cords[1])/(self.target.cords[0] - self.cords[0])
            moveMult = 1

            if self.target.cords[0] - self.cords[0] < 0:
                moveMult = -1
            self.cords[1] += self.speed * slope * moveMult
            self.cords[0] += self.speed  * moveMult

            if abs(self.target.cords[0] - self.cords[0]) < 5 and abs(self.target.cords[1] - self.cords[1]) < 5:
                self.target.spiceStorage += self.storage
                self.storage = 0
                self.transporting = False

            screen.blit(self.image,(self.cords[0],self.cords[1]))

class Jet():
    def __init__(self):
        self.transporting = False
        self.target = None
        self.speed = 5
        self.image = pygame.image.load("assets/jet.webp")
        drawings.append(self)
        self.cords = [0,0]
        self.storage = 0
    
    def draw(self):
        if self.transporting:
            
            if self.target.cords[0] - self.cords[0] == 0:
                slope = 1
            else:
                slope = (self.target.cords[1] - self.cords[1])/(self.target.cords[0] - self.cords[0])
            moveMult = 1

            if self.target.cords[0] - self.cords[0] < 0:
                moveMult = -1
            self.cords[1] += self.speed * slope * moveMult
            self.cords[0] += self.speed  * moveMult

            if abs(self.target.cords[0] - self.cords[0]) < 5 and abs(self.target.cords[1] - self.cords[1]) < 5:
                if self.cords[1] < 0:
                    global money
                    money += math.floor(self.storage)
                    self.storage = 0
                    self.transporting = False
                    self.cords = [-50,-50]
                else:
                    self.storage = self.target.spiceStorage
                    self.target.spiceStorage = 0
                    self.target = dropoff

            screen.blit(self.image,(self.cords[0],self.cords[1]))

class Target():
    def __init__(self,x,y):
        self.cords = (x,y)

class Refinery(InteractTile):
    def __init__(self,cords,capacity,allocated):
        super().__init__(cords,capacity,allocated)
        self.spiceCapacity = 100
        self.spiceStorage = 0
        self.spiceRate = 0.01
        self.transport = None

    def activate(self):
        self.transport = Transport()

class LandingPad(InteractTile):
    def __init__(self,cords,capacity,allocated):
        super().__init__(cords,capacity,allocated)
        self.spiceCapacity = 300
        self.spiceStorage = 0

def createMap():

    for cords in housingCords:
        house = InteractTile(cords,1,1)
        houses.append(house)
    
    for cords in generatorCords:
        generator = InteractTile(cords,5,0)
        generators.append(generator)

    for cords in refineryCords:
        refinery = Refinery(cords,6,0)
        refineries.append(refinery)  

    for cords in landingPadCords:
        landingPad = LandingPad(cords,10,0)
        landingPads.append(landingPad)      

    for ii in range(43):
        for i in range(53):
            if (i,ii) in housingCords:
                sand = Drawing(850 + 28 * ii - 28 * i,-700 + 20 * ii + 20 * i,56,74,"assets/building.webp")
            else:
                sand = Drawing(850 + 28 * ii - 28 * i,-700 + 20 * ii + 20 * i,56,74,"assets/sand.webp")
                if (i,ii) in refineryCords:
                    refinery = Drawing(850 + 28 * ii - 28 * i + 8,-700 + 20 * ii + 20 * i,49,40,"assets/refinery.webp")
                if (i,ii) in generatorCords:
                    generator = Drawing(850 + 28 * ii - 28 * i + 8,-700 + 20 * ii + 20 * i - 10,49,40,"assets/generator.webp")
                if (i,ii) in landingPadCords:
                    landingPad = Drawing(850 + 28 * ii - 28 * i,-700 + 20 * ii + 20 * i,56,74,"assets/landingPad.webp")

    for refinery in refineries:
        refinery.activate()
createMap()

selector = Drawing(850 + 28 * 20 - 28 * 20,-700 + 20 * 20 + 20 * 20,56,74,"assets/selector.webp")

peopleIndicator = Drawing(150,0,200,50,"assets/peopleIndicator.png")
electricIndicator = Drawing(400,0,200,50,"assets/electricIndicator.png")
moneyIndicator = Drawing(650,0,200,50,"assets/emptyIndicator.png")

peopleText = Text(str(availablePeople) + "/" + str(totalPeople),"white",250,8)
electricText = Text(str(usedPower) + "/" + str(availablePower),"white",500,8)
moneyText = Text("$ " + str(0),"white",720,8)

houseMenu = HouseUI("onBuilding",housingCords,houses) 
generatorMenu = GeneratorUI("onGenerator",generatorCords,generators)
refineryMenu = RefineryUI("onRefinery",refineryCords,refineries)
landingPadMenu = LandingPadUI("onLandingPad",landingPadCords,landingPads)

jet = Jet()
dropoff = Target(1250,-50)

money = 0


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
            if event.key == pygame.K_p:
                for ui in UIs:
                    ui.p()
            if event.key == pygame.K_o:
                for ui in UIs:
                    ui.o()
            if event.key == pygame.K_l:
                for ui in UIs:
                    ui.l()
            if event.key == pygame.K_t:
                for ui in UIs:
                    ui.t()
            selector.x =  850 + 28 * selectorCoordinates[0] - 28 * selectorCoordinates[1]
            selector.y = -700 + 20 * selectorCoordinates[0] + 20 * selectorCoordinates[1]
    
    availablePeople = 0
    totalPeople = 0
    for house in houses:
        availablePeople += house.allocated
    for house in houses:
        totalPeople += house.capacity
    
    availablePower = 0

    for generator in generators:
        availablePower += generator.allocated

    usedPower = 0

    for refinery in refineries:
        if refinery.powered:
            refinery.spiceStorage += refinery.spiceRate * refinery.allocated
            if refinery.spiceStorage > refinery.spiceCapacity:
                refinery.spiceStorage = refinery.spiceCapacity
            usedPower += 5

    peopleText.change(str(availablePeople) + "/" + str(totalPeople))
    electricText.change(str(usedPower) + "/" + str(availablePower))
    moneyText.change("$ " + str(money))

    conditions = []
    if (selectorCoordinates[1],selectorCoordinates[0]) in housingCords:
        conditions.append("onBuilding")
    if (selectorCoordinates[1],selectorCoordinates[0]) in generatorCords:
        conditions.append("onGenerator")
    if (selectorCoordinates[1],selectorCoordinates[0]) in refineryCords:
        conditions.append("onRefinery")
    if (selectorCoordinates[1],selectorCoordinates[0]) in landingPadCords:
        conditions.append("onLandingPad")

    for drawing in drawings:
        drawing.draw()

    pygame.display.update()
    clock.tick(60)

pygame.quit()