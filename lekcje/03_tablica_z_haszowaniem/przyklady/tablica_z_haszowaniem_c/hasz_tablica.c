#include "hasz_tablica.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

HaszTablica *utworz_tablice() {
  HaszTablica *nowa_tablica = malloc(sizeof(HaszTablica));
  for (int i = 0; i < ROZMIAR_TABLICY; i++) {
    nowa_tablica->tablica[i] = NULL;
  }
  return nowa_tablica;
}

unsigned int funkcja_haszujaca(const char *klucz) {
  unsigned int suma = 0;
  while (*klucz) {
    suma += (unsigned int)*klucz;
    klucz++;
  }
  return suma % ROZMIAR_TABLICY;
}

void dodaj_element(HaszTablica *ht, const char *klucz, const char *wartosc) {
  unsigned int indeks = funkcja_haszujaca(klucz);
  Element *nowy_element = malloc(sizeof(Element));
  nowy_element->klucz = strdup(klucz);
  nowy_element->wartosc = strdup(wartosc);
  nowy_element->nastepny = ht->tablica[indeks];
  ht->tablica[indeks] = nowy_element;
}

char *znajdz_element(HaszTablica *ht, const char *klucz) {
  unsigned int indeks = funkcja_haszujaca(klucz);
  Element *e = ht->tablica[indeks];
  while (e) {
    if (strcmp(e->klucz, klucz) == 0) {
      return e->wartosc;
    }
    e = e->nastepny;
  }
  return NULL;
}

void usun_element(HaszTablica *ht, const char *klucz) {
  unsigned int indeks = funkcja_haszujaca(klucz);
  Element *e = ht->tablica[indeks];
  Element *poprzedni = NULL;
  while (e) {
    if (strcmp(e->klucz, klucz) == 0) {
      if (poprzedni) {
        poprzedni->nastepny = e->nastepny;
      } else {
        ht->tablica[indeks] = e->nastepny;
      }
      free(e->klucz);
      free(e->wartosc);
      free(e);
      return;
    }
    poprzedni = e;
    e = e->nastepny;
  }
}

void zwolnij_tablice(HaszTablica *ht) {
  for (int i = 0; i < ROZMIAR_TABLICY; i++) {
    Element *e = ht->tablica[i];
    while (e) {
      Element *temp = e;
      e = e->nastepny;
      free(temp->klucz);
      free(temp->wartosc);
      free(temp);
    }
  }
  free(ht);
}
