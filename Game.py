import pygame
import time
import AI
import random


score = 0

def gameOver():
    AI.GameOver()

FPS = 30

gameState = []

screenx = 500
screeny = 200

yOffset = 10
xOffset = 1

pipeOffset = 20

pipeColor = (255, 255, 255)
birdColor = (255, 56, 34)

birdSize = 5

gravity = -10
velocity = 0
pygame.init()

screen = pygame.display.set_mode((screenx, screeny))

birdSpeed = 2

birdy = random.randrange(yOffset, screeny-yOffset)  #this will be the starting position of the bird
birdy = yOffset
birdx = 10  #the x position of the bird

pipeList = []

newPipeCountDown = 0

control = False
humanPlaying = True
while True:
    score += 1
    myfont = pygame.font.SysFont("arial", 12)
    lable = myfont.render(str(score), 2, (0, 255, 255))
    screen.blit(lable, (screenx-100, 10))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            AI.display()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and humanPlaying:
                control = True
            if event.key == pygame.K_h:
                humanPlaying = True
            if event.key == pygame.K_m:
                humanPlaying = False

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, birdColor, (birdx, birdy, birdSize, birdSize))
    time.sleep(1/FPS)

    if newPipeCountDown == 0:
        newPipeCountDown = 100
        newPipeLocation = [screenx, random.randrange(yOffset, screeny-yOffset)]
        pipeList.append(newPipeLocation)
    else:
        newPipeCountDown -= 1

    if(pipeList[0][0] < birdx - xOffset):
        pipeList.remove(pipeList[0])


    for p in pipeList:  #draw the pipes on the screen
        pygame.draw.rect(screen, pipeColor, (p[0], p[1] - pipeOffset - 200, 3, 200))
        pygame.draw.rect(screen, pipeColor, (p[0], p[1] + pipeOffset , 3, 200))

    for i in range(len(pipeList)):
        pipeList[i][0] -= birdSpeed

    pygame.display.update()

    gameState = [pipeList[0][0],birdy -  pipeList[0][1]]

    c = AI.GetControl(gameState, control, humanPlaying)
    if humanPlaying == False:
        control = c

    velocity += gravity * 0.5
    if control == True:
        control = False
        velocity = 70

    birdy -= 0.1 * velocity

    if birdy < yOffset or birdy > screeny - yOffset:
        gameOver()
        break

