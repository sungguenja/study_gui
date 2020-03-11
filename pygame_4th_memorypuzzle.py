# memory puzzle
# by al sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Released under a "simplified BSD' license

import random, pygame, sys
from pygame.locals import *

FPS = 30        # 초당 프레임
windowwidth = 640   # 윈도우의 너비
windowheight = 480  # 윈도우의 높이
revealspeed = 8     # 상자가 보였다가 가려지는 속도
boxsize = 40        # 상자의 너비와 높이
gapsize = 10        # 상자 사이의 간격
boardwidth = 10     # 아이콘 가로줄 수
boardheight = 7     # 아이콘 세로줄 수
assert (boardwidth*boardheight) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'
xmargin = int((windowwidth-(boardwidth*(boxsize+gapsize)))/2)
ymargin = int((windowheight-(boardheight*(boxsize+gapsize)))/2)

#               R    G    B
gray      =   (100, 100, 100)
navyblue  =   ( 60,  60, 100)
white     =   (255, 255, 255)
red       =   (255,   0,   0)
green     =   (  0, 255,   0)
blue      =   (  0,   0, 255)
yellow    =   (255, 255,   0)
orange    =   (255, 128,   0)
purple    =   (255,   0, 255)
cyan      =   (  0, 255, 255)

bgcolor = navyblue
lightbgcolor = gray
boxcolor = white
highlightcolor = blue

donut = 'donut'
square = 'square'
diamond = 'diamond'
lines = 'lines'
oval = 'oval'

allcolors = (red,green,blue,yellow,orange,purple,cyan)
allshapes = (donut,square,diamond,lines,oval)
assert len(allcolors)*len(allshapes)*2 >= boardwidth*boardheight, "board is too big for the number of shapes/colors defined."

def main():
    global fpsclock, displaysurf
    pygame.init()
    fpsclock = pygame.time.Clock()
    displaysurf = pygame.display.set_mode((windowwidth,windowheight))

    mousex = 0          # 마우스 이벤트 발생시 X좌표
    mousey = 0          # 마우스 이벤트 발생시 Y좌표
    pygame.display.set_caption('Memory Game')

    mainBoard = getRandomizedBoard()
    revealedboxes = generateRevealedBoxesData(False)

    firstSelection = None   # 첫번째 상자를 클릭했을 때 (x,y)를 저장

    displaysurf.fill(bgcolor)
    startGameAnimation(mainBoard)

    while True:
        mouseClicked = False

        displaysurf.fill(bgcolor)           # 윈도우를 그린다.
        drawBoard(mainBoard, revealedboxes)

        for event in pygame.event.get():    # 이벤트 처리 루프
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        boxx, boxy = getBoxAtPixel(mousex,mousey)
        if boxx != None and boxy != None:
            # 마우스가 현재 박스 위에 있다.
            if not revealedboxes[boxx][boxy]:
                drawHighlightBox(boxx,boxy)
            if not revealedboxes[boxx][boxy] and mouseClicked:
                revealBoxAnimation(mainBoard, [(boxx,boxy)])
                revealedboxes[boxx][boxy] = True        # 상자를 보이는 것으로 설정
                if firstSelection == None:              # 현재의 상자가 처음 클릭한 상자
                    firstSelection = (boxx,boxy)
                else:   # 현재의 상자가 두 번쨰 클릭한 상자라면
                    # 두 아이콘이 서로 맞는 짝인지 검사한다.
                    icon1shape, icon1color = getShapeAndColor(mainBoard, firstSelection[0], firstSelection[1])
                    icon2shape, icon2color = getShapeAndColor(mainBoard, boxx, boxy)

                    if icon1shape != icon2shape and icon1color != icon1color:
                        # 아이콘이 서로 맞지 않다면, 두 상자 모두 덮는다.
                        pygame.time.wait(1000) # 1000 milliseconds = 1 sec
                        coverBoxesAnimation(mainBoard, [(firstSelection[0],firstSelection[1]),(boxx,boxy)])
                        revealedboxes[firstSelection[0]][firstSelection[1]] = False
                        revealedboxes[boxx][boxy] = False
                    elif hasWon(revealedboxes): # 아이콘이 서로 짝이라면
                        gameWonAnimation(mainBoard)
                        pygame.time.wait(2000)

                        # 게임판을 재설정한다.
                        mainBoard = getRandomizedBoard()
                        revealedboxes = generateRevealedBoxesData(False)

                        # 잠시 동안 게임판의 상자를 열어서 보여준다.
                        drawBoard(mainBoard, revealedboxes)
                        pygame.display.update()
                        pygame.time.wait(1000)

                        #게임 시작 애니메이션을 보여준다.
                        startGameAnimation(mainBoard)
                    firstSelection = None           # firstSelection을 리셋한다

        # 화면을 다시 그린 다음 시간 지연을 기다린다.
        pygame.display.update()
        fpsclock.tick(FPS)


def generateRevealedBoxesData(val):
    revealBoxes = []
    for i in range(boardwidth):
        revealBoxes.append([val]*boardheight)
    return revealBoxes


def getRandomizedBoard():
    # 모든 가능한 색에서 가능한 모양의 목록을 모두 얻어낸다.
    icons = []
    for color in allcolors:
        for shape in allshapes:
            icons.append((shape,color))

    random.shuffle(icons)   # 아이콘 리스트의 순서를 랜덤으로 정한다.
    numIconsUsed = int(boardwidth*boardheight/2)    # 얼마나 많은 아이콘이 필요한지 계산한다.
    icons = icons[:numIconsUsed] * 2    # 각각의 짝을 만든다
    random.shuffle(icons)

    # 랜덤으로 아이콘이 놓여 있는 게임판의 데이터 구조를 만든다.
    board = []
    for x  in range(boardwidth):
        column = []
        for y in range(boardheight):
            column.append(icons[0])
            del icons[0]    # 방금 추가한 아이콘을 지운다 (그럼 pop쓰지)
        board.append(column)
    return board


def splitIntoGroupsOf(groupsize, thelist):
    # 리스트를 2차원 리스트로 만든다. 안쪽의 리스트는 최대로.
    # groupsize개 만큼의 아이템이 있다.
    result = []
    for i in range(0,len(thelist), groupsize):
        result.append(thelist[i:i+groupsize])
    return result


def leftTopCoordsOfBox(boxx, boxy):
    # 게임판 좌표계를 픽셀 좌표계로 변환한다.
    left = boxx * (boxsize+gapsize) + xmargin
    top = boxy * (boxsize+gapsize) + ymargin
    return (left,top)


def getBoxAtPixel(x,y):
    for boxx in range(boardwidth):
        for boxy in range(boardheight):
            left, top = leftTopCoordsOfBox(boxx,boxy)
            boxRect = pygame.Rect(left, top, boxsize, boxsize)
            if boxRect.collidepoint(x,y):
                return (boxx,boxy)
    return (None,None)


def drawIcon(shape,color,boxx,boxy):
    quarter = int(boxsize*0.25)     # syntactic sugar
    half    = int(boxsize*0.5)      # syntactic sugar

    left, top = leftTopCoordsOfBox(boxx,boxy)  # 보드의 좌표에서 픽셀의 좌표를 얻는다.
    # 형태를 그린다.
    if shape == donut:
        pygame.draw.circle(displaysurf, color, (left+half, top+half), half-5)
        pygame.draw.circle(displaysurf, bgcolor, (left + half, top + half), quarter - 5)
    elif shape == square: