# Algorytmy Genetyczne

Definicja:
- **Algorytmy genetyczne (AG)**: To heurystyczne metody optymalizacji i wyszukiwania inspirowane procesem naturalnej selekcji.
- **Populacja**: Zestaw potencjalnych rozwiazan w danej generacji.
- **Chromosom**: Jedno rozwiazanie problemu reprezentowane jako ciag binarny lub inna struktura danych.

Wady i zalety:
- **Zalety**: Mozliwosc znalezienia rozwiazania w zlozonych przestrzeniach, elastycznosc.
- **Wady**: Nie gwarantuje znalezienia optymalnego rozwiazania, mozliwosc wpadniecia w lokalne minima, wymaga doboru odpowiednich parametrow.

Zastosowania:
- Optymalizacja funkcji.
- Rozwiazywanie problemow NP-trudnych, jak problem komiwojazera czy problem plecakowy.
- Automatyczne generowanie algorytmow (programowanie genetyczne).

## Problem Optymalizacji

Optymalizacja to proces szukania najlepszego rozwiazania sposrod wszystkich mozliwych rozwiazan w danym kontekscie. Problem optymalizacji moze dotyczyc roznych dziedzin, w tym inzynierii, ekonomii, informatyki, itp. Najlepsze rozwiazanie jest zazwyczaj definiowane przez funkcje celu, ktora kwantyfikuje jakosc rozwiazania: im nizsza (lub wyzsza) wartosc funkcji celu, tym lepsze rozwiazanie.

### Przystosowanie w Algorytmach Genetycznych

W kontekscie algorytmow genetycznych, funkcja celu jest czesto nazywana funkcja przystosowania. Przystosowanie mierzy, jak "dobrze" dany osobnik (rozwiazanie) spelnia cel optymalizacji. Wyzsza wartosc przystosowania wskazuje na lepsze rozwiazanie

### Algorytmy Genetyczne jako Metoda Optymalizacji

Algorytmy genetyczne sa heurystycznymi metodami optymalizacji, ktore nasladuja proces naturalnej selekcji. Poprzez iteracyjny proces selekcji, krzyzowania (rekombinacji) i mutacji, algorytmy genetyczne stara sie stopniowo poprawiac jakosc rozwiazan w populacji, dazac do znalezienia najlepszego mozliwego rozwiazania.

### Etapy Optymalizacji w Algorytmach Genetycznych

- **Inicjalizacja Populacji**: Tworzenie poczatkowej populacji, ktora zazwyczaj sklada sie z losowo wygenerowanych rozwiazan.
- **Selekcja**: Wybor osobnikow do krzyzowania na podstawie ich przystosowania.
- **Krzyzowanie (Crossover)**: Tworzenie nowych osobnikow poprzez polaczenie genow rodzicow.
- **Mutacja**: Losowe modyfikacje genow w osobnikach, wprowadzajac nowe cechy w populacji i zapobiegajac stagnacji.
- **Ewaluacja**: Ocena nowych osobnikow i ich dodanie do populacji.
- **Selekcja Nowej Generacji**: Wybor osobnikow do nastepnej generacji, zazwyczaj na podstawie ich przystosowania.

### Kryteria zakonczenia

- Osiagniecie okreslonej liczby generacji.
- Znalezienie optymalnego rozwiazania.
- Stagnacja (brak poprawy przystosowania w kilku kolejnych generacjach).

## Operatory genetyczne

1. **Selekcja ruletki**

   Selekcja ruletki jest metoda wyboru osobnikow do reprodukcji oparta na ich funkcji przystosowania. W tej metodzie, szansa na wybranie danego osobnika jest proporcjonalna do jego przystosowania.

   **Przyklad**:

   Zalozmy, ze mamy trzy osobniki z wartosciami przystosowania 0.2, 0.5 i 0.3. W metodzie ruletki, pierwszy osobnik ma 20% szans na wybor, drugi - 50%, a trzeci - 30%.

2. **Selekcja turniejowa**

   W selekcji turniejowej, losowy zestaw osobnikow jest wybierany, a nastepnie osobnik z najlepszym przystosowaniem w tym zestawie jest wybrany do reprodukcji.

   **Przyklad**:

   Wybralismy losowo trzy osobniki na turniej. Z nich, osobnik z najwyzszym przystosowaniem zostanie wybrany do nastepnej generacji.

3. **Krzyzowanie jednopunktowe**

   Krzyzowanie jednopunktowe to proces, w ktorym dwa chromosomy rodzicow sa dzielone w jednym, losowo wybranym punkcie, a nastepnie czesci te sa wymieniane, aby utworzyc dwa nowe chromosomy.

   **Przyklad**:

   Rodzic 1: 11001 | 0110
   
   Rodzic 2: 10101 | 1001

   *Dzieci*:

       11001 | 1001
       10101 | 0110

4. **Krzyzowanie wielopunktowe**

   Krzyzowanie wielopunktowe jest rozszerzeniem krzyzowania jednopunktowego, gdzie geny sa wymieniane w kilku, losowo wybranych punktach.

   **Przyklad**:

   Rodzic 1: 110 | 01 | 0110
   
   Rodzic 2: 101 | 01 | 1001

   *Dzieci*:

       110 | 01 | 1001
       101 | 01 | 0110

5. **Mutacja bitowa**

   Mutacja bitowa polega na losowej zmianie wartosci jednego lub wiekszej liczby bitow w chromosomie.

   **Przyklad**:

   Przed mutacja: 110010110
   
   Po mutacji (zmiana trzeciego bitu): 111010110


## Implementacja w kodzie

### Inicjalizacja

Na poczatek, potrzebujesz stworzyc poczatkowa populacje, ktora zazwyczaj sklada sie z losowo generowanych chromosomow. Inicjalizacja jest waznym krokiem, ktory pomaga w ustawieniu podstawowej przestrzeni poszukiwan dla algorytmu genetycznego.

Przyklad:

```python
import random

def initialize_population(population_size, chromosome_length):
    population = []
    for _ in range(population_size):
        chromosome = "".join(random.choice(['0', '1']) for _ in range(chromosome_length))
        population.append(chromosome)
    return population
```

### Selekcja

Selekcja jest procesem wyboru odpowiednich chromosomow, ktore beda uczestniczyc w krzyzowaniu i mutacji. Mozesz zaimplementowac rozne strategie selekcji, jak selekcja ruletki czy turniejowa, ktore zostaly omowione wczesniej.

Przyklad:

```python
def selection(population, fitness_values):
    selected = random.choices(population, weights=fitness_values, k=len(population))
    return selected
```

### Krzyzowanie i mutacja

Po selekcji, nastepnym krokiem jest zaimplementowanie operatorow krzyzowania (jak krzyzowanie jedno- czy wielopunktowe) oraz mutacji (jak mutacja bitowa), ktore sluza do generowania nowej populacji.

Przyklad:

```python
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1)-1)
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
    return offspring1, offspring2

def mutation(chromosome, mutation_rate):
    chromosome = list(chromosome)
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = '1' if chromosome[i] == '0' else '0'
    return "".join(chromosome)
```

### Ocena

Ocena jest procesem, w ktorym obliczasz funkcje przystosowania dla kazdego chromosomu w populacji, aby zrozumiec, jak "dobrze" chromosom rozwiazuje problem.

Przyklad:

```python
def evaluate(population, fitness_function):
    fitness_values = [fitness_function(ind) for ind in population]
    return fitness_values

def sample_fitness_function(chromosome):
    return sum(int(gene) for gene in chromosome)
```

W tej czesci, zdefiniujesz funkcje przystosowania, ktora oceni, jak dobrze dany chromosom rozwiazuje problem, ktory probujesz rozwiazac za pomoca algorytmu genetycznego.

## Przykladowe implementacje i narzedzia

- Biblioteki jezyka Python takie jak DEAP, GAft, Pyevolve.
- Algorytmy genetyczne w innych jezykach programowania: Java (Jenetics), C++ (EO, GAlib).
