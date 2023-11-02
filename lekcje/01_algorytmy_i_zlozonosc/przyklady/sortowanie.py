import pygame
import random

# Inicjacja Pygame
pygame.init()

# Ustawienia okna
szerokosc_okna = 800
wysokosc_okna = 600
okno = pygame.display.set_mode((szerokosc_okna, wysokosc_okna))
pygame.display.set_caption("Wizualizacja Algorytmow Sortowania")

# Kolory
KOLOR_TLA = (0, 0, 0)
KOLOR_PROSTOKATA = (0, 128, 255)
KOLOR_ZAZNACZONY = (255, 0, 0)

# Lista wartosci do posortowania
liczba_prostokatow = 50
lista_wartosci = [random.randint(1, wysokosc_okna) for _ in range(liczba_prostokatow)]
szerokosc_prostokata = szerokosc_okna // liczba_prostokatow

# Algorytm sortowania babelkowego
def sortowanie_babelkowe(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            wyswietl(lista, j, j + 1)
            pygame.time.delay(50)


# Algorytm sortowania przez wybieranie
def sortowanie_przez_wybieranie(lista):
    n = len(lista)
    for i in range(n):
        min_indeks = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_indeks]:
                min_indeks = j
            wyswietl(lista, i, min_indeks)
            pygame.time.delay(50)
        lista[i], lista[min_indeks] = lista[min_indeks], lista[i]


# Algorytm sortowania przez wstawianie
def sortowanie_przez_wstawianie(lista):
    for i in range(1, len(lista)):
        klucz = lista[i]
        j = i - 1
        while j >= 0 and klucz < lista[j]:
            lista[j + 1] = lista[j]
            wyswietl(lista, j, i)
            pygame.time.delay(50)
            j -= 1
        lista[j + 1] = klucz


# Funkcja wyswietlajaca prostokaty i kolorujaca zaznaczone elementy
def wyswietl(lista, idx1=None, idx2=None):
    okno.fill(KOLOR_TLA)
    for i in range(len(lista)):
        kolor = KOLOR_PROSTOKATA
        if i == idx1 or i == idx2:
            kolor = KOLOR_ZAZNACZONY
        pygame.draw.rect(
            okno,
            kolor,
            (
                i * szerokosc_prostokata,
                wysokosc_okna - lista[i],
                szerokosc_prostokata,
                lista[i],
            ),
        )
    pygame.display.update()


def main():
    global lista_wartosci, liczba_prostokatow, szerokosc_prostokata

    # Pytanie o wielkosc tablicy
    liczba_prostokatow = int(
        input("Podaj liczbe prostokatow (elementow do posortowania): ")
    )

    # Pytanie o generowanie liczb lub wprowadzanie reczne
    metoda_generowania = (
        input("Czy chcesz wprowadzic liczby recznie? (tak/nie): ").strip().lower()
    )
    if metoda_generowania == "tak":
        lista_wartosci = [
            int(input(f"Podaj wartosc dla elementu {i+1}: "))
            for i in range(liczba_prostokatow)
        ]
    else:
        lista_wartosci = [
            random.randint(1, wysokosc_okna) for _ in range(liczba_prostokatow)
        ]

    # Pytanie o typ algorytmu
    algorytm = (
        input("Wybierz algorytm sortowania (babelkowe/wybieranie/wstawianie): ")
        .strip()
        .lower()
    )

    szerokosc_prostokata = szerokosc_okna // liczba_prostokatow

    # Petla glowna
    dziala = True
    while dziala:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dziala = False

        # Wywolanie funkcji sortujacej zgodnie z wyborem uzytkownika
        if algorytm == "babelkowe":
            sortowanie_babelkowe(lista_wartosci.copy())
        elif algorytm == "wybieranie":
            sortowanie_przez_wybieranie(lista_wartosci.copy())
        elif algorytm == "wstawianie":
            sortowanie_przez_wstawianie(lista_wartosci.copy())

        pygame.time.delay(500)
        dziala = False

    # Zamkniecie Pygame
    pygame.quit()


# Uruchomienie funkcji main
if __name__ == "__main__":
    main()
