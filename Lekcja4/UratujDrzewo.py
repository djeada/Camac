import random
import pygame
import math
from pygame.locals import *

class Wezel():
    def __init__(self, dane = None):
        self.dane = dane
        self.lewy = None
        self.prawy = None

class DrzewoBinarne():
    def __init__(self):
        self.korzen = Wezel()

    def dodaj(self, dane):
        if self.korzen.dane == None:
            self.korzen.dane = dane
        else:
            def dodaj_do_wierzcholka(wierzcholek, dane):
                if dane < wierzcholek.dane:
                    if wierzcholek.lewy == None:
                        wierzcholek.lewy = Wezel(dane)
                    else:
                        dodaj_do_wierzcholka(wierzcholek.lewy, dane)
                elif dane > wierzcholek.dane:
                    if wierzcholek.prawy == None:
                        wierzcholek.prawy = Wezel(dane)
                    else:
                        dodaj_do_wierzcholka(wierzcholek.prawy, dane)
            dodaj_do_wierzcholka(self.korzen, dane)

    def wyswietl(self):
        wynik = ''
        def wzdluzne(wynik, wierzcholek):
            if wierzcholek:
                wynik += (str(wierzcholek.dane) + '-')
                wynik = wzdluzne(wynik, wierzcholek.lewy)
                wynik = wzdluzne(wynik, wierzcholek.prawy)
            return wynik
        def poprzeczne(wynik, wierzcholek):
            if wierzcholek:
                wynik = wzdluzne(wynik, wierzcholek.lewy)
                wynik += (str(wierzcholek.dane) + '-')
                wynik = wzdluzne(wynik, wierzcholek.prawy)
            return wynik
        def wsteczne(wynik, wierzcholek):
            if wierzcholek:
                wynik = wzdluzne(wynik, wierzcholek.lewy)
                wynik = wzdluzne(wynik, wierzcholek.prawy)
                wynik += (str(wierzcholek.dane) + '-')
            return wynik
        print('Wzdluzne: ')
        print(wzdluzne(wynik, self.korzen))
        print('Poprzeczne: ')
        print(poprzeczne(wynik, self.korzen))
        print('Wsteczne: ')
        print(wsteczne(wynik, self.korzen))

    def wyszukaj(self, dane):
        if self.korzen.dane == dane:
            return self.korzen        
        def wyszukaj_wierzcholek(wierzcholek, dane):
            if wierzcholek:
                if wierzcholek.dane == dane:
                    return wierzcholek
                elif dane < wierzcholek.dane:
                    return wyszukaj_wierzcholek(wierzcholek.lewy, dane)
                else:
                    return wyszukaj_wierzcholek(wierzcholek.prawy, dane)
        return wyszukaj_wierzcholek(self.korzen,dane)

def setup():
    pygame.init()
    pygame.display.set_caption("Binarne Drzewo Poszukiwań")
    pygame.font.init()
    window = pygame.display.set_mode(((800,600)))
    window.set_alpha(None)
    window.fill(pygame.Color(0,0,0))
    return window

def drawBoard(window):
    window.fill(pygame.Color(0,0,0))
    drawCircle(window, 400, 40, 151)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            None
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()

def uzdrowBST(rodzic, dziecko):
    if dziecko:
        if dziecko == rodzic.lewy and dziecko.dane > rodzic.dane:
            swap(rodzic, dziecko)
        if dziecko == rodzic.prawy and dziecko.dane < rodzic.dane:
            swap(rodzic, dziecko)

def drawCircle(window, x, y, dane):
    pygame.draw.circle(window,pygame.Color(255,255,255),(x, y), 30)
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render(str(dane), False, (0, 0, 0))
    window.blit(textsurface,(x-calculateOffset(dane),y-20))

def calculateOffset(n):
    if n > 0:
        return (int(math.log10(n))+1)*7.5
    elif n == 0:
        return 10
    else:
        return (int(math.log10(-n))+2)*6

def swap(a, b):
    a.dane, b.dane = b.dane, a.dane

window = setup()
while True:
    drawBoard(window)
pygame.display.quit()
