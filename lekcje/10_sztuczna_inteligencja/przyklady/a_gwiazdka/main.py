import heapq


class Punkt:
    def __init__(self, x, y):
        """Inicjalizuje punkt o wspolrzednych (x, y)."""
        self.x = x
        self.y = y

    def __eq__(self, other):
        """Porownuje czy dwa punkty sa rowne."""
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        """Definiuje porownanie dla punktow w kontekscie kolejki priorytetowej."""
        return False

    def __repr__(self):
        """Zwraca reprezentacje punktu jako string."""
        return f"Punkt({self.x}, {self.y})"


def heurystyka(a, b):
    """Oblicza heurystyke kosztu od punktu a do b."""
    return abs(a.x - b.x) + abs(a.y - b.y)


def a_star(labirynt, start, koniec):
    """Znajduje najkrotsza sciezke w labiryncie od punktu start do punktu koniec uzywajac algorytmu A*."""
    kolejka_priorytetowa = []
    heapq.heappush(kolejka_priorytetowa, (0, start))
    sciezki = {start: []}
    koszty = {start: 0}

    while kolejka_priorytetowa:
        obecny_koszt, obecny_punkt = heapq.heappop(kolejka_priorytetowa)

        if obecny_punkt == koniec:
            return sciezki[koniec]

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = obecny_punkt.x + dx, obecny_punkt.y + dy
            nastepny_punkt = Punkt(x, y)

            if (
                0 <= x < len(labirynt)
                and 0 <= y < len(labirynt[0])
                and labirynt[x][y] != "#"
            ):
                nowy_koszt = obecny_koszt + 1

                if nastepny_punkt not in koszty or nowy_koszt < koszty[nastepny_punkt]:
                    koszty[nastepny_punkt] = nowy_koszt
                    priorytet = nowy_koszt + heurystyka(koniec, nastepny_punkt)
                    heapq.heappush(kolejka_priorytetowa, (priorytet, nastepny_punkt))
                    sciezki[nastepny_punkt] = sciezki[obecny_punkt] + [obecny_punkt]

    return None


def wypisz_labirynt(labirynt, sciezka):
    """Wypisuje labirynt z zaznaczona sciezka."""
    for x, wiersz in enumerate(labirynt):
        for y, znak in enumerate(wiersz):
            if Punkt(x, y) in sciezka:
                print("X", end="")
            else:
                print(znak, end="")
        print()


labirynt = [
    "##########",
    "#S#......#",
    "#.#.####.#",
    "#.#.#..#.#",
    "#...#.##.#",
    "#.###....#",
    "#.#######E",
    "#.........",
    "##########",
]

labirynt = [list(wiersz) for wiersz in labirynt]
start = Punkt(1, 1)
koniec = Punkt(6, 9)
sciezka = a_star(labirynt, start, koniec)

if sciezka is not None:
    wypisz_labirynt(labirynt, sciezka)
else:
    print("Brak sciezki.")
