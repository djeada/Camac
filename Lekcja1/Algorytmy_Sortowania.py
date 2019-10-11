import random
import time
import pygame
from pygame.locals import *

try:
    import winsound
except ImportError:
    import os
    def playsound(frequency,duration):
        #apt-get install beep
        os.system('beep -f %s -l %s' % (frequency,duration))
else:
    def playsound(frequency,duration):
        winsound.Beep(frequency,duration)



def setup():
    pygame.init()
    pygame.display.set_caption("Algorytmy Sortowania")
    window = pygame.display.set_mode(((1400,800)))
    window.set_alpha(None)
    window.fill(pygame.Color(0,0,0))
    return window

def draw(tab, szerokosci, window):
    window.fill(pygame.Color(0,0,0))
    for i in range(len(tab)):
        pygame.draw.rect(window,pygame.Color(255,255,255),(szerokosci[i],800-tab[i],3,tab[i]),0)
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

def znajdzMax(tablica):
    maksimum = tablica[0]
    indeks = 0
    for i in range(1,len(tablica)):
        if tablica[i] > maksimum:
            maksimum = tablica[i]
            indeks = i
    return indeks


def kopcuj(tablica, n, i):
    maksimum = i
    l = 2 * i + 1
    r = 2 * i + 2 
 
    if l < n and tablica[i] < tablica[l]:
        maksimum = l
 
    if r < n and tablica[maksimum] < tablica[r]:
        maksimum = r
 
    if maksimum != i:
        swap(i, maksimum, tablica)
        kopcuj(tablica, n,maksimum)

def sortowanie_babelkowe(tablica, szerokosci, window):
    for i in range(len(tablica)):
        for j in range(i):
            if tablica[i] < tablica[j]:
                swap(i, j, tablica)
                playsound(tablica[j] + 2000,10)
            draw(tablica, szerokosci, window)

def sortowanie_wybieranie(tablica, szerokosci, window):
    for i in range(len(tablica)):
        indeks = znajdzMin(tablica[i:len(tablica)]) + i
        swap(i,indeks,tablica)
        draw(tablica, szerokosci, window)
        playsound(tablica[i] + 2000,10)

def sortowanie_szybkie(tablica, szerokosci, window):
    if len(tablica) > 1:
        draw(tablica, szerokosci, window)
        playsound(random.randint(0,100) + 2000,10)    
        return sortowanie_szybkie([x for x in tablica[1:] if x < tablica[0]], szerokosci, window) + [x for x in tablica if x == tablica[0]] + sortowanie_szybkie([x for x in tablica[1:] if x > tablica[0]], szerokosci, window)
    else:
        return tablica

def sortowanie_zliczanie(tablica, szerokosci, window):
    maksimum = tablica[znajdzMax(tablica)]+1
    licznik = [0]*maksimum           
    
    for x in tablica:
        licznik[x] += 1             

    i = 0
    for x in range(maksimum):            
        for y in range(licznik[x]):  
            tablica[i] = x
            i += 1
            draw(tablica, szerokosci, window)
            playsound(random.randint(0,100) + 2000,10)

def sortowanie_kopcowanie(tablica, szerokosci, window):
    dlugosc = len(tablica)
    for i in range(dlugosc, 0, -1):
        kopcuj(tablica, dlugosc, i)
    for i in range(dlugosc-1, 0, -1):
        swap(i, 0, tablica)
        kopcuj(tablica, i, 0)
        draw(tablica, szerokosci, window)
        playsound(i + 2000,10)
            
def wypisz_slownik(slownik):
    for key in slownik:
        print(key, " ", slownik[key])

tab = []
czas = {}
szerokosci = []
szerokosc = 0

for i in range(500):
    losowa = random.randint(0,800)
    tab.append(losowa)
    szerokosci.append(szerokosc)
    szerokosc += 2.8

def menu(tab, szerokosci, czas):
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
            temp = list(tab)
            window = setup()
            start_time = time.time()
            sortowanie_babelkowe(temp, szerokosci, window)
            czas["babelkowe"] = time.time() - start_time
            pygame.display.quit()
        if(wybor == 2):
            temp = list(tab)
            window = setup()
            start_time = time.time()
            sortowanie_wybieranie(temp, szerokosci, window)
            czas["wybieranie"] = time.time() - start_time
            pygame.display.quit()
        if(wybor == 3):
            temp = list(tab)
            window = setup()
            start_time = time.time()
            sortowanie_szybkie(temp, szerokosci, window)
            czas["szybkie"] = time.time() - start_time
            pygame.display.quit()
        if(wybor == 4):
            temp = list(tab)
            window = setup()
            start_time = time.time()
            sortowanie_zliczanie(temp, szerokosci, window)
            czas["zliczanie"] = time.time() - start_time
            pygame.display.quit()
        if(wybor == 5):
            temp = list(tab)
            window = setup()
            start_time = time.time()
            sortowanie_kopcowanie(temp, szerokosci, window)
            czas["kopcowanie"] = time.time() - start_time
            pygame.display.quit()
        if(wybor == 7):
            wypisz_slownik(czas)

menu(tab, szerokosci, czas)
