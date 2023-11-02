import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns


def sigmoid(x):
    """
    Funkcja aktywacji sigmoidalnej.
    """
    return 1 / (1 + np.exp(-x))


def pochodna_sigmoid(x):
    """
    Pochodna funkcji aktywacji sigmoidalnej.
    """
    return x * (1 - x)


def trenuj_siec(X, y, liczba_epok=1000, wspolczynnik_uczenia=0.1):
    """
    Trenuje prosta siec neuronowa z jedna warstwa ukryta.
    """
    np.random.seed(1)
    wagi1 = np.random.rand(X.shape[1], 64)  # Inicjalizacja wag dla warstwy ukrytej
    bias1 = np.random.rand(1, 64)  # Inicjalizacja biasow dla warstwy ukrytej
    wagi2 = np.random.rand(64, 10)  # Inicjalizacja wag dla warstwy wyjsciowej
    bias2 = np.random.rand(1, 10)  # Inicjalizacja biasow dla warstwy wyjsciowej

    for epoka in range(liczba_epok):
        # Propagacja wprzod
        warstwa_wejsciowa = X
        warstwa_ukryta = sigmoid(np.dot(warstwa_wejsciowa, wagi1) + bias1)
        wyjscie = sigmoid(np.dot(warstwa_ukryta, wagi2) + bias2)

        # Obliczanie bledu
        blad = y - wyjscie

        # Propagacja wsteczna
        delta_wyjscie = blad * pochodna_sigmoid(wyjscie)
        blad_ukryty = delta_wyjscie.dot(wagi2.T)
        delta_ukryty = blad_ukryty * pochodna_sigmoid(warstwa_ukryta)

        # Aktualizacja wag i biasow
        wagi2 += warstwa_ukryta.T.dot(delta_wyjscie) * wspolczynnik_uczenia
        bias2 += np.sum(delta_wyjscie, axis=0, keepdims=True) * wspolczynnik_uczenia
        wagi1 += warstwa_wejsciowa.T.dot(delta_ukryty) * wspolczynnik_uczenia
        bias1 += np.sum(delta_ukryty, axis=0, keepdims=True) * wspolczynnik_uczenia

    return wagi1, bias1, wagi2, bias2


def prognozuj(X, wagi1, bias1, wagi2, bias2):
    """
    Przewiduje klasy dla podanego zestawu danych wejsciowych X, korzystajac z nauczonych wag i biasow.
    """
    warstwa_wejsciowa = X
    warstwa_ukryta = sigmoid(np.dot(warstwa_wejsciowa, wagi1) + bias1)
    wyjscie = sigmoid(np.dot(warstwa_ukryta, wagi2) + bias2)
    return np.argmax(wyjscie, axis=1)


def rysuj_macierz_konfuzji(y_prawdziwe, y_prognozowane):
    """
    Rysuje macierz konfuzji dla prawdziwych i przewidzianych etykiet klas.
    """
    cm = confusion_matrix(y_prawdziwe, y_prognozowane)
    plt.figure(figsize=(10, 7))
    sns.heatmap(cm, annot=True, fmt="d")
    plt.xlabel("Przewidywane")
    plt.ylabel("Prawdziwe")
    plt.title("Macierz konfuzji")
    plt.show()


# Wczytanie i normalizacja danych
cyfry = load_digits()
X = cyfry.data / 16.0  # Normalizacja wartosci pikseli do zakresu [0, 1]
y = np.eye(10)[cyfry.target]  # One-hot encoding etykiet

# Podzial na zbiory treningowe i testowe
X_treningowe, X_testowe, y_treningowe, y_testowe = train_test_split(
    X, y, test_size=0.2, random_state=1
)

# Trenowanie sieci neuronowej
wagi1, bias1, wagi2, bias2 = trenuj_siec(X_treningowe, y_treningowe)

# Prognozowanie
y_prognozowane = prognozuj(X_testowe, wagi1, bias1, wagi2, bias2)
y_testowe_klasy = np.argmax(y_testowe, axis=1)

# Ocena modelu
print("Raport klasyfikacji:\n", classification_report(y_testowe_klasy, y_prognozowane))

# Wizualizacja macierzy konfuzji
rysuj_macierz_konfuzji(y_testowe_klasy, y_prognozowane)
