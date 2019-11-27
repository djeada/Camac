import random
import math
import pygame
from pygame.locals import *
import time

width = 1000
height = 600
sineValues = []
clock = pygame.time.Clock()
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)

class Angle():
    def __init__(self):
        self.angle = 0
        self.time = 0

    def check(self):
        if self.angle > 360:
            self.angle = 0
        self.time = 0

def setup():
    pygame.init()
    pygame.display.set_caption('Szereg Fouriera')
    window = pygame.display.set_mode(((1400,800)))
    window.set_alpha(None)
    window.fill(black)
    return window

def draw(window, theta, sineValues):
    theta.time += clock.tick()
    if theta.time > 30:
        window.fill(black)
        theta.angle = drawCircle(window, theta.angle, 150, (200, 400), sineValues)
        theta.check()
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            None
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()

def drawCircle(window, angle, radius, center, sineValues):
    pygame.draw.circle(window, white, center, 150, 1)
    theta = math.radians(angle)
    x = int(center[0] + radius * math.cos(theta))
    y = int(center[1] +radius * math.sin(theta))
    sineValues.insert(0,y)
    if len(sineValues) > 1200:
        sineValues.pop()
    pygame.draw.line(window, white, (x,y), center)
    pygame.draw.circle(window, white, (x,y), 10)
    pygame.draw.line(window, white, (x,y), (center[0] + radius + 20,sineValues[0]))
    for i in range(len(sineValues)):
        pygame.draw.circle(window, white, (i + center[0] + radius + 20,sineValues[i]), 3)
    return angle + 1

window = setup()
theta = Angle()
while True:
    draw(window, theta, sineValues)
