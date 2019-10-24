import random

class HaszMapa:
    def __init__(self, rozmiar=10):
        self.rozmiar = rozmiar
        self.tablica = [None] * self.rozmiar

    def transformacja_kluczowa(self, klucz):
        hash = 0
        for c in str(klucz):
            hash += ord(c)
        return hash % self.rozmiar
    
    def dodaj(self, klucz, wartosc):
        klucz_hash = self.transformacja_kluczowa(klucz)
        klucz_wartosc = [klucz, wartosc]

        if self.tablica[klucz_hash] is None:
            self.tablica[klucz_hash] = list([klucz_wartosc])
            return
        else:
            for para in self.tablica[klucz_hash]:
                if para[0] == klucz:
                    para[1] = wartosc
                    return
                self.tablica[klucz_hash].append(klucz_wartosc)
                return

    def pobierz(self, klucz):
        klucz_hash = self.transformacja_kluczowa(klucz)
        if self.tablica[klucz_hash] is not None:
            for para in self.tablica[klucz_hash]:
                if para[0] == klucz:
                    return para[1]
        return None

    def usun(self, klucz):
        klucz_hash = self.transformacja_kluczowa(klucz)

        if self.tablica[klucz_hash] is None:
            return False
        for i in range(0, len(self.tablica[klucz_hash])):
            if self.tablica[klucz_hash][i][0] == klucz:
                self.tablica[klucz_hash].pop(i)
                return True
            
    def wyswietl(self):
        for item in self.tablica:
            if item:
                for x in item:
                    print(x[0], ' : ', x[1])

def dodaj_ksiazke(lista_ksiazek, klucze):
    ksiazka = HaszMapa(len(klucze))
    while 1:
        print('Podaj tytul ksiazki')
        tytul = input()
        if czy_ksiazka(lista_ksiazek, tytul):
            print('Ksiazka o tytule ', tytul, ' jest juz w naszym zbiorze!')
        else:
            ksiazka.dodaj('Tytul', tytul)
            break

    for klucz in klucze:
        if klucz != 'Tytul':
            print('Podaj {0}:'.format(klucz))
            dane = input()
            if dane.isdigit():
                dane =int(dane)
            ksiazka.dodaj(klucz, dane)

    lista_ksiazek.append(ksiazka)
    
def czy_ksiazka(lista_ksiazek, tytul):
    for ksiazka in lista_ksiazek:
        if tytul == ksiazka.pobierz('Tytul'):
            return True
    return False

def usun_ksiazke(lista_ksiazek):
    print('Podaj nazwe ksiazki ktora chcesz usunac')
    tytul = input()
    if not czy_ksiazka(lista_ksiazek, tytul):
        print('Ksiazka o tytule ', tytul, ' nie znajduje sie w zbiorze!')
    else:
        for ksiazka in lista_ksiazek:
            if tytul == ksiazka.pobierz('Tytul'):
                lista_ksiazek.remove(ksiazka)
                print('Poprawnie usunieto')
                break

def najtansza(lista_ksiazek):
    indeks = 0
    najtansza = lista_ksiazek[0].pobierz('Cena')
    for i in range(1, len(lista_ksiazek)):
        if lista_ksiazek[i].pobierz('Cena') < najtansza:
            najtansza = lista_ksiazek[i].pobierz('Cena')
            indeks = i
    return indeks

def wyswietl(lista_ksiazek, klucze):
    i = 0
    for ksiazka in lista_ksiazek:
        print('Ksiazka numer ', i)
        ksiazka.wyswietl()
        print(' ')
        i += 1

def sortuj_liste(lista_ksiazek, klucze):
    print('Wzgledem jakiego kryterium posorotwac liste?')
    for i in range(len(klucze)):
        print('{0}. {1}'.format(i, klucze[i]))
    wybor = int(input())
    lista_ksiazek = sortuj(lista_ksiazek, klucze[wybor])

def sortuj(lista, wybor):
    if len(lista) <= 1:
        return lista
    else:
        lewy, prawy = podziel(lista)
        return polacz(sortuj(lewy, wybor), sortuj(prawy, wybor), wybor)

def podziel(lista):
    return lista[:int(len(lista)/2)], lista[int(len(lista)/2):]

def polacz(lewy, prawy, wybor):
    if len(lewy) == 0:
        return prawy
    elif len(prawy) == 0:
        return lewy
    
    indeks_l = indeks_p = 0
    polaczone = []
    dlugosc = len(lewy) + len(prawy)
    while len(polaczone) < dlugosc:
        if lewy[indeks_l].pobierz(wybor) <= prawy[indeks_p].pobierz(wybor):
            polaczone.append(lewy[indeks_l])
            indeks_l += 1
        else:
            polaczone.append(prawy[indeks_p])
            indeks_p += 1
            
        if indeks_p == len(prawy):
            polaczone += lewy[indeks_l:]
            break
        elif indeks_l == len(lewy):
            polaczone += prawy[indeks_p:]
            break
        
    return polaczone

def menu(lista_ksiazek, klucze):
    while 1:
        print('1.Dodaj ksiazke do biblioteki')
        print('2. Wyswietl ksiazki')
        print('3. Posortuj ksiazki wedlug klucza')
        print('4. Usun ksiazke')
        print('5. Pokaz najtansza')
        wybor = int(input())
        if wybor == 1:
            dodaj_ksiazke(lista_ksiazek, klucze)
        if wybor == 2:
            wyswietl(lista_ksiazek, klucze)
        if wybor == 3:
            sortuj_liste(lista_ksiazek, klucze)
        if wybor == 4:
            usun_ksiazke(lista_ksiazek)
        if wybor == 5:
            lista_ksiazek[najtansza(lista_ksiazek)].wyswietl()

lista_ksiazek = []
klucze = ['Tytul', 'Autor', 'Rok Wydania', 'Cena', 'Liczba Stron']
menu(lista_ksiazek, klucze)
