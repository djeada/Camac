import random
import time
import pygame
import winsound
from pygame.locals import *

def setup():
    pygame.init()
    pygame.display.set_caption("Algorytmy Sortowania")
    window = pygame.display.set_mode(((1000,800)))
    window.set_alpha(None)
    window.fill(pygame.Color(0,0,0))
    return window

def draw(tab, szerokosci, window):
    window.fill(pygame.Color(0,0,0))
    for i in range(len(tab)):
        pygame.draw.rect(window,pygame.Color(255,255,255),(szerokosci[i],800-tab[i],10,tab[i]),0)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            None
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()

def swap(i,j, tablica):
    temp = tablica[i]
    tablica[i] = tablica[j]
    tablica[j] = temp

def znajdzMin(tablica):
    minimum = tablica[0]
    indeks = 0
    for i in range(1,len(tablica)):
        if tablica[i] < minimum:
            minimum = tablica[i]
            indeks = i
    return indeks

def sortowanie_babelkowe(tablica, szerokosci, window):
    for i in range(len(tablica)):
        for j in range(len(tablica)):
            if tablica[i] < tablica[j]:
                swap(i, j, tablica)
                winsound.Beep(tablica[j] + 2000,10)
            draw(tablica, szerokosci, window)

def sortowanie_wybieranie(tablica, szerokosci, window):
    for i in range(len(tablica)):
        indeks = znajdzMin(tablica[i:len(tablica)]) + i
        swap(i,indeks,tablica)
        draw(tablica, szerokosci, window)
        winsound.Beep(tablica[i] + 2000,10)


def sortowanie_szybkie(tablica, szerokosci, window):
    if len(tablica) > 1:
        draw(tablica, szerokosci, window)
        winsound.Beep(random.randint(0,100) + 2000,10)    
        return sortowanie_szybkie([x for x in tablica[1:] if x < tablica[0]], szerokosci, window) + [x for x in tablica if x == tablica[0]] + sortowanie_szybkie([x for x in tablica[1:] if x > tablica[0]], szerokosci, window)
    else:
        return tablica

def wypisz_slownik(slownik):
    for key in slownik:
        print(key, " ", slownik[key])

tab = []
czas = {}
szerokosci = []
szerokosc = 0

for i in range(100):
    losowa = random.randint(0,800)
    tab.append(losowa)
    szerokosci.append(szerokosc)
    szerokosc += 10

window = setup()

def menu(tab, szerokosci, window, czas):
    while True:
        print("Wybierz sortowanie:")
        print("1. Babelkowe")
        print("2. Wybieranie")
        print("3. Szybkie")
        print("4. Zliczanie")
        print("5. Kopcowanie")
        print("6. Pozycjne")
        print("7. Porownaj czas dla roznych sortowan")
        wybor = int(input())
        if(wybor == 1):
            start_time = time.time()
            sortowanie_babelkowe(tab, szerokosci, window)
            czas["babelkowe"] = time.time() - start_time
        if(wybor == 2):
            start_time = time.time()
            sortowanie_wybieranie(tab, szerokosci, window)
            czas["wybieranie"] = time.time() - start_time
        if(wybor == 3):
            start_time = time.time()
            sortowanie_szybkie(tab, szerokosci, window)
            czas["szybkie"] = time.time() - start_time
        if(wybor == 7):
            wypisz_slownik(czas)

menu(tab, szerokosci, window, czas)
            
