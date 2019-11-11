class Graf():
    def __init__(self):
        self.slownikSasiedztwa = dict()

    def dodajWierzcholek(self, wierzcholek):
        if wierzcholek in self.slownikSasiedztwa:
            print('Już dodany')
        else:
            self.slownikSasiedztwa[wierzcholek] = []

    def dodajKrawedz(self, start, koniec):
        if start in self.slownikSasiedztwa and koniec in self.slownikSasiedztwa:
            self.slownikSasiedztwa[start] += [koniec]
            
    def wypisz(self):
        for wierzcholek in self.slownikSasiedztwa:
            print(wierzcholek, ' : ', end='')
            for sasiedzi in self.slownikSasiedztwa[wierzcholek]:
                print(sasiedzi, ' , ', end='')
            print('')

    def znajdzSciezke(self, start, koniec):
        def znajdz(self, start, koniec, odwiedzone = set()):
            if start in self.slownikSasiedztwa and koniec in self.slownikSasiedztwa:
                if start == koniec:
                    return [koniec]
                for sasiad in self.slownikSasiedztwa[start]:
                    odwiedzone.add(sasiad)
                    sciezka = znajdz(self, sasiad, koniec, odwiedzone)
                    if sciezka:
                        return [sasiad] + sciezka
        if znajdz(self, start,koniec):
            return [start] + znajdz(self, start,koniec)[:-1]

    def znajdzWszystkieSciezki(self, start, koniec, sciezki = []):
        def znajdz(self, start, koniec, odwiedzone = set()):
            if start in self.slownikSasiedztwa and koniec in self.slownikSasiedztwa:
                if start == koniec:
                    return [koniec]
                for sasiad in self.slownikSasiedztwa[start]:
                    odwiedzone.add(sasiad)
                    sciezka = znajdz(self, sasiad, koniec, odwiedzone)
                    if sciezka:
                        return [sasiad] + sciezka

        for sasiad in self.slownikSasiedztwa[start]:
            if znajdz(self, sasiad, koniec):
                nowa = [start] + [sasiad] + znajdz(self, sasiad,koniec)[:-1]
                sciezki.append(nowa)
                #sciezki.append(self.znajdzWszystkieSciezki(sasiad, koniec, sciezki))
        return sciezki

    def najkrotszaSciezka(self, start, koniec):
        najkrotsza = self.znajdzWszystkieSciezki(start, koniec)[0]
        for x in self.znajdzWszystkieSciezki(start, koniec):
            if len(x) < len(najkrotsza):
                najkrotsza = x
        return najkrotsza

    def czyPetla(self,wierzcholek):
        for sasiad in self.slownikSasiedztwa[wierzcholek]:
            if sasiad == wierzcholek:
                return True
        return False

    def stopien(self, wierzcholek):
        if wierzcholek in self.slownikSasiedztwa:
            return len(self.slownikSasiedztwa[wierzcholek])

    def znajdzIzolowaneWierzcholki(self):
        izolowane = []
        for wierzcholek in self.slownikSasiedztwa:
            falga = 1
            for sasiad in self.slownikSasiedztwa[wierzcholek]:
                if sasiad != wierzcholek:
                    flaga = 0
            if flaga:
                izolowane.append(wierzcholek)
        return izolowane

    def czySpojny(self):
        if self.znajdzIzolowaneWierzcholki():
                return False
        return True
            
g = Graf()
g.dodajWierzcholek('A')
g.dodajWierzcholek('B')
g.dodajWierzcholek('C')
g.dodajWierzcholek('D')
g.dodajWierzcholek('E')
g.dodajWierzcholek('F')
g.dodajWierzcholek('G')
g.dodajWierzcholek('H')

g.dodajKrawedz('A', 'D')
g.dodajKrawedz('A', 'C')
g.dodajKrawedz('A', 'E')
g.dodajKrawedz('B', 'D')
g.dodajKrawedz('C', 'F')
g.dodajKrawedz('E', 'B')
g.dodajKrawedz('F', 'E')
g.dodajKrawedz('D', 'G')
g.dodajKrawedz('D', 'F')
g.dodajKrawedz('G', 'F')
g.dodajKrawedz('H', 'H')

g.wypisz()
print(g.znajdzWszystkieSciezki('A','F'))
print(g.najkrotszaSciezka('A','F'))
print('Czy graf jest spojny?', g.czySpojny())
print('Czy petla dla wierzcholka H', g.czyPetla('H'))
print('Czy petla dla wierzcholka A', g.czyPetla('A'))


