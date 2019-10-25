import random

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
                
d = DrzewoBinarne()
for i in range(100):
    d.dodaj(random.randint(0,100))
d.dodaj(5)
d.wyswietl()
print('Znaleziono')
for i in range(100):
    w = d.wyszukaj(random.randint(0,100))
    if w:
        print(w.dane)
    else:
        print('Brak')
