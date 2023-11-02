#include "graf.h"
#include <stdio.h>
#include <stdlib.h>

// Funkcje pomocnicze
Wierzcholek *nowyWierzcholek(int id) {
  Wierzcholek *nowy = (Wierzcholek *)malloc(sizeof(Wierzcholek));
  nowy->id = id;
  nowy->nastepny = NULL;
  return nowy;
}

// Implementacja funkcji
Graf *utworzGraf(int liczbaWierzcholkow) {
  Graf *graf = (Graf *)malloc(sizeof(Graf));
  graf->liczbaWierzcholkow = liczbaWierzcholkow;
  graf->listaSasiedztwa =
      (Wierzcholek **)malloc(liczbaWierzcholkow * sizeof(Wierzcholek *));
  for (int i = 0; i < liczbaWierzcholkow; i++) {
    graf->listaSasiedztwa[i] = NULL;
  }
  return graf;
}

void dodajKrawedz(Graf *graf, int src, int dest) {
  Wierzcholek *nowy = nowyWierzcholek(dest);
  nowy->nastepny = graf->listaSasiedztwa[src];
  graf->listaSasiedztwa[src] = nowy;

  nowy = nowyWierzcholek(src);
  nowy->nastepny = graf->listaSasiedztwa[dest];
  graf->listaSasiedztwa[dest] = nowy;
}

void usunKrawedz(Graf *graf, int src, int dest) {
  Wierzcholek *temp = graf->listaSasiedztwa[src];
  Wierzcholek *poprzedni = NULL;

  while (temp != NULL && temp->id != dest) {
    poprzedni = temp;
    temp = temp->nastepny;
  }

  if (poprzedni == NULL) {
    graf->listaSasiedztwa[src] = temp->nastepny;
  } else {
    poprzedni->nastepny = temp->nastepny;
  }
  free(temp);

  // Powtorz dla dest->src
  temp = graf->listaSasiedztwa[dest];
  poprzedni = NULL;
  while (temp != NULL && temp->id != src) {
    poprzedni = temp;
    temp = temp->nastepny;
  }

  if (poprzedni == NULL) {
    graf->listaSasiedztwa[dest] = temp->nastepny;
  } else {
    poprzedni->nastepny = temp->nastepny;
  }
  free(temp);
}

void usunWierzcholek(Graf *graf, int wierzcholek) {
  for (int i = 0; i < graf->liczbaWierzcholkow; i++) {
    if (i == wierzcholek || graf->listaSasiedztwa[i] == NULL) {
      continue;
    }
    usunKrawedz(graf, i, wierzcholek);
  }
  free(graf->listaSasiedztwa[wierzcholek]);
  graf->listaSasiedztwa[wierzcholek] = NULL;
}

void wyswietlGraf(Graf *graf) {
  for (int i = 0; i < graf->liczbaWierzcholkow; i++) {
    Wierzcholek *temp = graf->listaSasiedztwa[i];
    printf("Wierzcholek %d: ", i);
    while (temp) {
      printf("%d ", temp->id);
      temp = temp->nastepny;
    }
    printf("\n");
  }
}

void zwolnijGraf(Graf *graf) {
  for (int i = 0; i < graf->liczbaWierzcholkow; i++) {
    Wierzcholek *temp = graf->listaSasiedztwa[i];
    while (temp) {
      Wierzcholek *nastepny = temp->nastepny;
      free(temp);
      temp = nastepny;
    }
  }
  free(graf->listaSasiedztwa);
  free(graf);
}
