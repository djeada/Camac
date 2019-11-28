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

    def dfs(self, start):
        def _dfs(slownik, wierzcholek, odwiedzone=[]):
            if not odwiedzone or wierzcholek not in odwiedzone:
               odwiedzone.append(wierzcholek)
               for sasiad in slownik[wierzcholek]:
                   _dfs(slownik, sasiad, odwiedzone)
            return odwiedzone
        return _dfs(self.slownikSasiedztwa,start)

    def bfs(self, start):
        def _bfs(slownik, wierzcholek): 
            odwiedzone, kolejka = set(), [wierzcholek]
            odwiedzone.add(wierzcholek)
            while kolejka: 
                wierzcholek = kolejka.pop()
                for sasiad in slownik[wierzcholek]: 
                    if sasiad not in odwiedzone:
                        odwiedzone.add(sasiad) 
                        kolejka.append(sasiad)
            return odwiedzone  
        return _bfs(self.slownikSasiedztwa,start)
 
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

print(g.dfs('A'))
print(g.bfs('A'))

