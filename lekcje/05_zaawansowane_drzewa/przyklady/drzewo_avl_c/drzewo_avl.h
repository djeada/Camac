#ifndef DRZEWO_AVL_H
#define DRZEWO_AVL_H

typedef struct Wezel {
  int klucz;
  int wysokosc;
  struct Wezel *lewe;
  struct Wezel *prawe;
} Wezel;

// Funkcje
Wezel *utworz_wezel(int klucz);
int wysokosc(Wezel *N);
int maksimum(int a, int b);
Wezel *prawy_obrot(Wezel *y);
Wezel *lewy_obrot(Wezel *x);
int bilans(Wezel *N);
Wezel *dodaj_wezel(Wezel *wezel, int klucz);
void wyswietl_drzewo(Wezel *korzen);

#endif // DRZEWO_AVL_H
