import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    # Sigmoid: f(x) = 1 / (1 + exp(-x))
    return 1 / (1 + np.exp(-x))


def pochodna_sigmoid(x):
    # Pochodna sigmoid: f'(x) = x * (1 - x)
    return x * (1 - x)


def trenuj_siec_neuronowa(X, y, liczba_epok=10000, wspolczynnik_uczenia=0.1):
    np.random.seed(1)
    wagi = np.random.rand(X.shape[1], 1)
    biasy = np.random.rand(1)
    bledy = []

    for epoka in range(liczba_epok):
        # Propagacja wprzod
        warstwa_wejsciowa = X
        wyjscia = sigmoid(np.dot(warstwa_wejsciowa, wagi) + biasy)

        # Obliczanie bledu
        # Blad: e = y - f(x)
        blad = y - wyjscia
        bledy.append(np.mean(np.abs(blad)))

        # Propagacja wsteczna
        # Korekta wag: Δw = η * (e * f'(x)) * x.T
        korekty = wspolczynnik_uczenia * np.dot(
            warstwa_wejsciowa.T, blad * pochodna_sigmoid(wyjscia)
        )
        korekty_biasow = wspolczynnik_uczenia * np.sum(blad * pochodna_sigmoid(wyjscia))

        # Aktualizacja wag i biasow
        wagi += korekty
        biasy += korekty_biasow

    return wyjscia, wagi, biasy, bledy


# Dane wejsciowe
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Etykiety dla roznych bramek logicznych
y_and = np.array([[0], [0], [0], [1]])
y_or = np.array([[0], [1], [1], [1]])
y_xor = np.array([[0], [1], [1], [0]])

# Trenowanie sieci neuronowej
wyjscia_and, _, _, bledy_and = trenuj_siec_neuronowa(X, y_and)
wyjscia_or, _, _, bledy_or = trenuj_siec_neuronowa(X, y_or)
wyjscia_xor, _, _, bledy_xor = trenuj_siec_neuronowa(X, y_xor)

# Wizualizacja wynikow
def rysuj_wyniki(X, y, wyjscia, tytul):
    plt.scatter(X[:, 0], X[:, 1], c=y[:, 0], marker="o", label="Dane treningowe")
    plt.scatter(
        X[:, 0], X[:, 1], c=wyjscia[:, 0], marker="x", label="Dopasowanie sieci"
    )
    plt.title(tytul)
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.legend()
    plt.show()


rysuj_wyniki(X, y_and, wyjscia_and, "Bramka AND")
rysuj_wyniki(X, y_or, wyjscia_or, "Bramka OR")
rysuj_wyniki(X, y_xor, wyjscia_xor, "Bramka XOR")
