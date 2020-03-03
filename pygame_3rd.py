import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30    # 초당 프레임
fpsClock = pygame.time.Clock()

# 윈도우 설정하기
displaysurf = pygame.display.set_mode((400,300),0,32)
pygame.display.set_caption('Animation')

WHITE = (255,255,255)
now_img = pygame.image.load('aa.png')
img_x=10
img_y=10
direction = 'right'

while True:
    displaysurf.fill(WHITE)

    if direction == 'right':
        img_x+=5
        if img_x==280:
            direction='down'
    elif direction == 'down':
        img_y+=5
        if img_y==220:
            direction='left'
    elif direction == 'left':
        img_x -= 5
        if img_x==10:
            direction = 'up'
    elif direction == 'up':
        img_y += 5
        if img_y == 10:
            direction = 'right'

    displaysurf.blit(now_img, (img_x,img_y))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)