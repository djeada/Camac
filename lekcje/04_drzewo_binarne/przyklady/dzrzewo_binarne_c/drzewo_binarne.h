#ifndef DRZEWO_BINARNE_H
#define DRZEWO_BINARNE_H

// Struktura reprezentujaca wezel drzewa binarnego
typedef struct Wezel {
  int klucz;
  struct Wezel *lewe;
  struct Wezel *prawe;
} Wezel;

// Funkcje
Wezel *utworz_wezel(int klucz);
Wezel *dodaj_wezel(Wezel *korzen, int klucz);
void wyswietl_drzewo(Wezel *korzen);

#endif // DRZEWO_BINARNE_H
