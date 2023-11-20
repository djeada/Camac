# Wprowadzenie do Struktur Danych

Struktury danych sa kluczowym elementem w dziedzinie informatyki, pozwalajac na efektywne organizowanie, przechowywanie i manipulacje danymi. Ponizej przedstawiamy glowne kategorie struktur danych, ktore beda omawiane w tym kursie:

## Liniowe Struktury Danych

### Tablice
- **Definicja**: Stala przestrzen przechowujaca elementy tego samego typu.
- **Operacje**: Dostep do elementow, wstawianie, usuwanie.

### Listy
- **Definicja**: Zestaw polaczonych elementow, ktore moga przechowywac dane roznych typow.
- **Operacje**: Wstawianie, usuwanie, przeszukiwanie, iteracja.

### Stosy
- **Definicja**: Struktura danych operujaca na zasadzie "ostatni na wierzchu, pierwszy do obslugi" (LIFO).
- **Operacje**: Dodawanie (push), usuwanie (pop), szczyt (top).

### Kolejki
- **Definicja**: Struktura danych operujaca na zasadzie "pierwszy na wierzchu, pierwszy do obslugi" (FIFO).
- **Operacje**: Dodawanie (enqueue), usuwanie (dequeue), front.

## Nie-liniowe Struktury Danych

### Drzewa
- **Definicja**: Hierarchiczna struktura danych, ktora zaczyna sie od korzenia i rozwija sie w galezie i liscie.
- **Operacje**: Wstawianie, usuwanie, przeszukiwanie.

### Grafy
- **Definicja**: Zbior wierzcholkow polaczonych krawedziami, ktore moga przedstawiac relacje miedzy obiektami.
- **Operacje**: Dodawanie wierzcholkow, dodawanie krawedzi, przeszukiwanie (DFS, BFS).

### Tablice z Haszowaniem (HashMap)
- **Definicja**: Struktura danych, ktora przechowuje elementy w parach klucz-wartosc.
- **Operacje**: Dodawanie, usuwanie, przeszukiwanie na podstawie klucza.

## Listy pod lupa
Listy sa podstawowymi strukturami danych, ktore przechowuja elementy w uporzadkowany sposob. Istnieja rozne typy list, takie jak:

1. **Lista Jednokierunkowa (Singly Linked List)**
2. **Lista Dwukierunkowa (Doubly Linked List)**
3. **Lista Cykliczna (Circular Linked List)**

### Operacje na Listach

Podstawowe Operacje:
- `Wstawianie (Insertion)`: Dodanie nowego elementu do listy.
- `Usuniecie (Deletion)`: Usuniecie elementu z listy.
- `Wyszukiwanie (Searching)`: Znalezienie elementu w liscie.
- `Indeksowanie (Indexing)`: Dostep do elementu poprzez jego indeks.

Operacje Zaawansowane:
- `Odwrocenie (Reversal)`: Odwrocenie kolejnosci elementow w liscie.
- `Sortowanie (Sorting)`: Uporzadkowanie elementow listy wedlug okreslonego kryterium.

### Zlozonosc Czasowa i Pamieciowa

Operacje na listach moga miec rozna zlozonosc czasowa i pamieciowa, w zaleznosci od ich struktury i implementacji. Ogolnie:

- Wstawianie: O(1) lub O(n)
- Usuniecie: O(1) lub O(n)
- Wyszukiwanie: O(n)

## Implementacja List za pomoca Wskaznikow w Jezyku C

W jezyku C, listy (takie jak listy jednokierunkowe czy dwukierunkowe) sa czesto implementowane przy uzyciu wskaznikow. Ponizej przedstawiono ogolny przeglad tego, jak mozna to zrobic.

### Definicja Wezla
Definiujemy strukture wezla, ktora przechowuje dane oraz wskaznik(-i) do innych wezlow.

```c
struct Node {
    int data;
    struct Node* next;  // Dla listy jednokierunkowej
    struct Node* prev;  // Dla listy dwukierunkowej (opcjonalnie)
};
```

### Inicjalizacja Listy

Inicjalizujemy liste, tworzac wskaznik do glowy listy (najczesciej ustawiony na NULL).

```c
struct Node* head = NULL;
```

### Wstawianie Elementu

Funkcja, ktora wstawia nowy element na poczatek listy.

```c
void insert_at_beginning(struct Node** head_ref, int new_data) {
    struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));
    new_node->data = new_data;
    new_node->next = (*head_ref);
    new_node->prev = NULL;
    if ((*head_ref) != NULL)
        (*head_ref)->prev = new_node;
    (*head_ref) = new_node;
}
```

### Usuniecie Elementu

Funkcja do usuwania elementu z listy.

```c
void delete_node(struct Node** head_ref, struct Node* del) {
    if (*head_ref == NULL || del == NULL)
        return;
    if (*head_ref == del)
        *head_ref = del->next;
    if (del->next != NULL)
        del->next->prev = del->prev;
    if (del->prev != NULL)
        del->prev->next = del->next;
    free(del);
}
```
