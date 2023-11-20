# Sztuczna Inteligencja

Sztuczna Inteligencja (AI) jest dziedzina informatyki, ktora skupia sie na tworzeniu systemow zdolnych do inteligentnego zachowania, symulujac procesy myslowe charakterystyczne dla ludzi. Proces ten jest realizowany za pomoca zaawansowanych algorytmow, ktore umozliwiaja maszynom uczenie sie i samodzielne podejmowanie decyzji. AI jest na przecieciu wielu dziedzin, takich jak matematyka, informatyka, psychologia i neurobiologia.

## Fundamenty Algorytmiczne

### Algorytmy Uczenia Maszynowego 
Pozwalaja komputerom uczyc sie z danych, bez wyraznego programowania. Kluczowe techniki to:

- **Regresja**: matematyczna analiza relacji miedzy zmiennymi.
- **Klasyfikacja**: grupowanie danych do roznych kategorii na podstawie cech.
- **Klasteryzacja**: segregacja danych w grupy na podstawie ich podobienstwa.
  
### Glebokie Uczenie (Deep Learning) 
Poddziedzina uczenia maszynowego, ktora wykorzystuje wielowarstwowe sieci neuronowe do analizowania zlozonych, wielowymiarowych danych. Wykorzystuje matematyczne funkcje aktywacji i techniki optymalizacji.

### Optymalizacja i Przeszukiwanie
Algorytmy sluzace do znajdowania najlepszych rozwiazan w przestrzeni rozwiazan, wykorzystujace techniki, takie jak:

- **Przeszukiwanie Heurystyczne**: takie jak algorytmy genetyczne i symulowane wyzarzanie.
- **Programowanie Liniowe i Nielineowe**: matematyczne podejscia do optymalizacji zmiennych.

### Reprezentacja Wiedzy 
Metody i techniki reprezentowania wiedzy w systemach AI, wlaczajac:

- **Sieci Semantyczne**: struktury danych reprezentujace relacje miedzy obiektami.
- **Ramy (Frames)**: struktury danych uzywane do reprezentowania stereotypowych sytuacji.
- **Logiki Opisowe**: formalne jezyki sluzace do opisania wiedzy o swiecie.

## Zastosowania

- **Rozpoznawanie Obrazow**: Wykorzystuje techniki uczenia maszynowego i glebokiego uczenia do analizy obrazow i wideo, stosujac algorytmy takie jak konwolucyjne sieci neuronowe (CNN).

- **Przetwarzanie Jezyka Naturalnego (NLP)**: Zajmuje sie opracowywaniem algorytmow umozliwiajacych maszynom zrozumienie i generowanie jezyka ludzkiego. Techniki te moga obejmowac analize skladniowa, semantyczna i sentimentu.

- **Systemy Eksperckie**: Aplikacje AI, ktore symuluja decyzje i zalecenia eksperta w danej dziedzinie, korzystajac z algorytmow opartych na logice rozmytej i sieciach bayesowskich.

## Algorytm Minimax

Minimax jest znaczacym algorytmem uzywanym w teorii gier, szczegolnie w kontekscie gier turowych typu zero-jedynkowego (zero-sum games), w ktorych jeden gracz dazy do zminimalizowania swojej potencjalnej straty, podczas gdy drugi stara sie zmaksymalizowac swoje potencjalne zyski. Teoretycznie, mozna go przedstawic w kontekscie funkcji kosztu oraz uzyc matematycznego aparatu analizy funkcji do optymalizacji algorytmu.

### Mechanizm Dzialania

#### 1. Drzewo Gry
Algorytm analizuje wszystkie mozliwe sciezki (ruchy i odpowiedzi) w strukturze drzewa gry, gdzie kazdy wierzcholek reprezentuje stan gry, a krawedzie reprezentuja mozliwe ruchy.

#### 2. Ocenianie Ruchow
Kazdy potencjalny ruch jest oceniany na podstawie funkcji heurystycznej, ktora moze byc zdefiniowana matematycznie w celu kwantyfikacji jakosci ruchu.

#### 3. Maksymalizacja i Minimalizacja
Proces decyzyjny opiera sie na teorii gier, gdzie gracze alternatywnie staraja sie maksymalizowac lub zminimalizowac wartosc funkcji oceny. Matematycznie, to mozna przedstawic jako problem optymalizacji:

$$
\text{Maksymalizacja:} & \quad \max(f(x))$$

$$
\text{Minimalizacja:} & \quad \min(f(x))
$$

gdzie $f(x)$ jest funkcja oceny.

#### 4. Przycinanie
Za pomoca techniki przycinania alpha-beta, proces przeszukiwania jest optymalizowany poprzez eliminacje sciezek, ktore sa mniej prawdopodobne do prowadzenia do optymalnego rozwiazania.

### Przyklad Uzycia

W kontekscie gier takich jak szachy czy warcaby, algorytm Minimax jest uzywany do prognozowania mozliwych ruchow przeciwnika i reagowania na nie najlepszym mozliwym ruchem, maksymalizujac szanse na zwyciestwo. Jest to realizowane przez rozwiniecie drzewa gry i analize matematyczna funkcji oceniajacej.

### Zastosowania

- **Gry Planszowe**: Szachy, warcaby, tic-tac-toe, gdzie algorytm moze byc wykorzystany do automatycznego planowania strategii.
- **Sztuczna Inteligencja**: W scenariuszach, gdzie AI musi dokonywac decyzji opartych na prognozowanych reakcjach przeciwnika lub otoczenia.
- **Analiza Finansowa**: W kontekscie analizy ryzyka inwestycyjnego, dla minimalizacji potencjalnych strat.

### Wady i Zalety

Zalety:
- Pozwala na wypracowanie optymalnej strategii w kontekscie gier turowych.
- Potrafi znalezc globalnie najlepsze rozwiazanie, przy odpowiednim zastosowaniu funkcji heurystycznej.

Wady:
- Obliczeniowo zlozony, zwlaszcza dla gier z duza przestrzenia stanow, co mozna matematycznie opisac jako problem o wysokim stopniu zlozonosci.

### Strategie Optymalizacji

- **Przycinanie Alpha-Beta**: Pozwala na ograniczenie przestrzeni przeszukiwan przez eliminacje mniej obiecujacych ruchow, co mozna modelowac jako problem optymalizacji z ograniczeniami.

- **Memoizacja**: Zapamietywanie juz ocenionych stanow, aby uniknac ich wielokrotnego przeszukiwania, co przeklada sie na zredukowanie czasu obliczen. Matematycznie, to przypomina zastosowanie dynamicznego programowania do optymalizacji algorytmu.

## Algorytm A* (A Star)

Algorytm A* to wysoko optymalizowany algorytm uzywany do szukania najkrotszej sciezki w grafach, zastosowany szeroko w dziedzinach sztucznej inteligencji, robotyki i grach komputerowych. Jego dzialanie opiera sie na pewnych konceptach matematycznych, ktore mozna zanalizowac z perspektywy optymalizacji i teorii grafow.

### Podstawowe Koncepty

#### 1. **Heurystyka**
Funkcja heurystyczna, zapisywana jako $ h(n) $, jest funkcja szacujaca minimalny koszt dojscia od punktu $ n $ do celu. Dobor skutecznej funkcji heurystycznej jest kluczowy dla szybkosci i skutecznosci algorytmu.

#### 2. **Funkcja Kosztu**
Funkcja kosztu, oznaczana jako $ g(n) $, przedstawia rzeczywisty koszt przejscia od punktu startowego do punktu $ n $. Moze byc zdefiniowana jako suma wag krawedzi na sciezce.

#### 3. **Funkcja Oceny**
Funkcja oceny, $ f(n) $, jest kluczowym elementem algorytmu A*, definiowanym jako:

$$
f(n) = g(n) + h(n)
$$

gdzie:
- $ f(n) $ - funkcja oceny dla wezla $ n $
- $ g(n) $ - koszt przejscia od startu do wezla $ n $
- $ h(n) $ - szacowany koszt przejscia od wezla $ n $ do celu

### Krok po Kroku Dzialania Algorytmu

1. **Inicjalizacja** 
   Inicjalizuj liste otwarta, ktora zawiera tylko wezel startowy z $ g(n) = 0 $ i $ h(n) $ obliczonej z funkcji heurystycznej.
   
2. **Rozszerzanie Wezla**
   Wybierz wezel z najnizsza wartoscia $ f(n) $ z listy otwartej, a nastepnie usun go z tej listy i dodaj do listy zamknietej.
   
3. **Generowanie Nastepcow**
   Dla kazdego z sasiadow wybranego wezla, oblicz $ g(n) $ i $ h(n) $, a nastepnie oblicz $ f(n) $. Aktualizuj liste otwarta z nowymi wartosciami funkcji oceny.
   
4. **Sprawdzenie Warunku Stopu**
   Jesli osiagnieto cel, odtworz sciezke, przechodzac wstecz przez rodzicow wezlow. W przeciwnym razie powtorz kroki od 2 do 4.

### Zastosowania w Sztucznej Inteligencji

1. **Gry** 
   Implementacja AI w grach w celu znalezienia najlepszej strategii lub sciezki nawigacyjnej.
   
2. **Robotyka**
   Planowanie tras robotow, z minimalizacja czasu przejazdu i unikaniem przeszkod.
   
3. **Rozpoznawanie Wzorcow**
   Wykorzystywany w problemach rozpoznawania wzorcow, gdzie trzeba znalezc optymalna sekwencje decyzji minimalizujaca koszt.
   
### Optymalizacja i Wydajnosc

1. **Wybor Heurystyki**
   Wybor skutecznej funkcji heurystycznej jest kluczowy dla szybkosci i skutecznosci algorytmu.
   
2. **Optymalnosc**
   Algorytm A* gwarantuje optymalnosc rozwiazania, jezeli uzywana funkcja heurystyczna jest nieprzesadzona (admissible) i monotoniczna (consistent). Moze to byc formalnie wyrazone jako:

   $$
   h(n) \leq c(n, n') + h(n')
   $$
   
   gdzie:
   - $ c(n, n') $ - koszt przejscia od wezla $ n $ do $ n' $
   - $ h(n) $, $ h(n') $ - wartosci heurystyki dla $ n $ i $ n' $ odpowiednio
   
Dzieki spelnieniu tych warunkow, algorytm A* jest zarowno kompletny, jak i optymalny, gwarantujac znalezienie najkrotszej sciezki w grafie.
