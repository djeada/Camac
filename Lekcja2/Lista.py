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
        if i > self.dlugosc() or i < 0:
            print('zly indesk')
            return
        if self.glowa.dane != None:
            licznik = self.glowa
            pozycja = 0
            while licznik.nastepny.nastepny != None:
                poprzednik = licznik
                licznik = licznik.nastepny
                if pozycja + 1 == i:
                    poprzednik.nastepy = licznik.nastepny
                    return
                pozycja += 1
            licznik.nastepny = None

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

listaA = Lista()
listaA.dodaj(('Pan Tadeusz', 340))
listaA.dodaj(('Pan Amadeusz', 843))
listaA.dodaj(('Pan Maxwell', 143))
listaA.dodaj(('Pan Tadeusz', 356))
listaA.usun_ostatni()
listaA.wstaw(('Hej',33), 1)
listaA.wyswietl()
print('Najkrotsza ksiazka to ', listaA.znajdzNajkrotsza())
print(listaA.dlugosc())
