import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((1450, 850))

name = pygame.display.set_caption("Milk Maker")

score = 0

icon = pygame.image.load("icow.png")
pygame.display.set_icon(icon)
white = (255,255,255)
red = (255,0,0)

dollarsign = pygame.image.load("dollarsign.png")
milkIMG = pygame.image.load("milk.png")
milkIMG = pygame.transform.scale(milkIMG, (40, 50))

dollarsign = pygame.transform.scale(dollarsign, (60,70))

def dollar():
    screen.blit(dollarsign, (5, 5))

cowIMG = pygame.image.load("cow.png")
cowX = 500
cowY = 370

fenceIMG = pygame.image.load("fence.png")
score = 1
dolla = 0
convert = 1
convertprice = 100
def cow():
    screen.blit(cowIMG, (cowX, cowY))


fenceIMG = pygame.transform.scale(fenceIMG, (700, 200))



def fence():
    screen.blit(fenceIMG, (425, 650))

def milk(): 
    screen.blit(milkIMG, (732, 195))

running = True
while running:

    screen.fill((white))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                score = score + 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                if dolla >= convertprice:
                    dolla = dolla - convertprice
                    convert = convert * 2
                    convertprice = convertprice * 3 
                    dolla = math.trunc(dolla)
                elif dolla < convertprice:
                    for x in [1,2,3]:
                        pass      
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                dolla = dolla + score*convert
                score = 0
            
                
                
                
    cool = str(score)
    nice = str(dolla)
    font = pygame.font.Font("freesansbold.ttf", 64)
    scoreText = font.render(cool, True, (0, 0, 0))
    moneyText = font.render(nice, True, (0, 0, 0))
    screen.blit(moneyText, (60, 10))

    if score < 10:
        screen.blit(scoreText, (735, 125))
    if  100 > score >= 10:
        screen.blit(scoreText, (715, 125))
    if score >= 100:
        screen.blit(scoreText, (695, 125))   
    cow()
    fence()     
    milk()
    dollar()
    

    
    
    
         

    pygame.display.update()   
