import random
import math
import pygame
from pygame.locals import *
import time

width = 1400
height = 800
totalCities = 100
cities = []

for i in range(totalCities):
    cities.append((random.randint(0,width),random.randint(0,height)))

def setup():
    pygame.init()
    pygame.display.set_caption('Komiwojazer')
    window = pygame.display.set_mode(((1400,800)))
    window.set_alpha(None)
    window.fill(pygame.Color(0,0,0))
    return window

def draw(cities, window):
    window.fill(pygame.Color(0,0,0))
    white = pygame.Color(255,255,255)
    for i in range(len(cities)):
            pygame.draw.circle(window, white, cities[i], 10)
            if i != len(cities) - 1:
                pygame.draw.line(window, white, cities[i], cities[i+1])
            else:
                pygame.draw.line(window, white, cities[len(cities)-1], cities[0])

    text(window, white, str(calcDistance(cities)))
    swap(random.randint(0,len(cities)-1),random.randint(0,len(cities)-1),cities)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            None
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()

def text(window, color, text):
    pygame.font.init()
    myfont = pygame.font.SysFont('Calibri MS', 16)
    textsurface = myfont.render(text, False, color)
    window.blit(textsurface,(0,0))

def swap(i,j, tablica):
    temp = tablica[i]
    tablica[i] = tablica[j]
    tablica[j] = temp

def calcDistance(cities):
    suma = 0
    for i in range(len(cities)-1):
        suma +=  math.sqrt((cities[i][0]-cities[i+1][0])**2 + (cities[i][1]-cities[i+1][1])**2)
    suma +=  math.sqrt((cities[0][0]-cities[len(cities)-1][0])**2 + (cities[0][1]-cities[len(cities)-1][1])**2)
    return suma

window = setup()
while True:
    draw(cities,window)
