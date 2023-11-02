# Grafy

Definicja:
- **Graf**: Zbior wierzcholkow polaczonych krawedziami, gdzie wierzcholki reprezentuja obiekty, a krawedzie relacje miedzy nimi.
- **Wierzcholek (Vertex)**: Podstawowy element grafu, ktory moze reprezentowac roznego typu obiekty (np. osoby, miejsca, przedmioty).
- **Krawedz (Edge)**: Polaczenie miedzy dwoma wierzcholkami, ktore moze byc wazone (posiadac wartosc) lub niewazone, oraz skierowane lub nieskierowane. 

Rodzaje Grafow:
1. **Nieskierowany**: Krawedzie nie maja kierunku, co sugeruje wzajemne polaczenie miedzy wierzcholkami. Wykorzystywany w reprezentacji sieci nieskierowanych, takich jak sieci spolecznosciowe.
2. **Skierowany**: Krawedzie maja kierunek, reprezentujac relacje kierunkowe miedzy wierzcholkami. Przydatne w analizie sieci przeplywu, takich jak sieci transportowe czy sieci www.
3. **Wazony**: Krawedzie maja przypisane wagi, reprezentujace koszt lub odleglosc miedzy wierzcholkami. Wykorzystywane w problemach najkrotszej sciezki i innych zastosowaniach.
4. **Niewazony**: Krawedzie nie maja przypisanych wag, co sugeruje, ze wszystkie polaczenia maja rowna "sile" lub koszt.

Zastosowania:
- Analiza sieci spolecznosciowych.
- Algorytmy trasowania w sieciach komputerowych.
- Projektowanie tras w nawigacji GPS.
- Analiza struktur molekularnych w chemii.

## Reprezentacje Grafow

- **Macierz sasiedztwa**: Dwuwymiarowa tablica, gdzie wartosc `M[i][j]` reprezentuje krawedz miedzy wierzcholkami `i` i `j`. Jest to metoda dobra dla grafow gestych, lecz moze byc nieefektywna pod wzgledem pamieci dla grafow rzadkich.
- **Lista sasiedztwa**: Tablica list, gdzie lista na pozycji `i` zawiera wszystkie wierzcholki polaczone z wierzcholkiem `i`. Jest to bardziej kompaktowa i efektywna metoda reprezentacji grafow, szczegolnie gdy graf jest rzadki.
- **Lista Krawedzi**: Lista, ktora zawiera wszystkie krawedzie grafu, reprezentowane jako pary wierzcholkow. Jest to prosty sposob przedstawienia wszystkich polaczen w grafie.
- **Macierz Incydencji**: Dwuwymiarowa macierz, w ktorej wiersze reprezentuja wierzcholki, a kolumny reprezentuja krawedzie. Wartosc w komorce (i, j) wskazuje, czy wierzcholek i jest incydentny z krawedzia j.

## Operacje na Grafach

- **Dodawanie/Usuwanie Wierzcholka**: Proces dodawania lub usuwania wierzcholka wraz z jego krawedziami powiazanymi.
- **Dodawanie/Usuwanie Krawedzi**: Proces dodawania lub usuwania krawedzi miedzy dwoma wierzcholkami.
- **Przeszukiwanie Grafu**: Operacje przeszukiwania, takie jak BFS (przeszukiwanie wszerz) czy DFS (przeszukiwanie w glab), sa stosowane do eksploracji grafow i znajdowania sciezek miedzy wierzcholkami.

## Reprezentacje Grafow

Reprezentacja grafow w informatyce jest kluczowa do efektywnego ich przetwarzania. Oto kilka popularnych metod reprezentacji:

1. **Macierz sasiedztwa**:

   - **Opis**: Dwuwymiarowa tablica, gdzie wartosc `M[i][j]` reprezentuje krawedz miedzy wierzcholkami `i` i `j`. Jesli `M[i][j] = 1`, istnieje krawedz, jesli `M[i][j] = 0`, krawedz nie istnieje. W przypadku grafow wazonych, `M[i][j]` bedzie zawierala wage krawedzi.
   - **Zalety**:
     - Prosta implementacja i zrozumienie.
     - Szybkie sprawdzanie istnienia krawedzi.
   - **Wady**:
     - Zajmuje duzo miejsca dla grafow rzadkich (wiekszosc wartosci to zera).
     - Operacje takie jak dodawanie lub usuwanie krawedzi sa czasochlonne.

2. **Lista sasiedztwa**:

   - **Opis**: Tablica list, gdzie lista na pozycji `i` zawiera wszystkie wierzcholki polaczone z wierzcholkiem `i`. Jest to bardziej kompaktowa i efektywna metoda reprezentacji grafow rzadkich.
   - **Zalety**:
     - Zuzywa mniej miejsca dla grafow rzadkich.
     - Szybsze dodawanie i usuwanie krawedzi w porownaniu z macierza sasiedztwa.
   - **Wady**:
     - Sprawdzanie istnienia krawedzi moze byc wolniejsze niz w macierzy sasiedztwa.

3. **Lista krawedzi**:

   - **Opis**: Lista, ktora zawiera wszystkie krawedzie grafu, reprezentowane jako pary wierzcholkow (oraz ewentualnie wagi).
   - **Zalety**:
     - Prosta struktura danych do manipulowania krawedziami.
     - Idealna dla algorytmow, ktore iteruja po wszystkich krawedziach.
   - **Wady**:
     - Nieefektywna do szybkiego sprawdzania sasiedztwa miedzy wierzcholkami.

4. **Macierz incydencji**:

   - **Opis**: Dwuwymiarowa macierz, gdzie wiersze reprezentuja wierzcholki, a kolumny reprezentuja krawedzie. Wartosc w komorce (i, j) wskazuje, czy wierzcholek i jest incydentny z krawedzia j.
   - **Zalety**:
     - Dobrze nadaje sie do reprezentacji multigrafow (grafow z wielokrotnymi krawedziami miedzy wierzcholkami).
   - **Wady**:
     - Moze zuzywac duzo miejsca dla grafow z duza liczba krawedzi.

## Algorytmy Przeszukiwania

Algorytmy przeszukiwania sluza do przemierzania struktur grafu, odwiedzajac kazdy wierzcholek w okreslonym porzadku. Istnieja rozne strategie przeszukiwania, oto dwie najpopularniejsze:

### Przeszukiwanie wszerz (BFS)

- **Opis**: Przeszukiwanie rozpoczyna sie od wierzcholka startowego i eksploruje wszystkie sasiednie wierzcholki na danym poziomie przed przejsciem do nastepnego poziomu. Uzywa kolejki do sledzenia wierzcholkow do odwiedzenia.
- **Zastosowania**:
  - Znajdowanie najkrotszej sciezki w grafie nieskierowanym.
  - Algorytmy do wykrywania cykli.
- **Zlozonosc czasowa**: O(|V| + |E|), gdzie |V| to liczba wierzcholkow, a |E| liczba krawedzi.
- **Pseudokod**:

```
BFS(G, s):
    utworz kolejke Q
    dodaj s do Q i oznacz jako odwiedzony
    while Q nie jest pusta:
        v = Q.dequeue()
        dla kazdego sasiada u wierzcholka v:
            jesli u nie jest oznaczony jako odwiedzony:
                oznacz u jako odwiedzony
                dodaj u do Q
```

### Przeszukiwanie w glab (DFS)

- **Opis**: Przeszukiwanie rozpoczyna sie od wierzcholka startowego i przechodzi jak najdalej mozliwe wzdluz galezi, zanim wroci, aby zbadac inne galezie. Uzywa stosu (rekurencji) do sledzenia sciezki przeszukiwania.
- **Zastosowania**:
- Wyszukiwanie sciezek w grafie.
- Algorytmy do sprawdzania cyklicznosci.
- Topologiczne sortowanie grafow skierowanych acyklicznych (DAG).
- **Zlozonosc czasowa**: O(|V| + |E|), gdzie |V| to liczba wierzcholkow, a |E| liczba krawedzi.
- **Pseudokod**:

```
DFS(G, v):
    oznacz v jako odwiedzony
    dla kazdego sasiada u wierzcholka v:
        jesli u nie jest oznaczony jako odwiedzony:
            DFS(G, u)
```

## Algorytmy Najkrotszej Sciezki

Algorytmy najkrotszej sciezki sluza do znajdowania najkrotszej sciezki miedzy dwoma wierzcholkami w grafie wazonym. Oto trzy popularne algorytmy w tej kategorii:

1. Dijkstra:

    - **Opis**: Znajduje najkrotsza sciezke w grafie wazonym z jednym zrodlem. Nie moze jednak obslugiwac grafow z ujemnymi wagami krawedzi.
    - **Zastosowania**: Wyznaczanie najkrotszej trasy w systemach nawigacji GPS, sieci telekomunikacyjnych.
    - **Zlozonosc czasowa**: O(|V|^2) (lub O(|V| log |V| + |E| log |V|) z kopcem Fibonacciego).
    - **Pseudokod**:

```python
def dijkstra(graph, start):
    distance = {vertex: float('infinity') for vertex in graph}
    distance[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        if current_distance > distance[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance_through_v = current_distance + weight
            if distance_through_v < distance[neighbor]:
                distance[neighbor] = distance_through_v
                heapq.heappush(pq, (distance_through_v, neighbor))
    
    return distance
```

2. Bellman-Ford:

    - **Opis**: Rowniez sluzy do znajdowania najkrotszych sciezek, ale moze obslugiwac grafy z ujemnymi wagami. Jednak nie dziala poprawnie, gdy w grafie sa cykle o ujemnej wadze.
    - **Zastosowania**: W wykrywaniu cykli o ujemnej wadze, routingu IP.
    - **Zlozonosc czasowa**: O(|V||E|).
    - **Pseudokod**:

```python
def bellman_ford(graph, start):
    distance = {vertex: float('infinity') for vertex in graph}
    distance[start] = 0
    
    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex].items():
                if distance[vertex] + weight < distance[neighbor]:
                    distance[neighbor] = distance[vertex] + weight
    
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            if distance[vertex] + weight < distance[neighbor]:
                raise Exception("Graf zawiera cykl o ujemnej wadze")
    
    return distance
```

3. Floyd-Warshall:

    - **Opis**: Znajduje najkrotsze sciezki miedzy wszystkimi parami wierzcholkow, zarowno w grafach skierowanych, jak i nieskierowanych.
    - **Zastosowania**: Algorytm jest uzywany w problemach, ktore wymagaja znajdowania najkrotszych sciezek miedzy wszystkimi parami wierzcholkow.
    - **Zlozonosc czasowa**: O(|V|^3).
    - **Pseudokod**:

```python
def floyd_warshall(graph):
    num_vertices = len(graph)
    distance = [[float('infinity')] * num_vertices for _ in range(num_vertices)]
    
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i == j:
                distance[i][j] = 0
            elif (i, j) in graph:
                distance[i][j] = graph[(i, j)]
    
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
    return distance
```

## Cykle i Drzewa Rozpinajace

Cykle i drzewa rozpinajace sa waznymi konceptami w teorii grafow, ktore znajduja zastosowanie w wielu dziedzinach, takich jak sieci komputerowe, systemy trasportowe, itd. Ponizej przedstawiono szczegolowy opis obu koncepcji oraz popularnych algorytmow zwiazanych z drzewami rozpinajacymi.

Cykl:
- **Definicja**: Sekwencja wierzcholkow, w ktorej pierwszy i ostatni wierzcholek sa identyczne, a wszystkie krawedzie sa unikalne.
- **Zastosowania**: Wykrywanie obecnosci cykli jest istotne w roznych kontekstach, np. w wykrywaniu deadlockow w systemach operacyjnych czy w identyfikacji cykli w sieciach spolecznosciowych.
- **Przykladowe algorytmy**: Algorytmy przeszukiwania grafu, takie jak DFS, moga byc uzywane do identyfikowania cykli w grafie.

Drzewo Rozpinajace:
- **Definicja**: Podgraf, ktory zawiera wszystkie wierzcholki grafu, ale tylko niektore krawedzie, nie zawiera cykli i ma minimalna mozliwa sume wag krawedzi (w przypadku drzewa rozpinajacego minimalnego).
- **Zastosowania**: Drzewa rozpinajace znajduja szerokie zastosowanie w projektowaniu i optymalizacji sieci, takich jak sieci komputerowe, elektryczne czy transportowe.

Ponizej przedstawione sa dwa popularne algorytmy do znajdowania drzew rozpinajacych w grafach:

1. Algorytm Kruskala

    - **Opis**: Algorytm ten zaczyna od lasu (zestawu drzew), gdzie kazdy wierzcholek grafu stanowi osobne drzewo, a nastepnie laczy drzewa krok po kroku, wybierajac za kazdym razem krawedz o najmniejszej wadze, ktora nie tworzy cyklu.
    - **Zastosowania**: Idealny do znajdowania minimalnego drzewa rozpinajacego w duzych grafach.
    - **Zlozonosc czasowa**: O(E log E), gdzie E to liczba krawedzi w grafie.
    - **Pseudokod**:

```python
def kruskal(graph):
    tree = []
    edges = list(graph.edges())
    edges.sort(key=lambda x: x[2])  # Sort edges by weight
    
    union_find = UnionFind(len(graph.nodes()))
    for edge in edges:
        u, v, w = edge
        if union_find.find(u) != union_find.find(v):
            union_find.union(u, v)
            tree.append(edge)
    
    return tree
```

2. Algorytm Prima

   - **Opis**: Algorytm ten zaczyna od pojedynczego wierzcholka i sukcesywnie dodaje do drzewa rozpinajacego krawedz o najmniejszej wadze, ktora laczy wierzcholek w drzewie z wierzcholkiem poza drzewem.
   - **Zastosowania**: Szczegolnie efektywny dla grafow o gestych polaczeniach.
   - **Zlozonosc czasowa**: O(E log V), gdzie E to liczba krawedzi, a V to liczba wierzcholkow w grafie.
   - **Pseudokod**:

```python
def prim(graph):
    tree = []
    visited = [False] * len(graph.nodes())
    min_edge = [float('inf')] * len(graph.nodes())
    min_edge[0] = 0
    priority_queue = [(0, 0)]
    
    while priority_queue:
        w, u = heapq.heappop(priority_queue)
        if visited[u]:
            continue
        
        visited[u] = True
        tree.append((u, min_edge[u]))
        
        for v, w in graph[u]:
            if not visited[v] and w < min_edge[v]:
                min_edge[v] = w
                heapq.heappush(priority_queue, (w, v))
    
    return tree[1:]
```
