import pygame
pygame.init()

screen = pygame.display.set_mode((1200,800))
clock = pygame.time.Clock()

font = pygame.font.Font(None,50)

messages = []
drawings = []
buttons = []
conditions = []

refineryCords = [(5,5),(13,8),(22,31), (33,13), (20,16), (35,35), (42,20)]
refineries = []
generatorCords = [(33,20), (31,20),(29,20)]
generators = []
landingPads = [(33,24),(33,23),(32,24),(32,23),(30,24),(30,23),(29,23),(29,24)]
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

class InteractTile:
    def __init__(self,cords,capacity,allocated):
        self.cords = cords
        self.capacity = capacity
        self.allocated = allocated
        self.powered = False

def createMap():

    for cords in housingCords:
        house = InteractTile(cords,2,2)
        houses.append(house)
    
    for cords in generatorCords:
        generator = InteractTile(cords,5,0)
        generators.append(generator)

    for refinery in refineryCords:
        refinery = InteractTile(cords,6,0)
        refineries.append(refinery)    

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
                if (i,ii) in landingPads:
                    landingPad = Drawing(850 + 28 * ii - 28 * i,-700 + 20 * ii + 20 * i,56,74,"assets/landingPad.webp")

createMap()

selector = Drawing(850 + 28 * 20 - 28 * 20,-700 + 20 * 20 + 20 * 20,56,74,"assets/selector.webp")

peopleIndicator = Drawing(150,0,200,50,"assets/peopleIndicator.png")
electricIndicator = Drawing(400,0,200,50,"assets/electricIndicator.png")

peopleText = Text(str(availablePeople) + "/" + str(totalPeople),"white",250,8)
electricText = Text(str(usedPower) + "/" + str(availablePower),"white",500,8)

houseMenu = HouseUI("onBuilding",housingCords,houses) 
generatorMenu = GeneratorUI("onGenerator",generatorCords,generators)
refineryMenu = RefineryUI("onRefinery",refineryCords,refineries)


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

    peopleText.change(str(availablePeople) + "/" + str(totalPeople))
    electricText.change(str(usedPower) + "/" + str(availablePower))

    conditions = []
    if (selectorCoordinates[1],selectorCoordinates[0]) in housingCords:
        conditions.append("onBuilding")
    if (selectorCoordinates[1],selectorCoordinates[0]) in generatorCords:
        conditions.append("onGenerator")
    if (selectorCoordinates[1],selectorCoordinates[0]) in refineryCords:
        conditions.append("onRefinery")

    for drawing in drawings:
        drawing.draw()

    pygame.display.update()
    clock.tick(60)

pygame.quit()