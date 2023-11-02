import time
import random
import matplotlib.pyplot as plt

# Definiowanie algorytmow sortowania
def sortowanie_babelkowe(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


def sortowanie_przez_wybieranie(lista):
    n = len(lista)
    for i in range(n):
        min_indeks = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_indeks]:
                min_indeks = j
        lista[i], lista[min_indeks] = lista[min_indeks], lista[i]


def sortowanie_przez_wstawianie(lista):
    for i in range(1, len(lista)):
        klucz = lista[i]
        j = i - 1
        while j >= 0 and klucz < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = klucz


def sortowanie_szybkie(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[len(lista) // 2]
        left = [x for x in lista if x < pivot]
        middle = [x for x in lista if x == pivot]
        right = [x for x in lista if x > pivot]
        return sortowanie_szybkie(left) + middle + sortowanie_szybkie(right)


# Funkcja do mierzenia czasu wykonania algorytmow
def mierz_czas(algorytm, lista):
    start = time.time()
    algorytm(lista)
    end = time.time()
    return end - start


# Generowanie danych do wykresu
rozmiary_list = list(range(1000, 10001, 1000))
czas_babelkowe = []
czas_wybieranie = []
czas_wstawianie = []
czas_szybkie = []

for n in rozmiary_list:
    lista = [random.randint(0, 10000) for _ in range(n)]

    czas_babelkowe.append(mierz_czas(sortowanie_babelkowe, lista.copy()))
    czas_wybieranie.append(mierz_czas(sortowanie_przez_wybieranie, lista.copy()))
    czas_wstawianie.append(mierz_czas(sortowanie_przez_wstawianie, lista.copy()))
    czas_szybkie.append(mierz_czas(sortowanie_szybkie, lista.copy()))

# Rysowanie wykresu
plt.figure()
plt.plot(rozmiary_list, czas_babelkowe, label="Sortowanie Babelkowe")
plt.plot(rozmiary_list, czas_wybieranie, label="Sortowanie przez Wybieranie")
plt.plot(rozmiary_list, czas_wstawianie, label="Sortowanie przez Wstawianie")
plt.plot(rozmiary_list, czas_szybkie, label="Sortowanie Szybkie")
plt.xlabel("Rozmiar listy (n)")
plt.ylabel("Czas wykonania (s)")
plt.title("Zlozonosc czasowa algorytmow sortowania")
plt.legend()
plt.grid(True)
plt.show()
