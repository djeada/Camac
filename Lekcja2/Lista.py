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
            return 'Lista jest pusta'

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
            return 'Lista jest pusta'

        najdluzszy = self.glowa
        licznik = self.glowa
        while licznik.nastepny != None:
            if najdluzszy.dane[1] < licznik.dane[1]:
                najdluzszy = licznik
            licznik = licznik.nastepny
        if najdluzszy.dane[1] < licznik.dane[1]:
                najdluzszy = licznik
        return najdluzszy.dane

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

def menu(lista):
    while True:
        print("1. Dodaj nowa pozycje na koniec listy")
        print("2. Dodaj nowa pozycje na okreslone miejsce")
        print("3. Sprawdz dlugosc listy")
        print("4. Wyswietl liste")
        print("5. Usun pozycje z listy")
        print("6. Znajdz najdluzsza ksiazke")
        print("7. Znajdz najkrotsza ksiazke")
        print("8. Sortuj liste alfabetycznie")
        print("9. Sortuj liste po ilosci stron")
        print("10. Usun duplikaty z listy")
        print("11. Sprawdz czy lista jest palindromem")
        print("12. Koniec")
        wybor = int(input())
        if(wybor == 1):
            print('')
            print('Podaj nazwe książki: ')
            nazwa = input()
            print('Podaj ilosc stron: ')
            strony = int(input())
            print('')
            lista.dodaj((nazwa,strony))
        if(wybor == 2):
            print('')
            print('Podaj nazwe książki: ')
            nazwa = input()
            print('Podaj ilosc stron: ')
            strony = int(input())
            print('Podaj indeks: ')
            indeks = int(input())
            print('')
            lista.wstaw((nazwa,strony),indeks)
        if(wybor == 3):
            print('')
            print('Dlugosc list: ', lista.dlugosc())
            print('')
        if(wybor == 4):
            lista.wyswietl()
        if(wybor == 5):
            print('')
            print('Podaj indeks: ')
            indeks = int(input())
            lista.usun(indeks)
        if(wybor == 6):
            wynik = lista.znajdzNajdluzsza()
            nazwa = wynik[0]
            strony = wynik[1]
            print('')
            print('Najdluzsza ksiazka to ', nazwa, ' majaca ', strony, ' stron.')
            print('')
        if(wybor == 7):
            wynik = lista.znajdzNajkrotsza()
            nazwa = wynik[0]
            strony = wynik[1]
            print('')
            print('Najkrotsza ksiazka to ', nazwa, ' majaca ', strony, ' stron.')
            print('')
        if(wybor == 8):
            lista = lista.sortuj_przez_scalanie(0)
        if(wybor == 9):
            lista = lista.sortuj_przez_scalanie(1)
        if(wybor == 10):
            lista.usun_duplikaty()
        if(wybor == 11):
            if lista.czyPalindrom():
                print('')
                print('Lista jest palindromem')
                print('')
            else:
                print('')
                print('Lista nie jest palindromem')
                print('')
        if(wybor == 12):
            break
menu(Lista())
