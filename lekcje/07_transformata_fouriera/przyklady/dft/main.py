import numpy as np
import matplotlib.pyplot as plt


def DFT(x):
    """
    Funkcja oblicza Dyskretna Transformacje Fouriera (DFT) sygnalu x.
    :param x: sygnal wejsciowy
    :return: transformata Fouriera sygnalu
    """
    N = len(x)  # Liczba probek sygnalu
    X = np.zeros(N, dtype=complex)  # Inicjalizacja wynikowej tablicy kompleksowej

    # Implementacja DFT:
    # X[k] = Σ(x[n] * e^(-j2πkn/N)) od n=0 do N-1
    # gdzie: j to jednostka urojona, Σ oznacza sumowanie
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    return X


# Przykladowy sygnal: suma dwoch sygnalow sinusoidalnych o czestotliwosciach 7 Hz i 13 Hz
t = np.linspace(0, 1, 500)  # 500 punktow od 0 do 1
y = np.sin(2 * np.pi * 7 * t) + np.sin(
    2 * np.pi * 13 * t
)  # y(t) = sin(2π7t) + sin(2π13t)

# Obliczenie DFT
Y = DFT(y)

# Wizualizacja
plt.figure(figsize=(12, 6))

# Wykres sygnalu wejsciowego
plt.subplot(2, 1, 1)
plt.plot(t, y)
plt.title("Sygnal wejsciowy")
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda")

# Wykres modulu DFT
# Z uwagi na symetrie, pokazujemy tylko polowe wynikow
plt.subplot(2, 1, 2)
plt.plot(np.abs(Y[: len(Y) // 2]))
plt.title("DFT - Modul")
plt.xlabel("Czestotliwosc [Hz]")
plt.ylabel("Amplituda")

plt.tight_layout()
plt.show()
