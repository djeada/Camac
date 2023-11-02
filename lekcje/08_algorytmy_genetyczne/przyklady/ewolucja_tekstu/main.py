import random
import matplotlib.pyplot as plt


def losowy_znak():
    losowa_liczba = random.randint(0, 2)
    if losowa_liczba == 0:
        return chr(random.randint(65, 90))
    elif losowa_liczba == 1:
        return chr(random.randint(97, 122))
    return " "


def losowy_ciag(dlugosc):
    return "".join(losowy_znak() for _ in range(dlugosc))


class DNA:
    def __init__(self, n):
        self.geny = list(losowy_ciag(n))
        self.dopasowanie = 0

    def oblicz_dopasowanie(self, cel):
        wynik = sum(g == c for g, c in zip(self.geny, cel))
        self.dopasowanie = wynik / len(cel)

    def krzyzowanie(self, partner):
        potomek = DNA(len(self.geny))
        punkt_podzialu = random.randint(0, len(self.geny) - 1)

        potomek.geny = self.geny[:punkt_podzialu] + partner.geny[punkt_podzialu:]
        return potomek

    def mutacja(self, wspolczynnik_mutacji):
        self.geny = [
            losowy_znak() if random.random() < wspolczynnik_mutacji else gen
            for gen in self.geny
        ]


def srednie_dopasowanie(populacja):
    return sum(x.dopasowanie for x in populacja) / len(populacja)


def najlepiej_dopasowany(populacja):
    return max(populacja, key=lambda x: x.dopasowanie)


def nowa_generacja(populacja, najlepsi, sredniacy, cel, wspolczynnik_mutacji):
    pulka_rodzicielska = [
        osobnik for osobnik in populacja for _ in range(int(osobnik.dopasowanie * 100))
    ]
    for i in range(len(populacja)):
        rodzicA = random.choice(pulka_rodzicielska)
        rodzicB = random.choice(pulka_rodzicielska)
        dziecko = rodzicA.krzyzowanie(rodzicB)
        dziecko.mutacja(wspolczynnik_mutacji)
        dziecko.oblicz_dopasowanie(cel)
        populacja[i] = dziecko

    najlepsi.append(najlepiej_dopasowany(populacja).dopasowanie)
    sredniacy.append(srednie_dopasowanie(populacja))


def wizualizuj(generacje, najlepsi, sredniacy):
    plt.plot(najlepsi, "g-", label="Najlepiej dopasowany")
    plt.plot(sredniacy, "b-", label="Srednie dopasowanie")
    plt.xlabel("Generacja")
    plt.ylabel("Dopasowanie")
    plt.title("Dopasowanie w kolejnych generacjach")
    plt.legend()
    plt.show()


wspolczynnik_mutacji = 0.01
rozmiar_populacji = 150
cel = "lezy jerzy na wiezy"

populacja = [DNA(len(cel)) for _ in range(rozmiar_populacji)]
for osobnik in populacja:
    osobnik.oblicz_dopasowanie(cel)

generacja = 0
najlepsi = []
sredniacy = []

while "".join(najlepiej_dopasowany(populacja).geny) != cel:
    nowa_generacja(populacja, najlepsi, sredniacy, cel, wspolczynnik_mutacji)
    print("Obecna generacja:", generacja)
    print("".join(najlepiej_dopasowany(populacja).geny))
    generacja += 1

wizualizuj(generacja, najlepsi, sredniacy)
