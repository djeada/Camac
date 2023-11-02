import numpy as np
import matplotlib.pyplot as plt


def FFT(x):
    """
    Funkcja oblicza Szybka Transformacje Fouriera (FFT) sygnalu x.
    :param x: sygnal wejsciowy
    :return: transformata Fouriera sygnalu
    """
    N = len(x)
    if N <= 1:
        return x

    # Podzial sygnalu na czesc parzysta i nieparzysta
    even = FFT(x[0::2])
    odd = FFT(x[1::2])

    # Inicjalizacja tablicy wynikowej
    T = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]

    # Algorytm Cooley-Tukey FFT
    # X[k] = E[k] + e^(-2πik/N) * O[k] dla k < N/2
    # X[k] = E[k - N/2] - e^(-2πi(k - N/2)/N) * O[k - N/2] dla k >= N/2
    return [even[k] + T[k] for k in range(N // 2)] + [
        even[k] - T[k] for k in range(N // 2)
    ]


# Przykladowy sygnal: suma dwoch sygnalow sinusoidalnych o czestotliwosciach 7 Hz i 13 Hz
t = np.linspace(0, 1, 1024)  # 1024 punkty od 0 do 1
y = np.sin(2 * np.pi * 7 * t) + np.sin(
    2 * np.pi * 13 * t
)  # y(t) = sin(2π7t) + sin(2π13t)

# Obliczenie FFT
Y = FFT(y)

# Wizualizacja
plt.figure(figsize=(12, 6))

# Wykres sygnalu wejsciowego
plt.subplot(2, 1, 1)
plt.plot(t, y)
plt.title("Sygnal wejsciowy")
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda")

# Wykres modulu FFT
plt.subplot(2, 1, 2)
plt.plot(np.abs(Y)[: len(Y) // 2])
plt.title("FFT - Modul")
plt.xlabel("Czestotliwosc [Hz]")
plt.ylabel("Amplituda")

plt.tight_layout()
plt.show()
