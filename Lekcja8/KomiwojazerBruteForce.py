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
    cities.append((random.randint(30,width),random.randint(40,height)))

minimum = cities

def setup():
    pygame.init()
    pygame.display.set_caption('Komiwojazer')
    window = pygame.display.set_mode(((1400,800)))
    window.set_alpha(None)
    window.fill(pygame.Color(0,0,0))
    return window

def draw(window, cities, minimum, x, y):
    window.fill(pygame.Color(0,0,0))
    white = pygame.Color(255,255,255)
    for i in range(len(minimum)):
            pygame.draw.circle(window, white, minimum[i], 10)
            if i != len(minimum) - 1:
                pygame.draw.line(window, white, minimum[i], minimum[i+1])
            else:
                pygame.draw.line(window, white, minimum[len(minimum)-1], minimum[0])

    minimum = findNewMin(minimum, cities)
    text(window, white, 'Current distance: ' + str("%.2f" % calcDistance(minimum)), 5, 5)
    text(window, white, 'Current generation: ' + str(y*totalCities + x), 5, 35)

    swap(x,y,cities)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            None
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()

def text(window, color, text,x, y):
    pygame.font.init()
    myfont = pygame.font.SysFont('Calibri MS', 30)
    textsurface = myfont.render(text, False, color)
    window.blit(textsurface,(x,y))

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

def findNewMin(minimum, cities):
    if calcDistance(cities) < calcDistance(minimum):
        return cities
    return minimum

window = setup()
while True:
    for y in range(totalCities):
        for x in range(totalCities):
            if x != y:
                draw(window, cities, minimum, x, y)
