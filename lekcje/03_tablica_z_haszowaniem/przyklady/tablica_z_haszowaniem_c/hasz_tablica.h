#ifndef HASZTABLICA_H
#define HASZTABLICA_H

#define ROZMIAR_TABLICY 100

typedef struct Element {
  char *klucz;
  char *wartosc;
  struct Element *nastepny;
} Element;

typedef struct HaszTablica {
  Element *tablica[ROZMIAR_TABLICY];
} HaszTablica;

HaszTablica *utworz_tablice();
void dodaj_element(HaszTablica *ht, const char *klucz, const char *wartosc);
char *znajdz_element(HaszTablica *ht, const char *klucz);
void usun_element(HaszTablica *ht, const char *klucz);
void zwolnij_tablice(HaszTablica *ht);
unsigned int funkcja_haszujaca(const char *klucz);

#endif
