#include "lista_polaczona.h"
#include <stdio.h>

int main() {
  Wezel *glowa = NULL;
  dodaj_na_koniec(&glowa, 1);
  dodaj_na_koniec(&glowa, 2);
  dodaj_na_koniec(&glowa, 3);

  printf("Lista polaczona: ");
  wypisz_liste(glowa);

  usun_liste(&glowa);
  return 0;
}
