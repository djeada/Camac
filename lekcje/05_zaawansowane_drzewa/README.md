## Drzewa AVL

Drzewa AVL sa specyficznym typem drzew binarnych poszukiwan (BST), ktore sa zbalansowane w taki sposob, ze glebokosc lewego i prawego poddrzewa dowolnego wezla rozni sie co najwyzej o 1. Nazwa AVL pochodzi od nazwisk jej wynalazcow: Adelson-Velsky i Landis. Ponizej przedstawiam kluczowe koncepty i operacje zwiazane z drzewami AVL:

### Wlasciwosci

1. **Zbalansowanie**: Kazdy wezel w drzewie AVL ma balans rowny -1, 0 lub 1.
2. **Wyszukiwanie**: Operacja wyszukiwania jest podobna do wyszukiwania w standardowym BST.
3. **Rotacje**: Drzewa AVL uzywaja rotacji (LL, LR, RL, RR) do utrzymania balansu drzewa podczas wstawiania lub usuwania wezlow.

### Operacje

Wstawianie:

1. **Standardowe Wstawianie BST**: W pierwszej kolejnosci, wezel jest wstawiany zgodnie z zasadami BST, czyli w lewym poddrzewie jesli jest mniejszy niz wezel rodzica i w prawym, jesli jest wiekszy.

2. **Aktualizacja Wysokosci**: Po wstawieniu wezla, drzewo moze byc niezbalansowane. Dlatego aktualizujemy wysokosci wszystkich wezlow od nowo wstawionego wezla do korzenia.

3. **Rotacje**: Jesli drzewo jest niezbalansowane (roznica wysokosci lewego i prawego poddrzewa wieksza niz 1), stosujemy odpowiednie rotacje, aby przywrocic rownowage.

Usuwanie:

1. **Standardowe Usuwanie BST**: Usuwanie wezla rozpoczyna sie tak samo, jak w przypadku BST: usuniecie wezla i, jesli to konieczne, zastapienie go nastepca.

2. **Aktualizacja Wysokosci**: Tak jak przy wstawianiu, aktualizujemy wysokosci wezlow od miejsca usuniecia do korzenia.

3. **Rotacje**: Jesli drzewo staje sie niezbalansowane po usunieciu, stosujemy odpowiednie rotacje, aby je zrownowazyc.

Rotacje:

1. **LL (Left-Left)**
   - **Opis**: Stosowana, gdy lewe poddrzewo lewego dziecka jest ciezsze.
   - **Akcja**: Jedna rotacja w prawo.

2. **RR (Right-Right)**
   - **Opis**: Stosowana, gdy prawe poddrzewo prawego dziecka jest ciezsze.
   - **Akcja**: Jedna rotacja w lewo.

3. **LR (Left-Right)**
   - **Opis**: Stosowana, gdy prawe poddrzewo lewego dziecka jest ciezsze.
   - **Akcja**: Rotacja w lewo, a nastepnie w prawo (podwojna rotacja).

4. **RL (Right-Left)**
   - **Opis**: Stosowana, gdy lewe poddrzewo prawego dziecka jest ciezsze.
   - **Akcja**: Rotacja w prawo, a nastepnie w lewo (podwojna rotacja).

## Inne Drzewa

### Drzewa czerwono-czarne

1. **Wlasciwosci**: 
   - Kazdy wezel jest albo czerwony, albo czarny.
   - Korzen jest zawsze czarny.
   - Wszystkie liscie (NIL) sa czarne.
   - Czerwony wezel nie moze miec czerwonego dziecka.
   - Kazda sciezka od korzenia do liscia zawiera te sama liczbe czarnych wezlow.

2. **Operacje**: 
   - Wstawianie
   - Usuwanie
   - Balansowanie

3. **Zastosowania**:
   - Struktury danych, takie jak mapy i zbiory, w wielu bibliotekach standardowych.

### Drzewa B i B+

1. **Wlasciwosci**:
   - Wielopoziomowe, zrownowazone drzewa poszukiwan.
   - Efektywne operacje wstawiania, usuwania i wyszukiwania.
   
2. **Operacje**:
   - Wstawianie
   - Usuwanie
   - Wyszukiwanie

3. **Zastosowania**:
   - Systemy zarzadzania bazami danych
   - Systemy plikow

### Drzewa Trie (drzewa prefiksowe)

1. **Wlasciwosci**:
   - Slowa sa przechowywane w sposob hierarchiczny, gdzie kazdy wezel reprezentuje jedna litere.
   - Szybkie operacje dodawania, wyszukiwania i usuwania.

2. **Operacje**:
   - Dodawanie slowa
   - Wyszukiwanie slowa
   - Usuwanie slowa

3. **Zastosowania**:
   - Autouzupelnianie slow
   - Routing w sieciach komputerowych

### Splay Trees

1. **Wlasciwosci**:
   - Samodostosowujace sie drzewa binarne poszukiwan.
   - Operacje takie jak dostep, wstawianie i usuwanie przesuwaja elementy blizej korzenia.

2. **Operacje**:
   - Splay
   - Wstawianie
   - Usuwanie

3. **Zastosowania**:
   - Implementacje zbiorow i map w pewnych srodowiskach, gdzie pewne klucze sa czesciej uzywane niz inne.

### Drzewa sufiksowe

1. **Wlasciwosci**:
   - Drzewa przechowujace wszystkie sufiksy danego slowa.
   - Umozliwiaja szybkie operacje na ciagach znakow, takie jak wyszukiwanie podciagu.

2. **Operacje**:
   - Budowa drzewa
   - Wyszukiwanie podciagu

3. **Zastosowania**:
   - Wyszukiwanie wzorcow w tekstach
   - Algorytmy kompresji danych
