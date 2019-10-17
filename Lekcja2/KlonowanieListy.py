import random

class Pudelko():
    def __init__(self, dane=None):
        self.dane = dane
        self.nastepny = None
        self.losowy = None

class Lista():
    def __init__(self):
        self.glowa = Pudelko()
        self.poloczenia = {}

    def dodaj(self, dane):
        if self.glowa.dane == None:
            self.glowa.dane = dane
        else:
            licznik = self.glowa
            i = 0
            while licznik.nastepny != None:
                licznik = licznik.nastepny
            licznik.nastepny = Pudelko(dane)

    def ustawLosowe(self):
        if self.glowa:
            licznik1 = self.glowa
            licznik2 = self.glowa
            while licznik1.nastepny != None:
                if licznik1 != licznik2 and random.randint(1,7) % 3 == 0 and licznik2:
                    licznik1.losowy = licznik2
                    licznik1 = licznik1.nastepny
                    dodajDoSlownika(self.poloczenia, licznik1.dane, licznik2.dane)
                licznik2 = licznik2.nastepny
                if licznik2 == None:
                    licznik2 = self.glowa
            licznik1.losowy = self.glowa
            
    def wyswietl(self):
        if self.glowa.dane == None:
            print('Lista jest pusta')
        else:
            licznik = self.glowa
            while licznik.nastepny != None:
                print(licznik.dane)
                licznik = licznik.nastepny
            print(licznik.dane)

    def wyswietlLosowe(self):
        if self.glowa.dane == None:
            print('Lista jest pusta')
        else:
            wyswietlSlownik(self.poloczenia)
            '''
            licznik = self.glowa
            while licznik.losowy != self.glowa:
                print(licznik.dane)
                licznik = licznik.losowy
            print(licznik.dane)
            '''

    def dlugosc(self):
        dlugosc = 0
        if self.glowa.dane != None:
            licznik = self.glowa
            dlugosc += 1
            while licznik.nastepny != None:
                licznik = licznik.nastepny
                dlugosc += 1
        return dlugosc

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

def dodajDoSlownika(slownik, klucz, wartosc):
    if klucz in slownik:
        slownik[klucz] = slownik[klucz] + ' oraz ' + str(wartosc)
    else:
        slownik[klucz] = str(wartosc)

def wyswietlSlownik(slownik):
    for x in slownik:
        print(x , ': ', slownik[x])

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

lista = Lista()
for i in range(10):
    lista.dodaj(i)
lista.ustawLosowe()
print('Lista: ')
lista.wyswietl()
print('Polaczenia losowe: ')
lista.wyswietlLosowe()



