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

  BFS(graf, 0, 4);
  DFS(graf, 0, 4);

  zwolnijGraf(graf);

  return 0;
}
