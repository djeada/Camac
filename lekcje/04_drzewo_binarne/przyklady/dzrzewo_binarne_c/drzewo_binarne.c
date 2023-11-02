#include "drzewo_binarne.h"
#include <stdio.h>
#include <stdlib.h>

// Funkcja tworzaca nowy wezel drzewa
Wezel *utworz_wezel(int klucz) {
  Wezel *nowy_wezel = (Wezel *)malloc(sizeof(Wezel));
  nowy_wezel->klucz = klucz;
  nowy_wezel->lewe = NULL;
  nowy_wezel->prawe = NULL;
  return nowy_wezel;
}

// Funkcja dodajaca nowy wezel do drzewa
Wezel *dodaj_wezel(Wezel *korzen, int klucz) {
  if (korzen == NULL) {
    return utworz_wezel(klucz);
  }

  if (klucz < korzen->klucz) {
    korzen->lewe = dodaj_wezel(korzen->lewe, klucz);
  } else if (klucz > korzen->klucz) {
    korzen->prawe = dodaj_wezel(korzen->prawe, klucz);
  }

  return korzen;
}

// Funkcja wyswietlajaca drzewo binarne (przechodzenie inorder)
void wyswietl_drzewo(Wezel *korzen) {
  if (korzen != NULL) {
    wyswietl_drzewo(korzen->lewe);
    printf("%d ", korzen->klucz);
    wyswietl_drzewo(korzen->prawe);
  }
}
