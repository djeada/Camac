#include "drzewo_avl.h"
#include <stdio.h>
#include <stdlib.h>

Wezel *utworz_wezel(int klucz) {
  Wezel *wezel = (Wezel *)malloc(sizeof(Wezel));
  wezel->klucz = klucz;
  wezel->lewe = NULL;
  wezel->prawe = NULL;
  wezel->wysokosc = 1; // nowy wezel jest zawsze dodawany na lisc
  return wezel;
}

int wysokosc(Wezel *N) {
  if (N == NULL)
    return 0;
  return N->wysokosc;
}

int maksimum(int a, int b) { return (a > b) ? a : b; }

Wezel *prawy_obrot(Wezel *y) {
  Wezel *x = y->lewe;
  Wezel *T2 = x->prawe;

  // Wykonaj obrot
  x->prawe = y;
  y->lewe = T2;

  // Uaktualnij wysokosc
  y->wysokosc = maksimum(wysokosc(y->lewe), wysokosc(y->prawe)) + 1;
  x->wysokosc = maksimum(wysokosc(x->lewe), wysokosc(x->prawe)) + 1;

  // Zwroc nowy korzen
  return x;
}

Wezel *lewy_obrot(Wezel *x) {
  Wezel *y = x->prawe;
  Wezel *T2 = y->lewe;

  // Wykonaj obrot
  y->lewe = x;
  x->prawe = T2;

  // Uaktualnij wysokosc
  x->wysokosc = maksimum(wysokosc(x->lewe), wysokosc(x->prawe)) + 1;
  y->wysokosc = maksimum(wysokosc(y->lewe), wysokosc(y->prawe)) + 1;

  // Zwroc nowy korzen
  return y;
}

int bilans(Wezel *N) {
  if (N == NULL)
    return 0;
  return wysokosc(N->lewe) - wysokosc(N->prawe);
}

Wezel *dodaj_wezel(Wezel *wezel, int klucz) {
  if (wezel == NULL)
    return utworz_wezel(klucz);

  if (klucz < wezel->klucz)
    wezel->lewe = dodaj_wezel(wezel->lewe, klucz);
  else if (klucz > wezel->klucz)
    wezel->prawe = dodaj_wezel(wezel->prawe, klucz);
  else // rowna wartosc klucza jest zabroniona w drzewie AVL
    return wezel;

  // Uaktualnij wysokosc wezla
  wezel->wysokosc = 1 + maksimum(wysokosc(wezel->lewe), wysokosc(wezel->prawe));

  // Uzyskaj wartosc bilansu, aby sprawdzic, czy wezel jest niezrownowazony
  int balans = bilans(wezel);

  // Jesli wezel jest niezrownowazony, sa 4 przypadki

  // Lewy Lewy
  if (balans > 1 && klucz < wezel->lewe->klucz)
    return prawy_obrot(wezel);

  // Prawy Prawy
  if (balans < -1 && klucz > wezel->prawe->klucz)
    return lewy_obrot(wezel);

  // Lewy Prawy
  if (balans > 1 && klucz > wezel->lewe->klucz) {
    wezel->lewe = lewy_obrot(wezel->lewe);
    return prawy_obrot(wezel);
  }

  // Prawy Lewy
  if (balans < -1 && klucz < wezel->prawe->klucz) {
    wezel->prawe = prawy_obrot(wezel->prawe);
    return lewy_obrot(wezel);
  }

  // Niezmienione drzewo
  return wezel;
}

void wyswietl_drzewo(Wezel *korzen) {
  if (korzen != NULL) {
    wyswietl_drzewo(korzen->lewe);
    printf("%d ", korzen->klucz);
    wyswietl_drzewo(korzen->prawe);
  }
}
