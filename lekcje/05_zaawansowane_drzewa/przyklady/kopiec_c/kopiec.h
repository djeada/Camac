#ifndef KOPIEC_H
#define KOPIEC_H

typedef struct Kopiec {
  int *tab;      // tablica przechowujaca elementy kopca
  int rozmiar;   // biezacy rozmiar kopca
  int pojemnosc; // maksymalny rozmiar kopca
} Kopiec;

// Funkcje
Kopiec *utworz_kopiec(int pojemnosc);
void zwieksz_klucz(Kopiec *kopiec, int i, int nowa_wartosc);
void wstaw_do_kopca(Kopiec *kopiec, int klucz);
int usun_min(Kopiec *kopiec);
void wyswietl_kopiec(Kopiec *kopiec);

#endif // KOPIEC_H
