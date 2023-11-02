#ifndef GRAF_H
#define GRAF_H

#include <stdbool.h>

// Struktura reprezentujaca wierzcholek w liscie sasiedztwa
typedef struct Wierzcholek {
  int id;
  struct Wierzcholek *nastepny;
} Wierzcholek;

// Struktura reprezentujaca graf
typedef struct Graf {
  int liczbaWierzcholkow;
  Wierzcholek **listaSasiedztwa;
} Graf;

Graf *utworzGraf(int liczbaWierzcholkow);
void dodajKrawedz(Graf *graf, int src, int dest);
void usunKrawedz(Graf *graf, int src, int dest);
void usunWierzcholek(Graf *graf, int wierzcholek);
void wyswietlGraf(Graf *graf);
void zwolnijGraf(Graf *graf);

#endif // GRAF_H
