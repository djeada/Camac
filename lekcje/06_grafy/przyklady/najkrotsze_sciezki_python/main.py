from collections import defaultdict, deque


class Graf:
    def __init__(self, liczba_wierzcholkow):
        self.liczba_wierzcholkow = liczba_wierzcholkow
        self.lista_sasiedztwa = defaultdict(list)

    def dodaj_krawedz(self, src, dest):
        self.lista_sasiedztwa[src].append(dest)

    def BFS(self, start, cel):
        odwiedzone = [False] * self.liczba_wierzcholkow
        kolejka = deque()
        kolejka.append((start, [start]))

        while kolejka:
            (wierzcholek, sciezka) = kolejka.popleft()
            if wierzcholek == cel:
                print(f"Szukanie sciezki BFS z {start} do {cel}:")
                print(" -> ".join(map(str, sciezka)))
                return sciezka
            if not odwiedzone[wierzcholek]:
                odwiedzone[wierzcholek] = True
                for sasiad in self.lista_sasiedztwa[wierzcholek]:
                    if not odwiedzone[sasiad]:
                        kolejka.append((sasiad, sciezka + [sasiad]))
        print("Brak sciezki")
        return None

    def DFS(self, start, cel):
        odwiedzone = [False] * self.liczba_wierzcholkow

        def DFSRekurencyjnie(v, sciezka):
            odwiedzone[v] = True
            sciezka.append(v)
            if v == cel:
                print(f"Szukanie sciezki DFS z {start} do {cel}:")
                print(" -> ".join(map(str, sciezka)))
                return True
            for sasiad in self.lista_sasiedztwa[v]:
                if not odwiedzone[sasiad]:
                    if DFSRekurencyjnie(sasiad, sciezka):
                        return True
            sciezka.pop()
            return False

        if not DFSRekurencyjnie(start, []):
            print("Brak sciezki")


# Przyklad uzycia
graf = Graf(6)
graf.dodaj_krawedz(0, 1)
graf.dodaj_krawedz(0, 2)
graf.dodaj_krawedz(1, 3)
graf.dodaj_krawedz(1, 4)
graf.dodaj_krawedz(2, 5)
graf.dodaj_krawedz(3, 4)
graf.dodaj_krawedz(4, 5)

graf.BFS(0, 4)
graf.DFS(0, 4)
