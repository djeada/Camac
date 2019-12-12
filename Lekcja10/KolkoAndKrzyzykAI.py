import random
import math
import pygame
from pygame.locals import *
import time

black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
width = 900
height = 700
N = 3
box_width = width//N
box_height = height//N
board = [['' for x in range(N)] for x in range(N)]
number_of_moves = 0
ai = 'X'
human = 'O'

def setup():
    pygame.init()
    pygame.display.set_caption('Kolko i Krzyzyk')
    window = pygame.display.set_mode(((width,height)))
    window.set_alpha(None)
    window.fill(black)
    return window

def text(window, text,x, y):
    pygame.font.init()
    myfont = pygame.font.SysFont('Calibri MS', 80)
    textsurface = myfont.render(text + ' has won!', False, white)
    window.blit(textsurface,(x,y))
                         
def draw(window, board):
    window.fill(black)
    draw_board(window)
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == 'X':
                drawCharachter(window, 'X', int(0.2*box_width)+x*width//3, int(0.2*box_height)+y*box_height)
            if board[y][x] == 'O':
                drawCharachter(window, 'O' , box_width//2 + x*box_width, box_height//2 +y*box_height)
        
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            humanMove(x,y)
            global number_of_moves
            number_of_moves += 1
            if number_of_moves == N*N:
                endScreen(window, 'None') 
            result = checkWinner()
            if not result:
                aiMove()
                number_of_moves += 1
                result = checkWinner()
                if result:
                    endScreen(window, result) 
            else:
                endScreen(window, result) 
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()

def endScreen(window, result):
    while True:
        window.fill(black)
        text(window, result, int(0.6*width//2), height//2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()

def draw_board(window):
    for i in range(N-1):
        pygame.draw.line(window, white, (0,(i+1)*box_height), (width,(i+1)*box_height),3)
    for i in range(N-1):
        pygame.draw.line(window, white, ((i+1)*box_width,0), ((i+1)*box_width,height),3)
        
def drawCharachter(window, charachter, x, y):
    if charachter == 'X':
        pygame.draw.line(window, white, (x,y), (x+int(0.6*box_width), y+int(0.6*box_height)), 5)
        pygame.draw.line(window, white, (x, y+int(0.6*box_height)), (x+int(0.6*box_width), y), 5)
    else:
        pygame.draw.circle(window, white, (x,y), int(0.4*box_width) if width < height else int(0.4*box_height), 5)

def humanMove(x, y):
    for i in range(N):
        for j in range(N):
            if abs(box_width//2+ box_width * j - x) < box_width//2 and abs(box_height//2+ box_height * i - y) < box_height//2:
                if not board[i][j]:
                    board[i][j] = human
    
def aiMove():
    bestScore = float('-inf')
    for i in range(N):
        for j in range(N):
            if not board[i][j]:
                board[i][j] = ai
                score = minimax(board, 0 , True)
                board[i][j] = ''
                bestScore = max(bestScore, score)
                bestMove = (i, j)
    board[bestMove[0]][bestMove[1]] = ai
            
def minimax(board, depth, isMax):
    if isMax:
        bestScore = float('-inf')
        for i in range(N):
            for j in range(N):
                if not board[i][j]:
                    board[i][j] = ai
                    score = minimax(board, depth+1, False)
                    board[i][j] = ''
                    bestScore = max(score,bestScore)
    else:
        bestScore = float('inf')
        for i in range(N):
            for j in range(N):
                if not board[i][j]:
                    board[i][j] = human
                    score = minimax(board, depth+1, True)
                    board[i][j] = ''
                    bestScore = min(score,bestScore)
    return bestScore
        
def checkWinner():
    #horizontal
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
    #vertical
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    #diagonal
    if(board[0][0] == board[1][1] == board[2][2]):
        return board[0][0]
    if(board[2][0] == board[1][1] == board[0][2]):
        return board[2][0]

window = setup()
while True:
    draw(window, board)
