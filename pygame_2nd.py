import pygame, sys
from pygame.locals import *

pygame.init()

displaysurf = pygame.display.set_mode((400,300),0,32)
pygame.display.set_caption('Drawing')

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


displaysurf.fill(WHITE)
pygame.draw.polygon(displaysurf,GREEN,((146,0),(291,106),(236,277),(56,277),(0,106)))
pygame.draw.line(displaysurf,BLUE,(60,60),(120,60),4)
pygame.draw.line(displaysurf,BLUE,(120,60),(60,120))
pygame.draw.line(displaysurf,BLUE,(60,120),(120,120),4)
pygame.draw.circle(displaysurf,BLUE,(300,50),20,0)
pygame.draw.ellipse(displaysurf,RED,(300,200,40,80),1)
pygame.draw.rect(displaysurf,RED,(200,150,100,50))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()