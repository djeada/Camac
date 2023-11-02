# Klasa Wezel reprezentujaca pojedynczy element listy
class Wezel:
    def __init__(self, wartosc):
        self.wartosc = wartosc
        self.nastepny = None


# Klasa ListaPolaczona implementujaca liste jednokierunkowa
class ListaPolaczona:
    def __init__(self):
        self.glowa = None

    # Metoda dodajaca nowy wezel na koncu listy
    def dodaj_na_koniec(self, wartosc):
        nowy_wezel = Wezel(wartosc)
        if self.glowa is None:
            self.glowa = nowy_wezel
            return
        ostatni = self.glowa
        while ostatni.nastepny:
            ostatni = ostatni.nastepny
        ostatni.nastepny = nowy_wezel

    # Metoda wypisujaca wszystkie elementy listy
    def wypisz_liste(self):
        aktualny = self.glowa
        while aktualny:
            print(aktualny.wartosc, end=" -> ")
            aktualny = aktualny.nastepny
        print("None")

    # Metoda usuwajaca wszystkie elementy listy
    def usun_liste(self):
        self.glowa = None


# Funkcja main demonstrujaca uzycie listy
def main():
    lista = ListaPolaczona()
    lista.dodaj_na_koniec(1)
    lista.dodaj_na_koniec(2)
    lista.dodaj_na_koniec(3)

    print("Lista polaczona: ")
    lista.wypisz_liste()

    lista.usun_liste()


# Uruchomienie funkcji main
if __name__ == "__main__":
    main()
