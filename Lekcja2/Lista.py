class Pudelko():
    def __init__(self, dane=None):
        self.dane = dane
        self.nastepny = None

class Lista():
    def __init__(self):
        self.glowa = Pudelko()

    def dodaj(self, dane):
        if self.glowa.dane == None:
            self.glowa.dane = dane
        else:
            licznik = self.glowa
            while licznik.nastepny != None:
                licznik = licznik.nastepny
            licznik.nastepny = Pudelko(dane)

    def wyswietl(self):
        if self.glowa.dane == None:
            print('Lista jest pusta')
        else:
            licznik = self.glowa
            while licznik.nastepny != None:
                print(licznik.dane)
                licznik = licznik.nastepny
            print(licznik.dane)

    def dlugosc(self):
        dlugosc = 0
        if self.glowa.dane != None:
            licznik = self.glowa
            dlugosc += 1
            while licznik.nastepny != None:
                licznik = licznik.nastepny
                dlugosc += 1
        return dlugosc

    def usun_ostatni(self):
        if self.glowa.dane != None:
            licznik = self.glowa
            while licznik.nastepny.nastepny != None:
                licznik = licznik.nastepny
            licznik.nastepny = None
            
    def wstaw(self, dane, i):
        if i > self.dlugosc() or i < 0:
            print('zly indesk')
            return
        if self.glowa.dane != None:
            nowy = Pudelko(dane)
            licznik = self.glowa
            pozycja = 0
            while licznik.nastepny != None:
                poprzednik = licznik
                licznik = licznik.nastepny
                if pozycja + 1 == i:
                    poprzednik.nastepny = nowy
                    nowy.nastepny = licznik
                    return
                pozycja += 1
            licznik.nastepny = None
            
    def usun(self, i):
        if self.glowa.dane == None:
            print('lista jest pusta!')
            return
        if i >= self.dlugosc() or i < 0:
            print('zly indeks')
            return
        if i == 0:
            self.glowa = self.glowa.nastepny
            return
        licznik = self.glowa
        pozycja = 0
        while licznik.nastepny != None:
            poprzednik = licznik
            licznik = licznik.nastepny
            if pozycja+1 == i:
                poprzednik.nastepny = licznik.nastepny
                return
            pozycja += 1
            
    def usun_duplikaty(self):
        poprzednik = None
        licznik = self.glowa
        duplikaty = {}
        while licznik:
            if licznik.dane in duplikaty:
                poprzednik.nastepny = licznik.nastepny
            else:
                duplikaty[licznik.dane] = 'xD'
                poprzednik = licznik
            licznik = licznik.nastepny
            
    def pobierz(self, i):
        if self.glowa.dane == None:
            print('lista jest pusta!')
            return
        if i >= self.dlugosc() or i < 0:
            print('zly indeks')
            return
        licznik = self.glowa
        pozycja = 0
        while licznik:
            if pozycja == i:
                return licznik.dane
            pozycja += 1
            licznik = licznik.nastepny

    def znajdzNajkrotsza(self):
        if self.glowa.dane == None:
            print('Lista jest pusta')
            return

        najkrotszy = self.glowa
        licznik = self.glowa
        while licznik.nastepny != None:
            if najkrotszy.dane[1] > licznik.dane[1]:
                najkrotszy = licznik
            licznik = licznik.nastepny
        if najkrotszy.dane[1] > licznik.dane[1]:
                najkrotszy = licznik
        return najkrotszy.dane

    def znajdzNajdluzsza(self):
        if self.glowa.dane == None:
            print('Lista jest pusta')
            return

        najdluzszy = self.glowa
        licznik = self.glowa
        while licznik.nastepny != None:
            if najdluzszy.dane[1] > licznik.dane[1]:
                najdluzszy = licznik
            licznik = licznik.nastepny
        if najdluzszy.dane[1] > licznik.dane[1]:
                najdluzszy = licznik
        return najdluzszy.dane

    def sortuj(self):
        print('Wybierz rodzaj sortowania')
        print('1. Alfabetycznie')
        print('2. Wzgledem ilosci stron')
        wybor = int(input())
        if wybor == 1:
            return self.sortuj_przez_scalanie(0)
        if wybor == 2:
            return self.sortuj_przez_scalanie(1)

    def podziel(self):
        dlugosc = self.dlugosc()
        if dlugosc == 0:
            return None
        if dlugosc == 1:
            return self.glowa

        a = Lista()
        b = Lista()
        
        srodek = int(dlugosc/2)
        licznik = self.glowa
        pozycja = 0

        while pozycja < srodek:
            a.dodaj(licznik.dane)
            licznik = licznik.nastepny
            pozycja += 1

        while licznik:
            b.dodaj(licznik.dane)
            licznik = licznik.nastepny
        
        return a,b

    def sortuj_przez_scalanie(self, x):
        if self.dlugosc() <= 1:
            return self
        else:
            a, b = self.podziel()
            return scal(a.sortuj_przez_scalanie(x), b.sortuj_przez_scalanie(x), x)

    def czyPalindrom(self):
        listaA = self.klonuj()
        self.odwroc()
        listaB = self.klonuj()
        self.odwroc()
        return porownaj(listaA, listaB)

    def klonuj(self):
        nowa = Lista()
        licznik = self.glowa
        while licznik.nastepny != None:
            nowa.dodaj(licznik.dane)
            licznik = licznik.nastepny
        nowa.dodaj(licznik.dane)
        return nowa
  
    def odwroc(self):
        poprzednik = None
        licznik = self.glowa
        while licznik:
            nastepnik = licznik.nastepny
            licznik.nastepny = poprzednik
            poprzednik = licznik
            licznik = nastepnik
        self.glowa = poprzednik
        
def porownaj(listaA, listaB):
    temp1 = listaA.glowa
    temp2 = listaB.glowa

    if (temp1 == None and temp2 == None):
        return True

    while (temp1 != None and temp2 != None):
        if (temp1.dane == temp2.dane):
            temp1 = temp1.nastepny
            temp2 = temp2.nastepny 
        else:
            return False
    return True

def scal(a,b,x):
    pozycja_a = pozycja_b = 0

    polaczone_listy = Lista()
    dlugosc_poloczonych_list = a.dlugosc() + b.dlugosc()

    while polaczone_listy.dlugosc() < dlugosc_poloczonych_list:
        if a.pobierz(pozycja_a)[x] <= b.pobierz(pozycja_b)[x]:
            polaczone_listy.dodaj(a.pobierz(pozycja_a))
            pozycja_a += 1
        else:
            polaczone_listy.dodaj(b.pobierz(pozycja_b))
            pozycja_b += 1

        if pozycja_a == a.dlugosc():
            while pozycja_b < b.dlugosc():
                polaczone_listy.dodaj(b.pobierz(pozycja_b))
                pozycja_b += 1

        elif pozycja_b == b.dlugosc():
            while pozycja_a < a.dlugosc():
                polaczone_listy.dodaj(a.pobierz(pozycja_a))
                pozycja_a += 1
                
    return polaczone_listy

lista = Lista()
lista.dodaj(('Pan Tadeusz', 340))
lista.dodaj(('Pan Amadeusz', 843))
lista.dodaj(('Pan Amadeusz', 843))
lista.dodaj(('Pan Tadeusz', 340))
print(lista.czyPalindrom())
