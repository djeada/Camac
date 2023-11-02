#include "graf.h"
#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

Graf *utworzGraf(int liczbaWierzcholkow) {
  Graf *graf = (Graf *)malloc(sizeof(Graf));
  graf->liczbaWierzcholkow = liczbaWierzcholkow;
  graf->listaSasiedztwa = malloc(liczbaWierzcholkow * sizeof(Wierzcholek *));
  for (int i = 0; i < liczbaWierzcholkow; i++)
    graf->listaSasiedztwa[i] = NULL;
  return graf;
}

void dodajKrawedz(Graf *graf, int src, int dest) {
  Wierzcholek *nowy = (Wierzcholek *)malloc(sizeof(Wierzcholek));
  nowy->id = dest;
  nowy->nastepny = graf->listaSasiedztwa[src];
  graf->listaSasiedztwa[src] = nowy;
}

void usunGraf(Graf *graf) {
  for (int i = 0; i < graf->liczbaWierzcholkow; i++) {
    Wierzcholek *wierzcholek = graf->listaSasiedztwa[i];
    while (wierzcholek) {
      Wierzcholek *temp = wierzcholek;
      wierzcholek = wierzcholek->nastepny;
      free(temp);
    }
  }
  free(graf->listaSasiedztwa);
  free(graf);
}

void BFS(Graf *graf, int start, int cel) {
  // Kod BFS
  // TODO
}

void DFS(Graf *graf, int start, int cel) {
  bool odwiedzone[graf->liczbaWierzcholkow];
  for (int i = 0; i < graf->liczbaWierzcholkow; i++)
    odwiedzone[i] = false;

  int *sciezka = malloc(graf->liczbaWierzcholkow * sizeof(int));
  int indeksSciezki = 0;

  printf("Szukanie sciezki DFS z %d do %d:\n", start, cel);
  if (DFSRekurencyjnie(graf, start, cel, odwiedzone, sciezka, &indeksSciezki)) {
    for (int i = 0; i < indeksSciezki; i++)
      printf("%d ", sciezka[i]);
    printf("\n");
  } else {
    printf("Sciezka nie istnieje.\n");
  }

  free(sciezka);
}

bool DFSRekurencyjnie(Graf *graf, int start, int cel, bool *odwiedzone,
                      int *sciezka, int *indeksSciezki) {
  odwiedzone[start] = true;
  sciezka[(*indeksSciezki)++] = start;

  if (start == cel)
    return true;

  Wierzcholek *wierzcholek = graf->listaSasiedztwa[start];
  while (wierzcholek != NULL) {
    if (!odwiedzone[wierzcholek->id]) {
      if (DFSRekurencyjnie(graf, wierzcholek->id, cel, odwiedzone, sciezka,
                           indeksSciezki))
        return true;
    }
    wierzcholek = wierzcholek->nastepny;
  }
  (*indeksSciezki)--;
  return false;
}
