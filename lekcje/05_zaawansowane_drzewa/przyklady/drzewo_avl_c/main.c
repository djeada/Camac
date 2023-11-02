#include "drzewo_avl.h"

int main() {
  Wezel *korzen = NULL;

  korzen = dodaj_wezel(korzen, 10);
  korzen = dodaj_wezel(korzen, 20);
  korzen = dodaj_wezel(korzen, 30);
  korzen = dodaj_wezel(korzen, 40);
  korzen = dodaj_wezel(korzen, 50);
  korzen = dodaj_wezel(korzen, 25);

  printf("Drzewo AVL (inorder): ");
  wyswietl_drzewo(korzen);
  printf("\n");

  return 0;
}
