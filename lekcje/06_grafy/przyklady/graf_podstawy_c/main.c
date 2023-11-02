#include "graf.h"
#include <stdio.h>

int main() {
  int liczbaWierzcholkow = 5;
  Graf *graf = utworzGraf(liczbaWierzcholkow);

  dodajKrawedz(graf, 0, 1);
  dodajKrawedz(graf, 0, 4);
  dodajKrawedz(graf, 1, 2);
  dodajKrawedz(graf, 1, 3);
  dodajKrawedz(graf, 1, 4);
  dodajKrawedz(graf, 2, 3);
  dodajKrawedz(graf, 3, 4);

  printf("Graf przed usunieciem krawedzi i wierzcholkow:\n");
  wyswietlGraf(graf);

  usunKrawedz(graf, 1, 4);
  usunWierzcholek(graf, 2);

  printf("\nGraf po usunieciu krawedzi 1-4 i wierzcholka 2:\n");
  wyswietlGraf(graf);

  zwolnijGraf(graf);

  return 0;
}
