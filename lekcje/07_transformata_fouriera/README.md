## Transformata Fouriera

Transformata Fouriera jest narzedziem matematycznym sluzacym do analizy sygnalow, zwlaszcza w kontekscie ich czestotliwosci. Umozliwia przechodzenie miedzy przestrzenia czasowa (lub przestrzenna) a przestrzenia czestotliwosci.

Podstawowe Pojecia:
- **Sygnal Czasowy**: Funkcja reprezentujaca amplitude sygnalu w zaleznosci od czasu.
- **Spektrum Czestotliwosci**: Reprezentacja sygnalu w dziedzinie czestotliwosci, pokazujaca skladowe czestotliwosciowe sygnalu.
- **Faza i Amplituda**: Dwoch kluczowych komponentow analizy Fouriera, opisujacych skladowe sinusoidalne sygnalu.

Zastosowania:

1. **Analiza Spektralna Sygnalow**: Do analizowania skladowych czestotliwosciowych sygnalu.
2. **Procesy Filtracyjne**: W projektowaniu i implementacji filtrow cyfrowych.
3. **Komunikacja**: W systemach modulacji i demodulacji sygnalow.
4. **Przetwarzanie Obrazow**: W operacjach takich jak filtrowanie, kompresja itp.

## Transformata Fouriera (Continuous Time Fourier Transform - CTFT)

Matematycznie, Transformata Fouriera (dla sygnalow ciaglych) jest zdefiniowana jako:
$$
F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-j\omega t} dt
$$
gdzie:
- $ F(\omega) $ - transformata Fouriera
- $ f(t) $ - sygnal czasowy
- $ e^{-j\omega t} $ - jadro transformacji
- $ \omega $ - czestotliwosc katowa

## Dyskretna Transformata Fouriera (Discrete Fourier Transform - DFT)

Dla sygnalow dyskretnych, transformata jest zdefiniowana jako:
$$
X(k) = \sum_{n=0}^{N-1} x(n) e^{-j(2\pi/N)kn}
$$
gdzie:
- $ X(k) $ - wynik transformacji
- $ x(n) $ - probki sygnalu
- $ N $ - liczba probek
- $ k $ - indeks czestotliwosci

## Implementacja Dyskretnej Transformaty Fouriera (DFT) w Kodzie

Implementacja DFT w kodzie programistycznym zwykle wymaga zrozumienia podstawowych konceptow algebraicznych, w tym obslugi liczb zespolonych i operacji sumowania.

### Liczby Zespolone
W jezykach programowania, takich jak Python, liczby zespolone mozna przedstawiac i manipulowac przy uzyciu wbudowanych funkcji i typow danych. W Pythonie, liczby zespolone tworzy sie za pomoca skladni `a + bj`, gdzie `a` jest czescia rzeczywista, a `b` jest czescia urojona.

```python
z = 3 + 4j # Deklaracja liczby zespolonej
```

Operacje na Liczbach Zespolonych

- Dodawanie i Odejmowanie: Wykonuje sie tak jak dla liczb rzeczywistych.
- Mnozenie i Dzielenie: Wykorzystuje sie specyficzne wlasciwosci liczb zespolonych.
- Modul: Oblicza sie jako √(a² + b²).
- Sprzezenie: Zamienia sie znak czesci urojonej.

### Sumowanie

Sumowanie w kontekscie DFT zazwyczaj odnosi sie do sumowania elementow serii lub sekwencji. W wiekszosci jezykow programowania, sumowania mozna dokonac przy uzyciu petli lub funkcji wyzszego rzedu, takich jak reduce w Pythonie.

```python
# Przyklad sumowania za pomoca petli
sum_result = 0
for i in range(N):
    sum_result += some_sequence[i]
```

### Implementacja DFT

Implementacja DFT (Dyskretna Transformacja Fouriera) wymaga zastosowania rownania DFT, ktore zdefiniowane jest jako:

$$
X(k) = \sum_{n=0}^{N-1} x(n)e^{-j\left(\frac{2\pi}{N}\right)kn}
$$

Gdzie:
- $X(k)$ - wartosc DFT w punkcie $k$
- $x(n)$ - wartosci probek sygnalu w czasie
- $N$ - liczba probek sygnalu
- $j$ - jednostka urojona (rownowazna z $i$ w matematyce)
- $e$ - podstawa logarytmu naturalnego (okolo 2.71828)

Implementacja moze wygladac nastepujaco:

```python
import numpy as np

def DFT(x):
    N = len(x)
    X = [sum(x[n] * np.exp(-2j * np.pi * k * n / N) for n in range(N)) for k in range(N)]
    return X
```

W powyzszym kodzie:

- $x$: jest wejsciowa sekwencja liczb zespolonych.
- $N$: jest liczba probek w x.
- $X$: jest wynikowa sekwencja liczb zespolonych, reprezentujaca transformacje DFT.

Aby przetestowac implementacje, mozna utworzyc prosty zestaw danych i zastosowac funkcje DFT, a nastepnie porownac wynik z wynikiem zwroconym przez wbudowana funkcje, taka jak numpy.fft.fft.

```python
# Testowanie funkcji DFT
x = [1, 2, 3, 4]
X = DFT(x)
print(X)

# Porownanie z funkcja numpy
X_np = np.fft.fft(x)
print(X_np)
```

## Szybka Transformacja Fouriera (FFT)

FFT, czyli Szybka Transformacja Fouriera, jest algorytmem umozliwiajacym szybsze obliczenie DFT (Dyskretna Transformacja Fouriera). Osiaga to przez podzial problemu DFT na mniejsze, latwiejsze do rozwiazania problemy, a nastepnie kombinuje ich rozwiazania.

### Algorytm Cooley-Tukey

Jest to najpopularniejsza metoda obliczania FFT. Podstawowa idea tej metody to rekurencyjny podzial transformacji DFT na mniejsze fragmenty. Istnieja dwie glowne warianty tej metody:

1. **Decimation in Time (DIT)**: Podzial wejsciowej sekwencji na parzyste i nieparzyste elementy.
2. **Decimation in Frequency (DIF)**: Podzial wyjsciowej sekwencji na mniejsze czesci.

### Implementacja w Pythonie

Ponizej znajdziesz przykladowa implementacje algorytmu Cooley-Tukey:

```python
import numpy as np

def FFT(x):
    N = len(x)
    if N <= 1: 
        return x
    
    # Podzial na parzyste i nieparzyste indeksy
    even = FFT(x[0::2])
    odd = FFT(x[1::2])
    
    # Kombinacja
    T= [np.exp(-2j*np.pi*k/N)*odd[k] for k in range(N//2)]
    return [even[k] + T[k] for k in range(N//2)] + \
           [even[k] - T[k] for k in range(N//2)]

# Testowanie implementacji
x = [1, 2, 3, 4]
X_fft = FFT(x)
print(X_fft)
```

### Zlozonosc Obliczeniowa

FFT znaczaco zredukowala zlozonosc obliczeniowa z \(O(N^2)\) dla DFT do \(O(N\log N)\) dla FFT, co sprawia, ze jest to znacznie bardziej wydajne rozwiazanie dla duzych danych.
