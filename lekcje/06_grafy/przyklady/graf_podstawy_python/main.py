class Wierzcholek:
    def __init__(self, id):
        self.id = id
        self.nastepny = None


class Graf:
    def __init__(self, liczbaWierzcholkow):
        self.liczbaWierzcholkow = liczbaWierzcholkow
        self.listaSasiedztwa = [None] * liczbaWierzcholkow

    def dodajKrawedz(self, src, dest):
        nowy = Wierzcholek(dest)
        nowy.nastepny = self.listaSasiedztwa[src]
        self.listaSasiedztwa[src] = nowy

        nowy = Wierzcholek(src)
        nowy.nastepny = self.listaSasiedztwa[dest]
        self.listaSasiedztwa[dest] = nowy

    def usunKrawedz(self, src, dest):
        temp = self.listaSasiedztwa[src]
        poprzedni = None
        while temp is not None and temp.id != dest:
            poprzedni = temp
            temp = temp.nastepny

        if poprzedni is None:
            self.listaSasiedztwa[src] = temp.nastepny
        else:
            poprzedni.nastepny = temp.nastepny

        temp = self.listaSasiedztwa[dest]
        poprzedni = None
        while temp is not None and temp.id != src:
            poprzedni = temp
            temp = temp.nastepny

        if poprzedni is None:
            self.listaSasiedztwa[dest] = temp.nastepny
        else:
            poprzedni.nastepny = temp.nastepny

    def usunWierzcholek(self, wierzcholek):
        for i in range(self.liczbaWierzcholkow):
            if i == wierzcholek or self.listaSasiedztwa[i] is None:
                continue
            self.usunKrawedz(i, wierzcholek)
        self.listaSasiedztwa[wierzcholek] = None

    def wyswietlGraf(self):
        for i in range(self.liczbaWierzcholkow):
            temp = self.listaSasiedztwa[i]
            print(f"Wierzcholek {i}: ", end="")
            while temp:
                print(temp.id, end=" ")
                temp = temp.nastepny
            print()


# Przyklad uzycia
graf = Graf(5)
graf.dodajKrawedz(0, 1)
graf.dodajKrawedz(0, 4)
graf.dodajKrawedz(1, 2)
graf.dodajKrawedz(1, 3)
graf.dodajKrawedz(1, 4)
graf.dodajKrawedz(2, 3)
graf.dodajKrawedz(3, 4)

print("Graf przed usunieciem krawedzi i wierzcholkow:")
graf.wyswietlGraf()

graf.usunKrawedz(1, 4)
graf.usunWierzcholek(2)

print("\nGraf po usunieciu krawedzi 1-4 i wierzcholka 2:")
graf.wyswietlGraf()
