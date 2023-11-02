#include "kopiec.h"

int main() {
  Kopiec *kopiec = utworz_kopiec(11);

  wstaw_do_kopca(kopiec, 3);
  wstaw_do_kopca(kopiec, 1);
  wstaw_do_kopca(kopiec, 15);
  wstaw_do_kopca(kopiec, 5);
  wstaw_do_kopca(kopiec, 4);
  wstaw_do_kopca(kopiec, 45);

  printf("Kopiec: ");
  wyswietl_kopiec(kopiec);

  printf("Usuniety najmniejszy element: %d\n", usun_min(kopiec));

  printf("Kopiec po usunieciu elementu: ");
  wyswietl_kopiec(kopiec);

  return 0;
}
