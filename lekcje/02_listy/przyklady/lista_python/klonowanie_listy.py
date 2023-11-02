import random


class Wezel:
    def __init__(self, dane=None):
        self.dane = dane
        self.nastepny = None
        self.losowy = None


class Lista:
    def __init__(self):
        self.glowa = Wezel()
        self.polaczenia = {}

    def dodaj(self, dane):
        nowy_wezel = Wezel(dane)
        if not self.glowa.dane:
            self.glowa = nowy_wezel
        else:
            licznik = self.glowa
            while licznik.nastepny:
                licznik = licznik.nastepny
            licznik.nastepny = nowy_wezel

    def ustaw_losowe(self):
        licznik1 = licznik2 = self.glowa
        while licznik1 and licznik1.nastepny:
            if licznik1 != licznik2 and random.randint(1, 7) % 3 == 0 and licznik2:
                licznik1.losowy = licznik2
                self.dodaj_do_slownika(licznik1.dane, licznik2.dane)
                licznik1 = licznik1.nastepny
            licznik2 = licznik2.nastepny or self.glowa
        licznik1.losowy = self.glowa

    def wyswietl(self):
        if not self.glowa.dane:
            print("Lista jest pusta")
        else:
            licznik = self.glowa
            while licznik:
                print(licznik.dane, end=" -> ")
                licznik = licznik.nastepny
            print("None")

    def wyswietl_losowe(self):
        if not self.glowa.dane:
            print("Lista jest pusta")
        else:
            self.wyswietl_slownik(self.polaczenia)

    def dlugosc(self):
        dlugosc = 0
        licznik = self.glowa
        while licznik:
            dlugosc += 1
            licznik = licznik.nastepny
        return dlugosc

    def klonuj(self):
        nowa_lista = Lista()
        licznik = self.glowa
        while licznik:
            nowa_lista.dodaj(licznik.dane)
            if licznik.losowy:
                nowa_lista.dodaj_do_slownika(licznik.dane, licznik.losowy.dane)
            licznik = licznik.nastepny
        return nowa_lista

    def dodaj_do_slownika(self, klucz, wartosc):
        self.polaczenia.setdefault(klucz, []).append(wartosc)

    def wyswietl_slownik(self, slownik):
        for klucz, wartosci in slownik.items():
            print(f"{klucz}: {', '.join(map(str, wartosci))}")


def main():
    lista = Lista()
    for i in range(10):
        lista.dodaj(i)
    lista.ustaw_losowe()
    print("Lista1: ")
    lista.wyswietl()
    print("Polaczenia losowe: ")
    lista.wyswietl_losowe()
    print()

    lista2 = lista.klonuj()
    print("Lista2: ")
    lista2.wyswietl()
    print("Polaczenia losowe: ")
    lista2.wyswietl_losowe()


if __name__ == "__main__":
    main()
