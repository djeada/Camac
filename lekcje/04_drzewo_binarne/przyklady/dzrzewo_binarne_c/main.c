#include "drzewo_binarne.h"

int main() {
  Wezel *korzen = NULL;
  korzen = dodaj_wezel(korzen, 20);
  dodaj_wezel(korzen, 8);
  dodaj_wezel(korzen, 22);
  dodaj_wezel(korzen, 4);
  dodaj_wezel(korzen, 12);

  printf("Drzewo binarne (inorder): ");
  wyswietl_drzewo(korzen);
  printf("\n");

  return 0;
}
