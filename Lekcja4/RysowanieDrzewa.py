import random
import math
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import pygame
from pygame.locals import *

class Wezel():
    def __init__(self, dane = None):
        self.dane = dane
        self.lewy = None
        self.prawy = None

class DrzewoBinarne():
    def __init__(self):
        self.korzen = Wezel()
        self.dlugosc = 0

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
        self.dlugosc += 1

    def usun(self, dane):
        wezel = self.wyszukaj(dane)
        if wezel:
            rodzic = self.wyszukaj(self.znajdzRodzica(dane))
            if self.ktoreDziecko(dane) == 'prawy':
                if wezel.prawy:
                    rodzic.prawy = wezel.prawy
                    if wezel.lewy:
                        wezel.prawy.lewy = wezel.lewy
                else:
                    rodzic.prawy = None
                    if wezel.lewy:
                        rodzic.prawy = wezel.lewy
            else:
                if wezel.lewy:
                    rodzic.lewy = wezel.lewy
                    if wezel.prawy:
                        wezel.lewy.prawy = wezel.prawy
                else:
                    rodzic.lewy = None
                    if wezel.prawy:
                        rodzic.lewy = wezel.prawy

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

    def czyKorzen(self, x):
        if self.korzen.dane == x:
            return True
        return False
    
    def znajdzPoziom(self, x):
        return len(self.sciezka(x)) - 1

    def znajdzRodzica(self, x):
        return self.sciezka(x)[-2]

    def ktoreDziecko(self, x):
        if self.wyszukaj(self.znajdzRodzica(x)).lewy:
            if self.wyszukaj(self.znajdzRodzica(x)).lewy.dane == x:
                return 'lewy'
        return 'prawy'
    
    def sciezka(self, x):
        def _sciezka(wierzcholek, x, l=[]):
            if not wierzcholek:
                return []
            if wierzcholek.dane == x:
                return [wierzcholek.dane]
            res = _sciezka(wierzcholek.lewy, x)
            if res:
                return [wierzcholek.dane] + res
            res = _sciezka(wierzcholek.prawy, x)
            if res:
                return [wierzcholek.dane] + res
            return []
        return _sciezka(self.korzen, x)

    def poprzeczne(self):
        def _poprzeczne(wierzcholek):
            dane = []
            if wierzcholek:
                dane = _poprzeczne(wierzcholek.lewy)
                dane.append(wierzcholek.dane)
                dane +=_poprzeczne(wierzcholek.prawy)
            return dane
        return _poprzeczne(self.korzen)

    def wzdluzne(self):
        def _wzdluzne(wierzcholek):
            dane = []
            if wierzcholek:
                dane.append(wierzcholek.dane)
                dane += _wzdluzne(wierzcholek.lewy)
                dane +=_wzdluzne(wierzcholek.prawy)
            return dane
        return _wzdluzne(self.korzen)
    
    def wsteczne(self):
        def _wsteczne(wierzcholek):
            dane = []
            if wierzcholek:
                dane = _wsteczne(wierzcholek.lewy)
                dane +=_wsteczne(wierzcholek.prawy)
                dane.append(wierzcholek.dane)
            return dane
        return _wsteczne(self.korzen)
    
    def wyszukaj(self, dane):
        if self.korzen.dane == dane:
            return self.korzen        
        def wyszukaj_wierzcholek(wierzcholek, dane):
            if wierzcholek:
                if wierzcholek.dane:
                    if wierzcholek.dane == dane:
                        return wierzcholek
                    elif dane < wierzcholek.dane:
                        return wyszukaj_wierzcholek(wierzcholek.lewy, dane)
                    else:
                        return wyszukaj_wierzcholek(wierzcholek.prawy, dane)
        return wyszukaj_wierzcholek(self.korzen,dane)

def setup(root):
    embed = tk.Frame(root, width = 1200, height = 800)
    embed.grid(columnspan = (600), rowspan = 500)
    embed.pack(side = LEFT)
    os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
    os.environ['SDL_VIDEODRIVER'] = 'windib'
    pygame.init()
    pygame.font.init()
    window = pygame.display.set_mode(((1100,800)))
    window.set_alpha(None)
    return window

def rysujPlansze(window, root, drzewo, wspolrzendne):
    window.fill(pygame.Color(50,235,50))
    if drzewo.dlugosc > 0:
        for dane in drzewo.wzdluzne():
            x, y = obliczWspolrzedne(drzewo, dane, wspolrzendne)
            rysujWezel(window, x, y, dane, drzewo, wspolrzendne)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            None
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
    root.update()

def rysujWezel(window, x, y, dane, drzewo, wspolrzendne):
    pygame.draw.circle(window,pygame.Color(255,255,255),(x, y), 30)
    if not drzewo.czyKorzen(dane):
        startX, startY = wspolrzendne[drzewo.znajdzRodzica(dane)]
        if drzewo.ktoreDziecko(dane) == 'prawy':
            pygame.draw.line(window, pygame.Color(0,0,0), (startX+30,startY), (x-30,y))
        else:
            pygame.draw.line(window, pygame.Color(0,0,0), (startX-30,startY), (x+30,y))
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render(str(dane), False, (0, 0, 0))
    window.blit(textsurface,(x-obliczOffset(dane),y-20))

def obliczWspolrzedne(drzewo, dane, wspolrzendne):
    poziom = drzewo.znajdzPoziom(dane)
    y = 70*(poziom + 1)
    if drzewo.czyKorzen(dane):
        x = 550
    else:
        x = wspolrzendne[drzewo.znajdzRodzica(dane)][0]
        if drzewo.ktoreDziecko(dane) == 'prawy':
            if poziom < 4:
                x += 100*(4 - poziom)
            else:
                x += 100
        else:
            if poziom < 4:
                x -= 100*(4 - poziom)
            else:
                x -= 100
    wspolrzendne[dane] = (x, y)        
    return (x, y)

def obliczOffset(n):
    if n > 0:
        return (int(math.log10(n))+1)*7.5
    elif n == 0:
        return 10
    else:
        return (int(math.log10(-n))+2)*6

def budujGui(drzewo):
    root = tk.Tk()
    root.title('Binarne Drzewo Poszukiwań')
    root.option_add('*font', 'Calibri 22')
    window = setup(root)
    bInsert = Button(text = 'Dodaj',command=(lambda:popupInput('Dodaj', drzewo)))
    bInsert.pack()
    bRemove = Button(text = 'Usun', command=(lambda:popupInput('Usun', drzewo)))
    bRemove.pack()
    bSearch = Button(text = 'Wyszukaj', command=(lambda:popupInput('Wyszukaj', drzewo)))
    bSearch.pack()
    bInorder = Button(text = 'Poprzeczne', command=(lambda:popup('Poprzeczne', drzewo)))
    bInorder.pack()
    bPreorder = Button(text = 'Wzdluzne', command=(lambda:popup('Wzdluzne', drzewo)))
    bPreorder.pack()
    bPostorder = Button(text = 'Wsteczne', command=(lambda:popup('Wsteczne', drzewo)))
    bPostorder.pack()
    return root, window

def popupInput(s, drzewo):
    dane = simpledialog.askinteger('Wprowadz dane',s, minvalue=0, maxvalue=999)
    if s == 'Dodaj':
        if drzewo.wyszukaj(dane):
            messagebox.showerror('Error', 'Istnieje juz taki wezel')
        else:
            drzewo.dodaj(int(dane))
            messagebox.showinfo('Sukces','Poprawnie dodano wezel')
    elif s == 'Usun':
        if drzewo.wyszukaj(dane):
            drzewo.usun(int(dane))
            messagebox.showinfo('Sukces','Poprawnie usunięto wezel')
        else:
            messagebox.showerror('Error', 'Nie ma takiego wezla')
    elif s == 'Wyszukaj':
        if drzewo.wyszukaj(int(dane)):
            messagebox.showinfo('Sukces','Węzeł znajduje się w drzewie')
        else:
            messagebox.showerror('Error', 'Nie ma takiego wezla')

def popup(s, drzewo):
    if s == 'Poprzeczne':
        messagebox.showinfo('Poprzeczne', str(drzewo.poprzeczne()))
    elif s == 'Wzdluzne':
        messagebox.showinfo('Wzdluzne', str(drzewo.wzdluzne()))
    elif s == 'Wsteczne':
        messagebox.showinfo('Wsteczne', str(drzewo.wsteczne()))

d = DrzewoBinarne()
root, window = budujGui(d)
wspolrzendne = dict()

while True:
    rysujPlansze(window, root, d, wspolrzendne)
