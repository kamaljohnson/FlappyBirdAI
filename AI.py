import pygame
import random
import pickle
file = open("dataset.pkl", "wb")
scoreFile = open("score.pkl", "rb")
Topscore = pickle.load(scoreFile)
control = True
pointList = []
TrueColor = (0, 0, 255)
FalseColor = (255, 0, 0)
setOfPoints = []
listx = []
listy = []

for i in range(10):
    k = []
    for i in range(10):
        k.append(0)
    setOfPoints.append(k)

def GetControl(gameState, control, isHuman):
    if isHuman:
        pointList.append([control, int(gameState[0] + 300), int(gameState[1] + 400)])
        x = int(gameState[0])//20
        y = int(gameState[1] + 100)//20
        if(x < 10 and y < 10 and control == True):
            setOfPoints[x][y] += 10
        if (x < 10 and y < 10 and control == False):
            setOfPoints[x][y] -= 1
    x = int(gameState[0])//20
    y = int(gameState[1] + 100)//20
    if(x < 10 and y < 10):
        if setOfPoints[x][y] > 0:
            control = True
        elif setOfPoints[x][y] < 0:
            control = False
        else:
            i = random.randrange(2)
            if i == 0:
                control = False
            else:
                control = True
    return control
def display():
    pygame.init()
    screenx = 1000
    screeny = 1000
    screen = pygame.display.set_mode((screenx, screeny))
    notDrawn = True
    pygame.draw.rect(screen, (255, 255, 255), (300, 300, 200, 200), 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                for i in setOfPoints:
                    for k in i:
                        print(k, end=" ")
                    print()
                pickle.dump(setOfPoints, file)
                exit(0)
        if(notDrawn):
            notDrawn = False
            for i in pointList:
                listx.append(i[1])
                listy.append(i[2])
                if i[0] == True:
                    pygame.draw.circle(screen, TrueColor, (i[1], i[2]), 2)
                else:
                    pygame.draw.circle(screen, FalseColor, (i[1], i[2]), 2)
                pygame.display.update()
def GameOver():
    pass

