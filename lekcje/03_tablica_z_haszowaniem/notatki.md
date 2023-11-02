# Tablice z Haszowaniem

Tablice z haszowaniem, znane rowniez jako mapy haszowe, sa strukturami danych, ktore umozliwiaja przechowywanie i wyszukiwanie elementow w efektywny sposob. Kluczowym elementem tablicy haszowej jest funkcja haszujaca, ktora mapuje klucze na indeksy w tablicy.

Podstawowe Komponenty:

1. **Funkcja Haszujaca**: Funkcja, ktora przypisuje kazdemu kluczowi unikalny indeks w tablicy.

2. **Tablica**: Przestrzen przechowujaca wartosci. Kazda pozycja w tablicy jest zwiazana z unikalnym indeksem generowanym przez funkcje haszujaca.

3. **Pary Klucz-Wartosc**: Elementy przechowywane w tablicy z haszowaniem, skladajace sie z unikalnego klucza i zwiazanej z nim wartosci.

## Operacje

1. **Dodawanie (Wstawianie)**: Dodawanie nowych par klucz-wartosc do tablicy.

2. **Usuniecie**: Usuwanie pary klucz-wartosc z tablicy.

3. **Wyszukiwanie**: Wyszukiwanie wartosci na podstawie klucza.

4. **Aktualizacja**: Aktualizacja wartosci zwiazanej z konkretnym kluczem.

## Zlozonosc Czasowa

- **Wstawianie**: O(1) - w przypadku idealnym; O(n) - w najgorszym przypadku.
- **Usuniecie**: O(1) - w przypadku idealnym; O(n) - w najgorszym przypadku.
- **Wyszukiwanie**: O(1) - w przypadku idealnym; O(n) - w najgorszym przypadku.

## Przyklady Zastosowan

- Bazy danych
- Cachowanie
- Zbiory i mapy w roznych jezykach programowania

## Funkcje Haszujace

Funkcje haszujace sa funkcjami, ktore mapuja dane wejsciowe (lub "klucze") na numeryczny indeks w tablicy haszowej. Idealna funkcja haszujaca powinna minimalizowac ilosc kolizji, byc szybka do obliczen i rownomiernie rozkladac klucze po calej tablicy.

### Wlasciwosci Dobrej Funkcji Haszujacej

1. **Szybka do Obliczen**: Funkcja haszujaca powinna byc w stanie szybko przetworzyc dane wejsciowe.
2. **Rownomierny Rozklad**: Funkcja powinna rozkladac klucze rownomiernie po calej tablicy, minimalizujac prawdopodobienstwo kolizji.
3. **Deterministyczna**: Dla tego samego wejscia, funkcja zawsze powinna zwracac te sama wartosc haszowa.
4. **Unikalnosc**: Funkcja powinna starac sie generowac rozne hashe dla roznych danych wejsciowych.

### Przyklady Funkcji Haszujacych

1. Funkcja Dzielaca (Division-remainder method)

```python
def hash_division(key, table_size):
    return key % table_size
```

2. Funkcja Mnozaca (Multiplicative hash function)

```python
def hash_multiplicative(key, table_size):
    A = (sqrt(5) - 1) / 2  # stala 0 < A < 1
    return int(table_size * ((key * A) % 1))
```

3. Funkcja SHA-256 (przyklad funkcji kryptograficznej)

```python
import hashlib

def hash_sha256(key):
    return hashlib.sha256(key.encode()).hexdigest()
```

## Strategie Rozwiazania Kolizji

W tablicach z haszowaniem kolizje sa nieuniknione i moga znaczaco wplynac na wydajnosc operacji. Oto rozbudowane informacje o podstawowych strategiach rozwiazania kolizji:

### Metoda Lancuchow
W tej metodzie elementy o tym samym indeksie haszowym sa przechowywane jako lista polaczona. Istnieje kilka wariantow tej strategii:

- **Lista Pojedynczo Polaczona**: Kazdy element listy przechowuje dane i wskaznik do nastepnego elementu.

- **Lista Podwojnie Polaczona**: Kazdy element listy przechowuje dane oraz wskazniki do nastepnego i poprzedniego elementu, co ulatwia nawigacje w obie strony.

- **Drzewo**: Dla duzych ilosci danych, lista polaczona moze byc zastapiona przez drzewo, aby poprawic szybkosc wyszukiwania.

### Otwarte Adresowanie
Otwarte adresowanie to strategia, w ktorej wszyscy elementy sa przechowywane bezposrednio w tablicy. Jesli miejsce docelowe jest zajete, tablica probuje znalezc kolejne wolne miejsce zgodnie z zdefiniowana strategia:

- **Adresowanie Liniowe**: W przypadku kolizji, tablica szuka kolejnego wolnego miejsca, przesuwajac sie o staly krok.

- **Adresowanie Kwadratowe**: Podczas tej metody, kolizje sa rozwiazywane przez poszukiwanie nowego miejsca z krokami zwiekszanymi kwadratowo.

- **Podwojne Haszowanie**: Ta metoda uzywa drugiej funkcji haszujacej do okreslenia kroku dla poszukiwan miejsca w przypadku kolizji.

### Probkowanie (Robin Hood Hashing)
Jest to wariant otwartego adresowania, gdzie przy dodawaniu nowego elementu, jesli obecny element ma mniejsza liczbe prob niz nowy element, to nowy element "zabiera" miejsce obecnego elementu, a obecny jest umieszczany w nowym miejscu.

### Haszowanie Dynamiczne
Pozwala na dynamiczna zmiane rozmiaru tablicy, aby utrzymac wydajnosc, nawet gdy liczba przechowywanych elementow jest duzy i znaczaco rozni sie od poczatkowo zaalokowanej pojemnosci tablicy.
