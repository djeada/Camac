# Drzewa

Drzewa sa strukturami danych hierarchicznie zorganizowanymi, ktore maja zastosowania w wielu dziedzinach informatyki, wlaczajac w to reprezentacje danych w sposob strukturalny, zarzadzanie danymi oraz szereg innych algorytmow i procedur.

## Podstawowe Terminy

1. **Wezel (Node)**: Podstawowy element drzewa, zawierajacy dane oraz odnosniki do innych wezlow.
2. **Korzen (Root)**: Najwyzszy wezel w drzewie, z ktorego zaczyna sie wszystkie inne wezly.
3. **Lisc (Leaf)**: Wezel, ktory nie ma zadnych potomkow.
4. **Potomek (Child)**: Wezel, ktory jest bezposrednio polaczony z innym wezlem w dol.
5. **Rodzic (Parent)**: Wezel, ktory jest bezposrednio polaczony z innym wezlem w gore.
6. **Poddrzewo (Subtree)**: Drzewo zbudowane z dowolnego wezla i jego potomkow.
7. **Stopien (Degree)**: Liczba potomkow danego wezla.
8. **Glebokosc (Depth)**: Dlugosc najdluzszej sciezki od korzenia do danego wezla.
9. **Wysokosc (Height)**: Dlugosc najdluzszej sciezki od danego wezla do liscia.

## Typy Drzew

1. **Drzewa Binarne (Binary Tree)**: Drzewo, w ktorym kazdy wezel ma co najwyzej dwa dzieci (lewe i prawe).
2. **Drzewa BST (Binary Search Tree)**: Drzewo binarne, w ktorym lewe poddrzewo kazdego wezla zawiera wylacznie elementy o kluczach mniejszych niz wezel, a prawe poddrzewo zawiera elementy o kluczach wiekszych.
3. **Drzewa AVL**: Drzewo BST, ktore samo sie zbilansuje, aby utrzymac wysokosc minimalna.
4. **Drzewa B i B+**: Drzewa, ktore sa zoptymalizowane do dzialania z duza iloscia danych, czesto uzywane w bazach danych.
5. **Drzewa Trie**: Drzewo, w ktorym kazdy wezel reprezentuje jeden znak w slowie, uzywane do przechowywania slownikow. 

## Algorytmy

1. Przeszukiwanie (Traversal):
   - **Pre-order (KLR)**: Przeszukiwanie rozpoczyna sie od korzenia, a nastepnie przechodzi przez lewe i prawe poddrzewo. Typowe zastosowanie to klonowanie drzewa.
   - **In-order (LKR)**: Najpierw odwiedza lewe poddrzewo, potem korzen, a nastepnie prawe poddrzewo. Pozwala to na odwiedzenie wezlow w posortowanej kolejnosci.
   - **Post-order (LRK)**: Przeszukiwanie zaczyna sie od lewego poddrzewa, przechodzi przez prawe poddrzewo, a na koncu odwiedza korzen. Stosowane m.in. do usuwania drzewa.
   - **Poziomowe (Breadth-First)**: Przeszukiwanie odbywa sie poziomowo, odwiedzajac wszystkie wezly na danym poziomie zanim przejdzie do nastepnego poziomu.

2. Wstawianie i Usuwanie Wezlow:
   - **Wstawianie w drzewie BST**: Polega na lokalizacji wlasciwego miejsca dla nowego wezla, tak aby zachowac wlasciwosci BST.
   - **Usuwanie wezlow w drzewie BST**: Moze odbywac sie w kilku przypadkach - wezel bez dzieci, z jednym dzieckiem lub z dwoma dziecmi. Wymaga odpowiedniego zarzadzania wskaznikami.

3. Balansowanie Drzewa:
   - **Rotacje AVL**: Sa wykorzystywane do balansowania drzew AVL, obejmuja operacje jak LL, LR, RR, RL.
   - **Drzewa czerwono-czarne**: Inny mechanizm balansowania, ktory zapewnia, ze drzewo pozostaje mniej wiecej zbalansowane podczas wstawiania i usuwania.

4. Szukanie najkrotszej sciezki:
   - **Algorytm Dijkstry**: Jest to algorytm sluzacy do znajdowania najkrotszej sciezki w grafie wazonym z jednym zrodlem.
   - **Algorytm A***: Jest to heurystyczny algorytm sluzacy do znajdowania najkrotszej sciezki, ktory zazwyczaj dziala szybciej niz Dijkstra, uzywajac heurystyki do przewidywania odleglosci od celu.

## Zastosowania Drzew
1. Reprezentacja hierarchicznych struktur danych (np. system plikow).
2. Ulatwienie szybkiego wyszukiwania danych (np. drzewa binarne).
3. Wykorzystanie w algorytmach grafowych oraz w sieciach.

## Binarne Drzewo Poszukiwan
Binary Search Tree (BST) to drzewo binarne, ktore spelnia nastepujace wlasciwosci:
1. Lewe poddrzewo kazdego wezla zawiera wylacznie elementy o kluczach mniejszych niz wezel.
2. Prawe poddrzewo kazdego wezla zawiera wylacznie elementy o kluczach wiekszych niz wezel.
3. Zarowno lewe, jak i prawe poddrzewo sa takze binarnymi drzewami poszukiwan.

###  Podstawowe Operacje

1. Wstawianie: Elementy sa wstawiane w taki sposob, ze zachowane sa wlasciwosci BST.

2. Wyszukiwanie: Mozemy efektywnie wyszukiwac elementy, zaczynajac od korzenia i poruszajac sie w dol drzewa, porownujac klucze.

3. Usuwanie: Usuwanie elementu moze byc realizowane na rozne sposoby, zaleznie od tego czy wezel ma zero, jedno czy dwa dzieci.

4. Przeszukiwanie:
    - In-order Traversal: pozwala na odwiedzenie wezlow w posortowanej kolejnosci.
    - Pre-order i Post-order Traversal: maja inne zastosowania.

### Analiza Zlozonosci

Zlozonosc Czasowa:
  - Wyszukiwanie: O(log n) - w przypadku zbalansowanego drzewa, O(n) - w najgorszym przypadku.
  - Wstawianie: O(log n) - w przypadku zbalansowanego drzewa, O(n) - w najgorszym przypadku.
  - Usuwanie: O(log n) - w przypadku zbalansowanego drzewa, O(n) - w najgorszym przypadku.

Zlozonosc Pamieciowa: O(n)
