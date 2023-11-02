class ElementHaszujacy:
    def __init__(self, klucz, wartosc):
        self.klucz = klucz
        self.wartosc = wartosc


class TablicaHaszujaca:
    def __init__(self, rozmiar=100):
        self.rozmiar = rozmiar
        self.tablica = [[] for _ in range(self.rozmiar)]

    def _haszuj(self, klucz):
        """Funkcja haszujaca oblicza indeks w tablicy dla danego klucza."""
        return hash(klucz) % self.rozmiar

    def dodaj(self, klucz, wartosc):
        """Dodaje pare klucz-wartosc do tablicy."""
        indeks = self._haszuj(klucz)
        for element in self.tablica[indeks]:
            if element.klucz == klucz:
                element.wartosc = wartosc
                return
        self.tablica[indeks].append(ElementHaszujacy(klucz, wartosc))

    def pobierz(self, klucz):
        """Zwraca wartosc dla danego klucza."""
        indeks = self._haszuj(klucz)
        for element in self.tablica[indeks]:
            if element.klucz == klucz:
                return element.wartosc
        raise KeyError("Klucz nie istnieje w tablicy haszujacej.")

    def usun(self, klucz):
        """Usuwa pare klucz-wartosc z tablicy."""
        indeks = self._haszuj(klucz)
        for i, element in enumerate(self.tablica[indeks]):
            if element.klucz == klucz:
                del self.tablica[indeks][i]
                return
        raise KeyError("Klucz nie istnieje w tablicy haszujacej.")

    def __str__(self):
        """Reprezentacja tekstowa tablicy haszujacej."""
        elementy = []
        for lancuch in self.tablica:
            for element in lancuch:
                elementy.append(f"{element.klucz}: {element.wartosc}")
        return "{ " + ", ".join(elementy) + " }"


# Przyklad uzycia
if __name__ == "__main__":
    th = TablicaHaszujaca()

    # Dodajemy elementy
    th.dodaj("imie", "Jan")
    th.dodaj("nazwisko", "Kowalski")
    th.dodaj("wiek", 30)

    # Wyswietlamy tablice
    print("Tablica haszujaca:", th)

    # Odczytujemy wartosci
    print("Imie:", th.pobierz("imie"))
    print("Nazwisko:", th.pobierz("nazwisko"))
    print("Wiek:", th.pobierz("wiek"))

    # Usuwamy element
    th.usun("wiek")

    # Proba odzyskania usunietego elementu powinna zglosic blad KeyError
    try:
        print("Wiek:", th.pobierz("wiek"))
    except KeyError as e:
        print(e)
