# -*- coding: utf-8 -*-
import os
import sys
import getch

SCREEN = []
PLAYER = {'X':0, 'Y':0, 'BX':0, 'BY':0,}
STONES = []
PITS   = []

class init():
    def __init__(self):
        self.field()
        self.player()
        self.stones(6,3)
        self.pits(6,2)
        self.stones(4,3)
        self.pits(4,2)

    def field(self,s_width=10,s_height=6):
        global SCREEN
        row = []
        for y in range(s_height):
            for x in range(s_width):
                row.append("*")
            row.append("\n")
            SCREEN.append(row)
            row = []
        for y in range(len(SCREEN)-2):
            for x in range(len(SCREEN[0])-3):
                SCREEN[y+1][x+1] = '.'

    def player(self,p_x=3,p_y=3):
        global PLAYER
        PLAYER['X'] = p_x
        PLAYER['BX'] = p_x
        PLAYER['Y'] = p_y
        PLAYER['BY'] = p_y

    def stones(self,x,y):
        global STONES
        STONES.append([x,y])

    def pits(self,x,y):
        global PITS
        PITS.append([x,y])

def move(x=0,y=0):
    '''update player pos'''
    global PLAYER
    next_x = PLAYER['X']+x
    next_y = PLAYER['Y']+y
    if SCREEN[next_y][next_x]=='o':
        movestone(x,y,next_x,next_y)
    if SCREEN[next_y][next_x]=='.':
        PLAYER['BX'] = PLAYER['X']
        PLAYER['BY'] = PLAYER['Y']
        PLAYER['X'] = next_x
        PLAYER['Y'] = next_y

def movestone(x,y,nx,ny): 
    global SCREEN
    global STONES
    stone = [nx,ny]
    if  SCREEN[ny+y][nx+x]=='.' or \
        SCREEN[ny+y][nx+x]=='x':
        for j in range(len(STONES)):
            if STONES[j] == stone:
                STONES[j] = [nx+x,ny+y]
                SCREEN[ny][nx] = '.'

def key():
    key = getch.getch()
    if key == 'h':
        move(-1,0)
    if key == 'j':
        move(0,1)
    if key == 'k':
        move(0,-1)
    if key == 'l':
        move(1,0)
    if key == 'q':
        sys.exit()

class draw():
    def __init__(self):
        self.player()
        self.stones()
        self.pits()
        self.field()
        self.player2()
        self.finish()

    def player(self):
        global SCREEN
        SCREEN[PLAYER['Y']][PLAYER['X']] = '@'

    def player2(self):
        global SCREEN
        SCREEN[PLAYER['BY']][PLAYER['BX']] = '.'

    def field(self):
        buffer = []
        for x in SCREEN:
            buffer.append(''.join(x))
        print(''.join(buffer))

    def pits(self):
        global SCREEN
        for x in PITS:
            px,py = x
            SCREEN[py][px] = 'x'
            if x in STONES:
                SCREEN[py][px] = '0'

    def stones(self):
        for x in STONES:
            sx,sy = x
            SCREEN[sy][sx] = 'o'

    def finish(self):
        finish = 0
        for x in SCREEN:
            for y in x:
                if 'x' in y:
                    finish = 1
        if finish == 0:
            print('win!!')



def monitor():
    print(PLAYER)
    print(STONES)
    print(PITS)

init()
    # update()
    # draw()
os.system('clear')
while True:
    move()
    draw()
    # monitor()
    key()
    os.system('clear')
