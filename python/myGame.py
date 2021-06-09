import pygame
import random
import os
pygame.font.init()


#left to implement
#game over screen and game over logic
#level select screen
#title screen
#high scores
#delayed auto shift
#proper scoring and level entries and speeds
#maybe make real backgrounds, not just crappy placeholders

myFont = pygame.font.SysFont('comicsans',28)
BACKGROUND = pygame.image.load(os.path.join('Assets','back.png'))
HIGH_SCORES = pygame.image.load(os.path.join('Assets','scores.png'))
GRID_BLOCK_SIZE = 15
GRID_HEIGHT = 20
GRID_WIDTH = 10
GRID_OFFSET_X = 390
GRID_OFFSET_Y = 150
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (227,11,92)
BLUE = (6,64,239)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("my game")
board_state = [2049,2049,2049,2049,2049,2049,2049,2049,2049,2049,2049,2049,2049,2049,2049,2049,2049,2049,2049,2049,4095,4095,4095]
color_scheme = 0

class piece:
    def __init__(self, cPos, x, y, pos):
        self.x = x
        self.y = y
        self.cPos = cPos
        self.pos = pos
    def equals(self, p):
        self.x = p.x
        self.y = p.y 
        self.cPos = p.cPos
        self.pos = p.pos

myPiece = piece(0,2,5,[[48,48,0,0],[48,48,0,0],[48,48,0,0],[48,48,0,0]])
nextPiece = piece(0,2,5,[[48,48,0,0],[48,48,0,0],[48,48,0,0],[48,48,0,0]])

def draw_grid():
    for i in range(GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            if i>=myPiece.y and i<=3+myPiece.y and myPiece.pos[myPiece.cPos%4][i-myPiece.y]>>(10-j) & 1 :
                pygame.draw.rect(SCREEN,RED,pygame.Rect(j * (GRID_BLOCK_SIZE + 1) + GRID_OFFSET_X,i * (GRID_BLOCK_SIZE + 1) + GRID_OFFSET_Y, GRID_BLOCK_SIZE, GRID_BLOCK_SIZE))
            elif (board_state[i] >> (10-j)) & 1:
                pygame.draw.rect(SCREEN,BLUE,pygame.Rect(j * (GRID_BLOCK_SIZE + 1) + GRID_OFFSET_X,i * (GRID_BLOCK_SIZE + 1) + GRID_OFFSET_Y, GRID_BLOCK_SIZE, GRID_BLOCK_SIZE))
            else :
                pygame.draw.rect(SCREEN,BLACK,pygame.Rect(j * (GRID_BLOCK_SIZE + 1) + GRID_OFFSET_X,i * (GRID_BLOCK_SIZE + 1) + GRID_OFFSET_Y, GRID_BLOCK_SIZE, GRID_BLOCK_SIZE))

def draw_next_piece(next_piece):
    for i in range(4):
        for j in range(4):
            if (next_piece.pos[next_piece.cPos][i]>>(7-j)) & 1:
                pygame.draw.rect(SCREEN,RED,pygame.Rect(j * (GRID_BLOCK_SIZE + 1) + 707,i * (GRID_BLOCK_SIZE + 1) + 261, GRID_BLOCK_SIZE, GRID_BLOCK_SIZE))

def draw_to_SCREEN(menu,score,level,lines,next_piece):
    if menu == 0:
        SCREEN.blit(BACKGROUND,(0,0))
        score_text = myFont.render(str(score),1,BLACK)
        SCREEN.blit(score_text,(130,22))
        level_text = myFont.render(str(level),1,BLACK)
        SCREEN.blit(level_text,(130,62))
        lines_text = myFont.render(str(lines),1,BLACK)
        SCREEN.blit(lines_text,(130,101))
        draw_grid()
        draw_next_piece(next_piece)
    if menu == 1:
        SCREEN.blit(HIGH_SCORES,(0,0))
    pygame.display.update()

def checkRight():
    for i in range(4):
        if ((((myPiece.pos[myPiece.cPos][i]>>1) ^ board_state[myPiece.y+i]) - (myPiece.pos[myPiece.cPos][i]>>1)) != board_state[myPiece.y+i]):
            return False
    return True
            
def checkLeft():
    for i in range(4):
        if ((((myPiece.pos[myPiece.cPos][i]<<1) ^ board_state[myPiece.y+i]) - (myPiece.pos[myPiece.cPos][i]<<1)) != board_state[myPiece.y+i]):
            return False
    return True

def checkDown():
    for i in range(4):
        if ((((myPiece.pos[myPiece.cPos][i]) ^ board_state[myPiece.y+i+1]) - (myPiece.pos[myPiece.cPos][i])) != board_state[myPiece.y+i+1]):
            return False
    return True

def checkClear(check):
    if(check):
        for i in range(GRID_HEIGHT):
            if board_state[i] == 4095:
                for j in range(i-1):
                    board_state[i-j] = board_state[i-j-1] #this logic may cause problems when game grid is really high, may be out of bounds
                board_state[0] = 2049
                return 1 + checkClear(True)
    return 0

#might not work
def check_end_game():
    for i in range(4):
        if(myPiece.pos[myPiece.cPos][i]>>8 & board_state[i+1]>>8 & 1 or myPiece.pos[myPiece.cPos][i]>>5 & board_state[i+1]>>5 & 1 or myPiece.pos[myPiece.cPos][i]>>6 & board_state[i+1]>>6 & 1 or myPiece.pos[myPiece.cPos][i]>>7 & board_state[i+1]>>7 & 1):
            return True
    return False

def rotateCW():
    if checkCW():
        myPiece.cPos = (myPiece.cPos + 1) % 4

def rotateCCW():
    myPiece.cPos = (myPiece.cPos - 1) % 4

def checkCW():
    for i in range(4):
        if ((((myPiece.pos[(myPiece.cPos + 1) % 4][i]) ^ board_state[myPiece.y+i]) - (myPiece.pos[(myPiece.cPos + 1) % 4][i])) != board_state[myPiece.y+i]):
            return False
    return True

def checkCCW():
    for i in range(4):
        if ((((myPiece.pos[(myPiece.cPos - 1) % 4][i]) ^ board_state[myPiece.y+i]) - (myPiece.pos[(myPiece.cPos - 1) % 4][i])) != board_state[myPiece.y+i]):
            return False
    return True

def mergeBoardAndPiece():
    for i in range(4):
        board_state[i+myPiece.y] = board_state[i+myPiece.y] | myPiece.pos[myPiece.cPos][i]

def set_score(score,num,level):
    if num == 1:
        score += (40 * (level+1))
    if num == 2:
        score += (100 * (level+1))
    if num == 3:
        score += (300 * (level+1))
    if num == 4:
        score += (1200 * (level+1))
    return score

def check_lines(level,lines):
    return int(lines/10) > level

def newPiece():
    num = random.random() * 7
    nextPiece.cPos = 0
    nextPiece.x = 0
    nextPiece.y = -1
    if num == 0:
        #z
        nextPiece.pos = [[0,192,96,0],[64,192,128,0],[0,192,96,0],[64,192,128,0]]
    elif int(num) == 1:
        #s
        nextPiece.pos = [[0,96,192,0],[64,96,32,0],[0,96,192,0],[64,96,32,0]]
    elif int(num) == 2:
        #j
        nextPiece.pos = [[0,224,32,0],[64,64,192,0],[128,224,0,0],[96,64,64,0]]
    elif int(num) == 3:
        #l
        nextPiece.pos = [[0,224,128,0],[192,64,64,0],[32,224,0,0],[64,64,96,0]]
    elif int(num) == 4:
        #t
        nextPiece.pos = [[0,224,64,0],[64,192,64,0],[64,224,0,0],[64,96,64,0]]
    elif int(num) == 5:
        #i
        nextPiece.pos = [[0,240,0,0],[32,32,32,32],[0,240,0,0],[32,32,32,32]]
    else:
        #o
        nextPiece.pos = [[0,96,96,0],[0,96,96,0],[0,96,96,0],[0,96,96,0]]

def main():
    run = True
    clock = pygame.time.Clock()
    start_ticks = pygame.time.get_ticks()
    newPiece()
    myPiece.equals(nextPiece)
    newPiece()
    score = 0
    lines = 0
    level = 0
    menu = 0
    speed = 1000 - (level * 100)
    while run:
        clock.tick(60)
        if (pygame.time.get_ticks() - start_ticks) >= speed:
            if checkDown():
                myPiece.y += 1
                start_ticks = pygame.time.get_ticks()
            #elif check_end_game():
                #display game over on screen then wait a second and then change menu to 1
            else:
                mergeBoardAndPiece()
                myPiece.equals(nextPiece)
                newPiece()
                start_ticks = pygame.time.get_ticks()
                num = checkClear(True)
                score = set_score(score,num,level)
                lines += num
                if check_lines(level,lines):
                    level += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if checkDown():
                        myPiece.y += 1
                    else:
                        mergeBoardAndPiece()
                if event.key == pygame.K_UP:
                    rotateCW()
                if event.key == pygame.K_RIGHT and checkRight():
                    myPiece.x += 1
                    for i in range(4):
                        for j in range(4):
                            myPiece.pos[i][j] = myPiece.pos[i][j]>>1
                if event.key == pygame.K_LEFT and checkLeft():
                    myPiece.x -= 1
                    for i in range(4):
                        for j in range(4):
                            myPiece.pos[i][j] = myPiece.pos[i][j]<<1
        draw_to_SCREEN(menu,score,level,lines,nextPiece)
    pygame.quit()



if __name__ == "__main__":
    main()
