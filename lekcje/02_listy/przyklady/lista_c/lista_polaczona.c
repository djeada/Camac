#include "lista_polaczona.h"
#include <stdio.h>
#include <stdlib.h>

// Funkcja tworzaca nowy wezel z podana wartoscia.
Wezel *utworz_wezel(int wartosc) {
  Wezel *nowy_wezel = (Wezel *)malloc(sizeof(Wezel));
  if (nowy_wezel == NULL) {
    fprintf(stderr, "Nie udalo sie zaalokowac pamieci dla nowego wezla.\n");
    exit(EXIT_FAILURE);
  }
  nowy_wezel->wartosc = wartosc;
  nowy_wezel->nastepny = NULL;
  return nowy_wezel;
}

// Funkcja dodajaca nowy wezel na koncu listy.
void dodaj_na_koniec(Wezel **glowa, int wartosc) {
  Wezel *nowy_wezel = utworz_wezel(wartosc);
  if (*glowa == NULL) {
    *glowa = nowy_wezel;
    return;
  }
  Wezel *ostatni = *glowa;
  while (ostatni->nastepny != NULL) {
    ostatni = ostatni->nastepny;
  }
  ostatni->nastepny = nowy_wezel;
}

// Funkcja wypisujaca wszystkie elementy listy.
void wypisz_liste(Wezel *glowa) {
  Wezel *aktualny = glowa;
  while (aktualny != NULL) {
    printf("%d -> ", aktualny->wartosc);
    aktualny = aktualny->nastepny;
  }
  printf("NULL\n");
}

// Funkcja usuwajaca wszystkie elementy listy i zwalniajaca pamiec.
void usun_liste(Wezel **glowa) {
  Wezel *aktualny = *glowa;
  Wezel *nastepny;
  while (aktualny != NULL) {
    nastepny = aktualny->nastepny;
    free(aktualny);
    aktualny = nastepny;
  }
  *glowa = NULL;
}
