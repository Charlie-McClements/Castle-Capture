import pygame, sys, random
from pygame.locals import *
from time import sleep

pygame.init()

# Game Title
name = "Castle Capture"

#Frames Per Second (Game Speed)
FPS = 30
fpsClock = pygame.time.Clock()

#Window(s)
DISPLAYSURF = pygame.display.set_mode((1000, 500))
pygame.display.set_caption(str(name))

# Colours
Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Yellow = (255, 255, 0)
TBG = (178, 224, 240)
TTC = (76, 88, 92)

# Game Variables
rx = 0
ry = 0
gx = 0
gy = 450
bx = 950
by = 0
yx = 950
yy = 450
turn = 'YELLOW'
roll = 0
rol = 0
rsx = -50
rsy = -50
rsx1 = -50
rsy1 = -50
rsx2 = -50
rsy2 = -50
gsx = -50
gsy = -50
gsx1 = -50
gsy1 = -50
gsx2 = -50
gsy2 = -50
bsx = -50
bsy = -50
bsx1 = -50
bsy1 = -50
bsx2 = -50
bsy2 = -50
ysx = -50
ysy = -50
ysx1 = -50
ysy1 = -50
ysx2 = -50
ysy2 = -50
bbx = 100
bby = -50
grx = 100
gry = 250
grx1 = 200
gry1 = 250
grx2 = 500
gry2 = 100
grx3 = 600
gry3 = 100
grx4 = 750
gry4 = 350
grx5 = 850
gry5 = 350
gpx = 150
gpy = 200
gpx1 = 150
gpy1 = 300
gpx2 = 550
gpy2 = 50
gpx3 = 550
gpy3 = 150
gpx4 = 800
gpy4 = 300
gpx5 = 800
gpy5 = 400
hold = "RED"
start = 0

# All images
grid = pygame.image.load("grid.png")
castle = pygame.image.load("castle.jpg")
ground_river = pygame.image.load("ground_river.jpg")
ground_road = pygame.image.load("ground_road.jpg")
red = pygame.image.load("red.png")
green = pygame.image.load("green.png")
blue = pygame.image.load("blue.png")
yellow = pygame.image.load("yellow.png")
bomb = pygame.image.load("bomb.jpg")
background = pygame.image.load("background.jpg")

# All Text
fontObj = pygame.font.Font('freesansbold.ttf', 50)
fontObj2 = pygame.font.Font('freesansbold.ttf', 22)
fontObj1 = pygame.font.Font('freesansbold.ttf', 40)
textSurfaceObj = fontObj.render(str(turn) + ' rolled a ' + str(rol), True, Green, Blue)
textSurfaceObj3 = fontObj.render(str(turn) + ' rolled a ' + str(rol), True, Green, Blue)
textSurfaceObj2 = fontObj.render(str(turn) + ' rolled a ' + str(rol), True, Green, Blue)
textRectObj2 = textSurfaceObj2.get_rect()
textRectObj2.center = (545, 450)
textRectObj = textSurfaceObj.get_rect()
textRectObj3 = textSurfaceObj.get_rect()
textRectObj3.center = (570, 50)
textRectObj.center = (500, 250)
textRectObj1 = textSurfaceObj.get_rect()
textRectObj1.center = (500, 100)


def start():
    start = 0
    while start == 0:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                if event.key == K_RETURN:
                    start = 1
        DISPLAYSURF.blit(background, (0, 0))
        DISPLAYSURF.blit(fontObj2.render('Press enter to start a new game.', True, TTC, TBG), textRectObj2)
        DISPLAYSURF.blit(fontObj1.render(str(name), True, TTC, TBG), textRectObj3)
        pygame.display.update
        if start == 1:
            break
        fpsClock.tick(FPS)


def next_turn():
    global turn
    global roll
    global rol
    if turn == 'RED':
        turn = 'BLUE'
        rol = random.randint(1,6)
        roll = rol * 50
        return turn
    if turn == 'BLUE':
        turn = 'GREEN'
        rol = random.randint(1,6)
        roll = rol * 50
        return turn
    if turn == 'GREEN':
        turn = 'YELLOW'
        rol = random.randint(1,6)
        roll = rol * 50
        return turn
    if turn == 'YELLOW':
        turn = 'RED'
        rol = random.randint(1,6)
        roll = rol * 50
        return turn


def capture():
    # Capturing towers
    global rsx, rsy, rsx1, rsy1, rsx2, rsy2, gsx, gsy, gsx1, gsy1, gsx2, gsy2, bsx, bsy, bsx1, bsy1, bsx2, bsy2, ysx, ysy, ysx1, ysy1, ysx2, ysy2
    if rx == 150 and ry == 250:
        rsx = 162
        rsy = 262
        bsx = -50
        bsy = -50
        gsx = -50
        gsy = -50
        ysx = -50
        ysy = -50
        return rsx and rsy
    if rx == 550 and ry == 100:
        rsx1 = 562
        rsy1 = 112
        bsx1 = -50
        bsy1 = -50
        gsx1 = -50
        gsy1 = -50
        ysx1 = -50
        ysy1 = -50
        return rsx1 and rsy1
    if rx == 800 and ry == 350:
        rsx2 = 812
        rsy2 = 362
        bsx2 = -50
        bsy2 = -50
        gsx2 = -50
        gsy2 = -50
        ysx2 = -50
        ysy2 = -50
        return rsx2 and rsy2
    if gx == 150 and gy == 250:
        gsx = 162
        gsy = 262
        bsx = -50
        bsy = -50
        rsx = -50
        rsy = -50
        ysx = -50
        ysy = -50
        return gsx and gsy
    if gx == 550 and gy == 100:
        gsx1 = 562
        gsy1 = 112
        bsx1 = -50
        bsy1 = -50
        rsx1 = -50
        rsy1 = -50
        ysx1 = -50
        ysy1 = -50
        return gsx1 and gsy1
    if gx == 800 and gy == 350:
        gsx2 = 812
        gsy2 = 362
        bsx2 = -50
        bsy2 = -50
        rsx2 = -50
        rsy2 = -50
        ysx2 = -50
        ysy2 = -50
        return gsx2 and gsy2
    if bx == 150 and by == 250:
        bsx = 162
        bsy = 262
        bsx = -50
        rsy = -50
        rsx = -50
        gsy = -50
        ysx = -50
        ysy = -50
        return bsx and bsy
    if bx == 550 and by == 100:
        bsx1 = 562
        bsy1 = 112
        rsx1 = -50
        rsy1 = -50
        gsx1 = -50
        gsy1 = -50
        ysx1 = -50
        ysy1 = -50
        return bsx1 and bsy1
    if bx == 800 and by == 350:
        bsx2 = 812
        bsy2 = 362
        rsx2 = -50
        rsy2 = -50
        gsx2 = -50
        gsy2 = -50
        ysx2 = -50
        ysy2 = -50
        return bsx2 and bsy2
    if yx == 150 and yy == 250:
        ysx = 162
        ysy = 262
        bsx = -50
        bsy = -50
        gsx = -50
        gsy = -50
        rsx = -50
        rsy = -50
        return ysx and ysy
    if yx == 550 and yy == 100:
        ysx1 = 562
        ysy1 = 112
        bsx1 = -50
        bsy1 = -50
        gsx1 = -50
        gsy1 = -50
        rsx1 = -50
        rsy1 = -50
        return ysx1 and ysy1
    if yx == 800 and yy == 350:
        ysx2 = 812
        ysy2 = 362
        bsx2 = -50
        bsy2 = -50
        gsx2 = -50
        gsy2 = -50
        rsx2 = -50
        rsy2 = -50
        return ysx2 and ysy2

def check_win():
    global rsx, rsy, rsx1, rsy1, rsx2, rsy2, bsx, bsy, bsx1, bsy1, bsx2, bsy2, gsx, gsy, gsx1, gsy1, gsx2, gsy2, ysx, ysy, ysx1, ysy1, ysx2, ysy2, start
    if rsx == 162 and rsy == 262 and rsx1 == 562 and rsy1 == 112 and rsx2 == 812 and rsy2 == 362:
        DISPLAYSURF.blit(fontObj.render('RED WINS', True, Red, Black), textRectObj1)
        pygame.display.update()
        sleep(3)
        pygame.quit()
        sys.exit()
    if gsx == 162 and gsy == 262 and gsx1 == 562 and gsy1 == 112 and gsx2 == 812 and gsy2 == 362:
        DISPLAYSURF.blit(fontObj.render('GREEN WINS', True, Green, Black), textRectObj1)
        pygame.display.update()
        sleep(3)
        pygame.quit()
        sys.exit()
    if bsx == 162 and bsy == 262 and bsx1 == 562 and bsy1 == 112 and bsx2 == 812 and bsy2 == 362:
        DISPLAYSURF.blit(fontObj.render('BLUE WINS', True, Blue, Black), textRectObj1)
        pygame.display.update()
        sleep(3)
        pygame.quit()
        sys.exit()
    if ysx == 162 and ysy == 262 and ysx1 == 562 and ysy1 == 112 and ysx2 == 812 and ysy2 == 362:
        DISPLAYSURF.blit(fontObj.render('YELLOW WINS', True, Yellow, Black), textRectObj1)
        pygame.display.update()
        sleep(3)
        pygame.quit()
        sys.exit()



def destroy():
    global grx, gry, grx1, gry1, grx2, gry2, grx3, gry3, grx4, gry4, grx5, gry5, gpx, gpy, gpx1, gpy1, gpx2, gpy2, gpx3, gpy3, gpx4, gpy4, gpx5, gpy5, bbx, bby, hold, turn
    if bbx == grx and bby == gry:
        grx = -50
        gry = -50
        bbx = -50
        bby = -50
        turn = hold
        return gpx3 and gpy3 and bbx and bby and turn
    if bbx == grx1 and bby == gry1:
        grx1 = -50
        gry1 = -50
        bbx = -50
        bby = -50
        turn = hold
        return gpx3 and gpy3 and bbx and bby and turn
    if bbx == grx2 and bby == gry2:
        grx2 = -50
        gry2 = -50
        bbx = -50
        bby = -50
        turn = hold
        return gpx3 and gpy3 and bbx and bby and turn
    if bbx == grx3 and bby == gry3:
        grx3 = -50
        gry3 = -50
        bbx = -50
        bby = -50
        turn = hold
        return gpx3 and gpy3 and bbx and bby and turn
    if bbx == grx4 and bby == gry4:
        grx4 = -50
        gry4 = -50
        bbx = -50
        bby = -50
        turn = hold
        return gpx3 and gpy3 and bbx and bby and turn
    if bbx == grx5 and bby == gry5:
        grx5 = -50
        gry5 = -50
        bbx = -50
        bby = -50
        turn = hold
        return gpx3 and gpy3 and bbx and bby and turn
    if bbx == gpx and bby == gpy:
        gpx = -50
        gpy = -50
        bbx = -50
        bby = -50
        turn = hold
        return gpx3 and gpy3 and bbx and bby and turn
    if bbx == gpx1 and bby == gpy1:
        gpx1 = -50
        gpy1 = -50
        bbx = -50
        bby = -50
        turn = hold
        return gpx3 and gpy3 and bbx and bby and turn
    if bbx == gpx2 and bby == gpy2:
        gpx2 = -50
        gpy2 = -50
        bbx = -50
        bby = -50
        turn = hold
        return gpx3 and gpy3 and bbx and bby and turn
    if bbx == gpx3 and bby == gpy3:
        gpx3 = -50
        gpy3 = -50
        bbx = -50
        bby = -50
        turn = hold
        return gpx3 and gpy3 and bbx and bby and turn
    if bbx == gpx4 and bby == gpy4:
        gpx4 = -50
        gpy4 = -50
        bbx = -50
        bby = -50
        turn = hold
        return gpx3 and gpy3 and bbx and bby and turn
    if bbx == gpx5 and bby == gpy5:
        gpx5 = -50
        gpy5 = -50
        bbx = -50
        bby = -50
        turn = hold
        return gpx3 and gpy3 and bbx and bby and turn

start()
next_turn()

while True:
    for event in pygame.event.get(): # Exiting
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP: # Player Movement
            if event.key == K_UP and turn == 'YELLOW' and yy != 0:
                yy -= roll
            if event.key == K_DOWN and turn == 'YELLOW' and yy != 450:
                yy += roll
            if event.key == K_LEFT and turn == 'YELLOW' and yx != 0:
                yx -= roll
            if event.key == K_RIGHT and turn == 'YELLOW' and yx != 950:
                yx += roll
            if event.key == K_UP and turn == 'RED' and ry != 0:
                ry -= roll
            if event.key == K_DOWN and turn == 'RED' and ry != 450:
                ry += roll
            if event.key == K_LEFT and turn == 'RED' and rx != 0:
                rx -= roll
            if event.key == K_RIGHT and turn == 'RED' and rx != 950:
                rx += roll
            if event.key == K_UP and turn == 'BLUE' and by != 0:
                by -= roll
            if event.key == K_DOWN and turn == 'BLUE' and by != 450:
                by += roll
            if event.key == K_LEFT and turn == 'BLUE' and bx != 0:
                bx -= roll
            if event.key == K_RIGHT and turn == 'BLUE' and bx != 950:
                bx += roll
            if event.key == K_UP and turn == 'GREEN' and gy != 0:
                gy -= roll
            if event.key == K_DOWN and turn == 'GREEN' and gy != 450:
                gy += roll
            if event.key == K_LEFT and turn == 'GREEN' and gx != 0:
                gx -= roll
            if event.key == K_RIGHT and turn == 'GREEN' and gx != 950:
                gx += roll
            if event.key == K_UP and turn == "BOMB" and bby != 0:
                bby -= 50
            if event.key == K_DOWN and turn == "BOMB" and bby != 450:
                bby += 50
            if event.key == K_RIGHT and turn == "BOMB" and bbx != 950:
                bbx += 50
            if event.key == K_LEFT and turn == "BOMB" and bbx != 0:
                bbx -= 50
            if event.key == K_i and turn == 'RED' and rx == grx and ry == gry:
                rsx = 162
                rsy = 262
                bsx = -50
                bsy = -50
                gsx = -50
                gsy = -50
                ysx = -50
                ysy = -50
            if event.key == K_i and turn == 'BLUE' and bx == grx and by == gry:
                bsx = 162
                bsy = 262
                rsx = -50
                rsy = -50
                gsx = -50
                gsy = -50
                ysx = -50
                ysy = -50
            if event.key == K_i and turn == 'GREEN' and gx == grx and gy == gry:
                gsx = 162
                gsy = 262
                bsx = -50
                bsy = -50
                rsx = -50
                rsy = -50
                ysx = -50
                ysy = -50
            if event.key == K_i and turn == 'YELLOW' and yx == grx and yy == gry:
                ysx = 162
                ysy = 262
                bsx = -50
                bsy = -50
                gsx = -50
                gsy = -50
                rsx = -50
                rsy = -50
            if event.key == K_i and turn == 'RED' and rx == grx1 and ry == gry1:
                rsx = 162
                rsy = 262
                bsx = -50
                bsy = -50
                gsx = -50
                gsy = -50
                ysx = -50
                ysy = -50
            if event.key == K_i and turn == 'GREEN' and gx == grx1 and gy == gry1:
                gsx = 162
                gsy = 262
                bsx = -50
                bsy = -50
                rsx = -50
                rsy = -50
                ysx = -50
                ysy = -50
            if event.key == K_i and turn == 'BLUE' and bx == grx1 and by == gry1:
                bsx = 162
                bsy = 262
                rsx = -50
                rsy = -50
                gsx = -50
                gsy = -50
                ysx = -50
                ysy = -50
            if event.key == K_i and turn == 'YELLOW' and yx == grx1 and yy == gry1:
                ysx = 162
                ysy = 262
                bsx = -50
                bsy = -50
                gsx = -50
                gsy = -50
                rsx = -50
                rsy = -50
            if event.key == K_i and turn == 'RED' and rx == gpx and ry == gpy:
                rsx = 162
                rsy = 262
                bsx = -50
                bsy = -50
                gsx = -50
                gsy = -50
                ysx = -50
                ysy = -50
            if event.key == K_i and turn == 'BLUE' and bx == gpx and by == gpy:
                bsx = 162
                bsy = 262
                rsx = -50
                rsy = -50
                gsx = -50
                gsy = -50
                ysx = -50
                ysy = -50
            if event.key == K_i and turn == 'GREEN' and gx == gpx and gy == gpy:
                gsx = 162
                gsy = 262
                bsx = -50
                bsy = -50
                rsx = -50
                rsy = -50
                ysx = -50
                ysy = -50
            if event.key == K_i and turn == 'YELLOW' and yx == gpx and yy == gpy:
                ysx = 162
                ysy = 262
                bsx = -50
                bsy = -50
                gsx = -50
                gsy = -50
                rsx = -50
                rsy = -50
            if event.key == K_i and turn == 'RED' and rx == gpx1 and ry == gpy1:
                rsx = 162
                rsy = 262
                bsx = -50
                bsy = -50
                gsx = -50
                gsy = -50
                ysx = -50
                ysy = -50
            if event.key == K_i and turn == 'BLUE' and bx == gpx1 and by == gpy1:
                bsx = 162
                bsy = 262
                rsx = -50
                rsy = -50
                gsx = -50
                gsy = -50
                ysx = -50
                ysy = -50
            if event.key == K_i and turn == 'GREEN' and gx == gpx1 and gy == gpy1:
                gsx = 162
                gsy = 262
                bsx = -50
                bsy = -50
                rsx = -50
                rsy = -50
                ysx = -50
                ysy = -50
            if event.key == K_i and turn == 'YELLOW' and yx == gpx1 and yy == gpy1:
                ysx = 162
                ysy = 262
                bsx = -50
                bsy = -50
                gsx = -50
                gsy = -50
                rsx = -50
                rsy = -50
            if event.key == K_i and turn == 'RED' and rx == grx2 and ry == gry2:
                rsx1 = 562
                rsy1 = 112
                bsx1 = -50
                bsy1 = -50
                gsx1 = -50
                gsy1 = -50
                ysx1 = -50
                ysy1 = -50
            if event.key == K_i and turn == 'BLUE' and bx == grx2 and by == gry2:
                bsx1 = 562
                bsy1 = 112
                rsx1 = -50
                rsy1 = -50
                gsx1 = -50
                gsy1 = -50
                ysx1 = -50
                ysy1 = -50
            if event.key == K_i and turn == 'GREEN' and gx == grx2 and gy == gry2:
                gsx1 = 562
                gsy1 = 112
                bsx1 = -50
                bsy1 = -50
                rsx1 = -50
                rsy1 = -50
                ysx1 = -50
                ysy1 = -50
            if event.key == K_i and turn == 'YELLOW' and yx == grx2 and yy == gry2:
                ysx1 = 562
                ysy1 = 112
                bsx1 = -50
                bsy1 = -50
                gsx1 = -50
                gsy1 = -50
                rsx1 = -50
                rsy1 = -50
            if event.key == K_i and turn == 'RED' and rx == grx3 and ry == gry3:
                rsx1 = 562
                rsy1 = 112
                bsx1 = -50
                bsy1 = -50
                gsx1 = -50
                gsy1 = -50
                ysx1 = -50
                ysy1 = -50
            if event.key == K_i and turn == 'BLUE' and bx == grx3 and by == gry3:
                bsx1 = 562
                bsy1 = 112
                rsx1 = -50
                rsy1 = -50
                gsx1 = -50
                gsy1 = -50
                ysx1 = -50
                ysy1 = -50
            if event.key == K_i and turn == 'GREEN' and gx == grx3 and gy == gry3:
                gsx1 = 562
                gsy1 = 112
                bsx1 = -50
                bsy1 = -50
                rsx1 = -50
                rsy1 = -50
                ysx1 = -50
                ysy1 = -50
            if event.key == K_i and turn == 'YELLOW' and yx == grx3 and yy == gry3:
                ysx1 = 562
                ysy1 = 112
                bsx1 = -50
                bsy1 = -50
                gsx1 = -50
                gsy1 = -50
                rsx1 = -50
                rsy1 = -50
            if event.key == K_i and turn == 'RED' and rx == gpx2 and ry == gpy2:
                rsx1 = 562
                rsy1 = 112
                bsx1 = -50
                bsy1 = -50
                gsx1 = -50
                gsy1 = -50
                ysx1 = -50
                ysy1 = -50
            if event.key == K_i and turn == 'BLUE' and bx == gpx2 and by == gpy2:
                bsx1 = 562
                bsy1 = 112
                rsx1 = -50
                rsy1 = -50
                gsx1 = -50
                gsy1 = -50
                ysx1 = -50
                ysy1 = -50
            if event.key == K_i and turn == 'GREEN' and gx == gpx2 and gy == gpy2:
                gsx1 = 562
                gsy1 = 112
                bsx1 = -50
                bsy1 = -50
                rsx1 = -50
                rsy1 = -50
                ysx1 = -50
                ysy1 = -50
            if event.key == K_i and turn == 'YELLOW' and yx == gpx2 and yy == gpy2:
                ysx1 = 562
                ysy1 = 112
                bsx1 = -50
                bsy1 = -50
                gsx1 = -50
                gsy1 = -50
                rsx1 = -50
                rsy1 = -50
            if event.key == K_i and turn == 'RED' and rx == gpx3 and ry == gpy3:
                rsx1 = 562
                rsy1 = 112
                bsx1 = -50
                bsy1 = -50
                gsx1 = -50
                gsy1 = -50
                ysx1 = -50
                ysy1 = -50
            if event.key == K_i and turn == 'BLUE' and bx == gpx3 and by == gpy3:
                bsx1 = 562
                bsy1 = 112
                rsx1 = -50
                rsy1 = -50
                gsx1 = -50
                gsy1 = -50
                ysx1 = -50
                ysy1 = -50
            if event.key == K_i and turn == 'GREEN' and gx == gpx3 and gy == gpy3:
                gsx1 = 562
                gsy1 = 112
                bsx1 = -50
                bsy1 = -50
                rsx1 = -50
                rsy1 = -50
                ysx1 = -50
                ysy1 = -50
            if event.key == K_i and turn == 'YELLOW' and yx == gpx3 and yy == gpy3:
                ysx1 = 562
                ysy1 = 112
                bsx1 = -50
                bsy1 = -50
                gsx1 = -50
                gsy1 = -50
                rsx1 = -50
                rsy1 = -50
            if event.key == K_i and turn == 'RED' and rx == grx4 and ry == gry4:
                rsx2 = 812
                rsy2 = 362
                bsx2 = -50
                bsy2 = -50
                gsx2 = -50
                gsy2 = -50
                ysx2 = -50
                ysy2 = -50
            if event.key == K_i and turn == 'BLUE' and bx == grx4 and by == gry4:
                bsx2 = 812
                bsy2 = 362
                rsx2 = -50
                rsy2 = -50
                gsx2 = -50
                gsy2 = -50
                ysx2 = -50
                ysy2 = -50
            if event.key == K_i and turn == 'GREEN' and gx == grx4 and gy == gry4:
                gsx2 = 812
                gsy2 = 362
                bsx2 = -50
                bsy2 = -50
                rsx2 = -50
                rsy2 = -50
                ysx2 = -50
                ysy2 = -50
            if event.key == K_i and turn == 'YELLOW' and yx == grx4 and yy == gry4:
                ysx2 = 812
                ysy2 = 362
                bsx2 = -50
                bsy2 = -50
                gsx2 = -50
                gsy2 = -50
                rsx2 = -50
                rsy2 = -50
            if event.key == K_i and turn == 'RED' and rx == grx5 and ry == gry5:
                rsx2 = 812
                rsy2 = 362
                bsx2 = -50
                bsy2 = -50
                gsx2 = -50
                gsy2 = -50
                ysx2 = -50
                ysy2 = -50
            if event.key == K_i and turn == 'BLUE' and bx == grx5 and by == gry5:
                bsx2 = 812
                bsy2 = 362
                rsx2 = -50
                rsy2 = -50
                gsx2 = -50
                gsy2 = -50
                ysx2 = -50
                ysy2 = -50
            if event.key == K_i and turn == 'GREEN' and gx == grx5 and gy == gry5:
                gsx2 = 812
                gsy2 = 362
                bsx2 = -50
                bsy2 = -50
                rsx2 = -50
                rsy2 = -50
                ysx2 = -50
                ysy2 = -50
            if event.key == K_i and turn == 'YELLOW' and yx == grx5 and yy == gry5:
                ysx2 = 812
                ysy2 = 362
                bsx2 = -50
                bsy2 = -50
                gsx2 = -50
                gsy2 = -50
                rsx2 = -50
                rsy2 = -50
            if event.key == K_i and turn == 'RED' and rx == gpx4 and ry == gpy4:
                rsx2 = 812
                rsy2 = 362
                bsx2 = -50
                bsy2 = -50
                gsx2 = -50
                gsy2 = -50
                ysx2 = -50
                ysy2 = -50
            if event.key == K_i and turn == 'BLUE' and bx == gpx4 and by == gpy4:
                bsx2 = 812
                bsy2 = 362
                rsx2 = -50
                rsy2 = -50
                gsx2 = -50
                gsy2 = -50
                ysx2 = -50
                ysy2 = -50
            if event.key == K_i and turn == 'GREEN' and gx == gpx4 and gy == gpy4:
                gsx2 = 812
                gsy2 = 362
                bsx2 = -50
                bsy2 = -50
                rsx2 = -50
                rsy2 = -50
                ysx2 = -50
                ysy2 = -50
            if event.key == K_i and turn == 'YELLOW' and yx == gpx4 and yy == gpy4:
                ysx2 = 812
                ysy2 = 362
                bsx2 = -50
                bsy2 = -50
                gsx2 = -50
                gsy2 = -50
                rsx2 = -50
                rsy2 = -50
            if event.key == K_i and turn == 'RED' and rx == gpx5 and ry == gpy5:
                rsx2 = 812
                rsy2 = 362
                bsx2 = -50
                bsy2 = -50
                gsx2 = -50
                gsy2 = -50
                ysx2 = -50
                ysy2 = -50
            if event.key == K_i and turn == 'BLUE' and bx == gpx5 and by == gpy5:
                bsx2 = 812
                bsy2 = 362
                rsx2 = -50
                rsy2 = -50
                gsx2 = -50
                gsy2 = -50
                ysx2 = -50
                ysy2 = -50
            if event.key == K_i and turn == 'GREEN' and gx == gpx5 and gy == gpy5:
                gsx2 = 812
                gsy2 = 362
                bsx2 = -50
                bsy2 = -50
                rsx2 = -50
                rsy2 = -50
                ysx2 = -50
                ysy2 = -50
            if event.key == K_i and turn == 'YELLOW' and yx == gpx5 and yy == gpy5:
                ysx2 = 812
                ysy2 = 362
                bsx2 = -50
                bsy2 = -50
                gsx2 = -50
                gsy2 = -50
                rsx2 = -50
                rsy2 = -50
            if event.key == K_b:
                bbx = 500
                bby = 250
                hold = turn
                turn = "BOMB"
            if event.key == K_d:
                destroy()
            if event.key == K_RETURN: #Changing turn and getting new roll
                capture()
                next_turn()
                DISPLAYSURF.blit(fontObj.render(str(turn) + ' rolled a ' + str(rol), True, White, Black), textRectObj)
                pygame.display.update()
                sleep(1)

    # drawing board and players
    DISPLAYSURF.blit(grid, (0, 0))
    DISPLAYSURF.blit(ground_river, (grx, gry))
    DISPLAYSURF.blit(ground_river, (grx1, gry1))
    DISPLAYSURF.blit(ground_road, (gpx, gpy))
    DISPLAYSURF.blit(ground_road, (gpx1, gpy1))
    DISPLAYSURF.blit(castle, (150, 250))
    DISPLAYSURF.blit(ground_river, (grx2, gry2))
    DISPLAYSURF.blit(ground_river, (grx3, gry3))
    DISPLAYSURF.blit(ground_road, (gpx2, gpy2))
    DISPLAYSURF.blit(ground_road, (gpx3, gpy3))
    DISPLAYSURF.blit(castle, (550, 100))
    DISPLAYSURF.blit(ground_river, (grx4, gry4))
    DISPLAYSURF.blit(ground_river, (grx5, gry5))
    DISPLAYSURF.blit(ground_road, (gpx4, gpy4))
    DISPLAYSURF.blit(ground_road, (gpx5, gpy5))
    DISPLAYSURF.blit(castle, (800, 350))
    DISPLAYSURF.blit(red, (rx, ry))
    DISPLAYSURF.blit(green, (gx, gy))
    DISPLAYSURF.blit(blue, (bx, by))
    DISPLAYSURF.blit(yellow, (yx, yy))
    DISPLAYSURF.blit(bomb, (bbx, bby))
    pygame.draw.rect(DISPLAYSURF, Red, (rsx, rsy, 25, 25))
    pygame.draw.rect(DISPLAYSURF, Red, (rsx1, rsy1, 25, 25))
    pygame.draw.rect(DISPLAYSURF, Red, (rsx2, rsy2, 25, 25))
    pygame.draw.rect(DISPLAYSURF, Green, (gsx, gsy, 25, 25))
    pygame.draw.rect(DISPLAYSURF, Green, (gsx1, gsy1, 25, 25))
    pygame.draw.rect(DISPLAYSURF, Green, (gsx2, gsy2, 25, 25))
    pygame.draw.rect(DISPLAYSURF, Blue, (bsx, bsy, 25, 25))
    pygame.draw.rect(DISPLAYSURF, Blue, (bsx1, bsy1, 25, 25))
    pygame.draw.rect(DISPLAYSURF, Blue, (bsx2, bsy2, 25, 25))
    pygame.draw.rect(DISPLAYSURF, Yellow, (ysx, ysy, 25, 25))
    pygame.draw.rect(DISPLAYSURF, Yellow, (ysx1, ysy1, 25, 25))
    pygame.draw.rect(DISPLAYSURF, Yellow, (ysx2, ysy2, 25, 25))
    check_win()
    pygame.display.update()
    fpsClock.tick(FPS)

