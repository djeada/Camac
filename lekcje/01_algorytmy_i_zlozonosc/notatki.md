# Cel Nauki Algorytmow i Struktur Danych

## Po co to Komu Potrzebne?

1. Przygotowanie do technicznej rozmowy o prace
2. Dodanie projektow do swojego CV
3. Glebokie zrozumienie i nauczenie sie konkretnego zagadnienia

## Plan Studiowania

### Teoria

1. **Wskazniki** - Podstawy manipulacji adresami w pamieci
2. **Listy** - Struktury danych przechowujace elementy w sekwencyjnym porzadku
3. **Tablice z haszowaniem** - Struktury danych umozliwiajace szybkie wyszukiwanie elementow
4. **Drzewa** - Hierarchiczne struktury danych
5. **Grafy** - Reprezentacje relacji miedzy obiektami
6. **Programowanie dynamiczne** - Metoda rozwiazania problemow poprzez rozlozenie ich na mniejsze, prostsze podproblemy
7. **Algorytmy Genetyczne** - Proces optymalizacji inspirowany mechanizmami ewolucji biologicznej
8. **Perceptron** - Najprostszy model sieci neuronowej

### Analiza Algorytmow

#### Czas i Pamiec - Ograniczenia Fizyczne

W procesie projektowania i implementacji algorytmow, bardzo wazne jest zrozumienie, ze kazda operacja wykonana przez komputer zajmuje pewna ilosc czasu i pamieci. Oto bardziej szczegolowa rozbudowa tej sekcji:

1. **Zrozumienie ograniczen czasowych i pamieciowych w kontekscie realizacji algorytmow**
   
    1.1 **Ograniczenia czasowe**
        - **Czas procesora**: Jak szybko procesor moze wykonywac instrukcje.
        - **Czas dostepu do pamieci**: Czas potrzebny do zapisu i odczytu danych z pamieci.
        - **Zlozonosc czasowa**: Analiza, ktora pozwala oszacowac, jak dlugo algorytm bedzie dzialal w zaleznosci od wielkosci danych wejsciowych.
        - **Optymalizacje**: Techniki, ktore pozwalaja zmniejszyc czas wykonania algorytmu, np. memoizacja.
   
    1.2 **Ograniczenia pamieciowe**
        - **Pamiec RAM**: Ilosc dostepnej pamieci operacyjnej, ktora moze wplywac na to, jak duze dane mozemy przechowywac i przetwarzac.
        - **Zlozonosc przestrzenna**: Analiza, ktora pozwala ocenic, ile pamieci bedzie potrzebne do wykonania algorytmu w zaleznosci od wielkosci danych wejsciowych.
        - **Zarzadzanie pamiecia**: Techniki, ktore pozwalaja efektywniej korzystac z dostepnej pamieci, np. alokacja i dealokacja pamieci.
        - **Optymalizacje**: Metody pozwalajace na zmniejszenie uzycia pamieci, np. przez kompresje danych lub uzycie struktur danych o mniejszych wymaganiach pamieciowych.
   
2. **Wplyw ograniczen fizycznych na wydajnosc algorytmow**
    - **Wplyw na Wybor Algorytmow**: Jak ograniczenia moga wplywac na wybor konkretnego algorytmu lub struktury danych.
    - **Skalowalnosc**: Jak zbudowac algorytmy, ktore moga efektywnie dzialac na duza skale, pomimo ograniczen fizycznych.
    - **Testowanie i Tuning**: Jak przeprowadzac testy i dostosowywac algorytmy, majac na uwadze ograniczenia czasu i pamieci.
   
3. **Praktyczne Strategie**
    - **Analiza Wymagan**: Jak okreslic, jakie sa faktyczne wymagania dla danego problemu w kontekscie czasu i pamieci.
    - **Opracowywanie Rozwiazan**: Jak opracowac rozwiazania, ktore biora pod uwage ograniczenia fizyczne, ale tez spelniaja inne wazne kryteria, np. latwosc implementacji czy zrozumienie.
    - **Monitorowanie i Diagnostyka**: Jak monitorowac uzycie zasobow przez algorytmy i diagnozowac potencjalne problemy z wydajnoscia.

#### Notacje Analityczne

1. **Notacja Duzego O (O)** - Okreslenie gornego ograniczenia czasu wykonania
2. **Notacja Omega (Ω)** - Okreslenie dolnego ograniczenia czasu wykonania
3. **Notacja Theta (Θ)** - Okreslenie dokladnego (sredniego) czasu wykonania

### Zasady Notacji Duzego O

1. **Pojedyncza operacja** - O(1)
2. **Liniowa** - O(n)
3. **Logarytmiczna** - O(log n)
4. **Liniowo-logarytmiczna** - O(n log n)
5. **Kwadratowa** - O(n²)
6. **Wielomianowa** - O(n^k), gdzie k > 2
7. **Wykladnicza** - O(2^n)


### Przyklady 

#### Operacje na Stalych i Zmiennych

Kod:

```python
a = 5
b = 10
c = a + b
```

Zlozonosc:

- Czasowa: O(1)
- Pamieciowa: O(1)

#### Liniowy Przeszukiwanie Listy

Kod:

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Przykladowe uzycie:
arr = [1, 2, 3, 4, 5]
linear_search(arr, 3)
```

Zlozonosc:

- Czasowa: O(n)
- Pamieciowa: O(1)

#### Sortowanie przez Wstawianie

Kod:

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Przykladowe uzycie:
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
```

Zlozonosc:

- Czasowa: O(n²)
- Pamieciowa: O(1)

#### Rekurencyjne Obliczenie n-tego Wyrazu Ciagu Fibonacciego

Kod:

```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Przykladowe uzycie:
fibonacci(5)
```

Zlozonosc:

- Czasowa: O(2ⁿ)
- Pamieciowa: O(n)

## Problemy Klasyczne

### 1. P vs NP

Problem "P vs NP" jest jednym z najwazniejszych nierozwiazanych problemow w informatyce teoretycznej i matematyce. Glowna kwestia tego problemu to pytanie, czy kazdy problem, ktorego rozwiazanie mozna zweryfikowac w czasie wielomianowym (klasa problemow NP), mozna rowniez rozwiazac w czasie wielomianowym (klasa problemow P).

- **Klasa P**: Zbior problemow, ktore mozna rozwiazac szybko (w czasie wielomianowym) za pomoca deterministycznego algorytmu Turinga. 

- **Klasa NP**: Zbior problemow, dla ktorych rozwiazanie, jesli jest dane, mozna zweryfikowac szybko (rowniez w czasie wielomianowym) na deterministycznym algorytmie Turinga.

#### Podproblemy i Zagadnienia Powiazane
1. **NP-Complete**: Klasy problemow, ktore sa przynajmniej tak "trudne" jak najtrudniejsze problemy w NP. Jesli jakikolwiek problem NP-Complete moze byc rozwiazany w czasie wielomianowym, to kazdy problem w NP takze bedzie mogl byc rozwiazany w tym czasie.
   
2. **NP-Hard**: Klasy problemow, ktore sa co najmniej tak "trudne" jak najtrudniejsze problemy w NP, ale niekoniecznie naleza do klasy NP.

### 2. Milion Dolarow za Rozwiazanie

Inicjatywa Clay Mathematics Institute, ktora oferuje nagrode miliona dolarow za rozwiazanie siedmiu "Problematow Milenijnych", ktore sa uznawane za najwazniejsze otwarte problemy w matematyce i informatyce. Problem "P vs NP" jest jednym z tych problemow. Oto kilka szczegolow tej inicjatywy:

1. **Historia**: Program zostal uruchomiony w roku 2000 z zamiarem zainspirowania matematykow i informatykow do rozwiazania tych kluczowych problemow.

2. **Zasady**: Aby zdobyc nagrode, rozwiazanie musi byc opublikowane w renomowanym czasopismie matematycznym lub informatycznym i musi przejsc okres przegladu 2 lat, w czasie ktorego inne osoby w dziedzinie maja mozliwosc zrecenzowania rozwiazania.

3. **Pozostale Problemy Milenijne**: Oprocz "P vs NP", do problemow milenijnych naleza miedzy innymi Hipoteza Riemanna, Hipoteza Birch i Swinnerton-Dyer oraz Problem Naviera-Stokesa.

4. **Postepy**: Do tej pory, jeden z problemow milenijnych, Hipoteza Poincare, zostala udowodniona (choc nagroda zostala odmowiona).

5. **Wplyw na Nauke**: Program nagrod ma na celu nie tylko znalezienie rozwiazan tych problemow, ale takze zainspirowanie dalszych badan i innowacji w matematyce i informatyce.
