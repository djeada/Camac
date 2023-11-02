#include "kopiec.h"
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

Kopiec *utworz_kopiec(int pojemnosc) {
  Kopiec *kopiec = (Kopiec *)malloc(sizeof(Kopiec));
  kopiec->pojemnosc = pojemnosc;
  kopiec->rozmiar = 0;
  kopiec->tab = (int *)malloc(pojemnosc * sizeof(int));
  return kopiec;
}

int rodzic(int i) { return (i - 1) / 2; }
int lewe_dziecko(int i) { return (2 * i) + 1; }
int prawe_dziecko(int i) { return (2 * i) + 2; }

void zwieksz_klucz(Kopiec *kopiec, int i, int nowa_wartosc) {
  kopiec->tab[i] = nowa_wartosc;
  while (i != 0 && kopiec->tab[rodzic(i)] > kopiec->tab[i]) {
    int temp = kopiec->tab[i];
    kopiec->tab[i] = kopiec->tab[rodzic(i)];
    kopiec->tab[rodzic(i)] = temp;
    i = rodzic(i);
  }
}

void wstaw_do_kopca(Kopiec *kopiec, int klucz) {
  if (kopiec->rozmiar == kopiec->pojemnosc) {
    printf("Kopiec jest pelny. Nie mozna dodac wiecej elementow.\n");
    return;
  }
  kopiec->rozmiar++;
  int i = kopiec->rozmiar - 1;
  kopiec->tab[i] = klucz;
  zwieksz_klucz(kopiec, i, klucz);
}

int usun_min(Kopiec *kopiec) {
  if (kopiec->rozmiar <= 0)
    return INT_MAX;
  if (kopiec->rozmiar == 1) {
    kopiec->rozmiar--;
    return kopiec->tab[0];
  }

  int root = kopiec->tab[0];
  kopiec->tab[0] = kopiec->tab[kopiec->rozmiar - 1];
  kopiec->rozmiar--;
  kopiec_min_heapify(kopiec, 0);

  return root;
}

void kopiec_min_heapify(Kopiec *kopiec, int i) {
  int l = lewe_dziecko(i);
  int r = prawe_dziecko(i);
  int najmniejszy = i;

  if (l < kopiec->rozmiar && kopiec->tab[l] < kopiec->tab[i])
    najmniejszy = l;
  if (r < kopiec->rozmiar && kopiec->tab[r] < kopiec->tab[najmniejszy])
    najmniejszy = r;

  if (najmniejszy != i) {
    int temp = kopiec->tab[i];
    kopiec->tab[i] = kopiec->tab[najmniejszy];
    kopiec->tab[najmniejszy] = temp;
    kopiec_min_heapify(kopiec, najmniejszy);
  }
}

void wyswietl_kopiec(Kopiec *kopiec) {
  for (int i = 0; i < kopiec->rozmiar; ++i)
    printf("%d ", kopiec->tab[i]);
  printf("\n");
}
