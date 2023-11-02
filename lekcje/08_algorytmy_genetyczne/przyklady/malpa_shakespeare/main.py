import random
import time

# Fragment "Hamleta" Szekspira, ktory chcemy wygenerowac
docelowy_tekst = "byc albo nie byc"
dlugosc_tekstu = len(docelowy_tekst)

# Zbior liter, z ktorego malpa moze wybierac
litery = "abcdefghijklmnopqrstuvwxyzaeoslzzcnABCDEFGHIJKLMNOPQRSTUVWXYZAEOSLZZCN ,."


def losowa_litera():
    return random.choice(litery)


def generuj_tekst(n):
    return "".join(losowa_litera() for _ in range(n))


def ocena_tekstu(tekst):
    return sum(1 for a, b in zip(tekst, docelowy_tekst) if a == b)


def eksperyment_malpy():
    najlepszy_tekst = generuj_tekst(dlugosc_tekstu)
    najlepsza_ocena = ocena_tekstu(najlepszy_tekst)
    licznik_prob = 0

    print("Rozpoczynam eksperyment...")
    while najlepsza_ocena < dlugosc_tekstu:
        licznik_prob += 1
        nowy_tekst = generuj_tekst(dlugosc_tekstu)
        nowa_ocena = ocena_tekstu(nowy_tekst)

        if nowa_ocena > najlepsza_ocena:
            najlepsza_ocena = nowa_ocena
            najlepszy_tekst = nowy_tekst
            print(f"Proba {licznik_prob}: {najlepszy_tekst} | Ocena: {najlepsza_ocena}")

        if licznik_prob % 10000 == 0:
            print(f"Proba {licznik_prob}: {najlepszy_tekst} | Ocena: {najlepsza_ocena}")

        if najlepszy_tekst == docelowy_tekst:
            print(f"Znaleziono dokladny tekst po {licznik_prob} probach!")
            break

    return najlepszy_tekst


eksperyment_malpy()
