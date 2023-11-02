#ifndef GRAF_H
#define GRAF_H

#include <stdbool.h>

typedef struct Wierzcholek {
  int id;
  struct Wierzcholek *nastepny;
} Wierzcholek;

typedef struct Graf {
  int liczbaWierzcholkow;
  Wierzcholek **listaSasiedztwa;
} Graf;

Graf *utworzGraf(int liczbaWierzcholkow);
void dodajKrawedz(Graf *graf, int src, int dest);
void usunGraf(Graf *graf);
void BFS(Graf *graf, int start, int cel);
void DFS(Graf *graf, int start, int cel);
bool DFSRekurencyjnie(Graf *graf, int start, int cel, bool *odwiedzone,
                      int *sciezka, int *indeksSciezki);

#endif // GRAF_H
