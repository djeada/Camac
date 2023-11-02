#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_LICZBA_ELEMENTOW 100

void sortowanie_babelkowe(int *lista, int n);
void sortowanie_przez_wybieranie(int *lista, int n);
void sortowanie_przez_wstawianie(int *lista, int n);
void wyswietl(int *lista, int n);

int main() {
  srand(time(0));

  int liczba_elementow;
  char algorytm[20];
  char metoda_generowania[4];

  printf("Podaj liczbe elementow elementow do posortowania (max 100): ");
  scanf("%d", &liczba_elementow);

  if (liczba_elementow > MAX_LICZBA_ELEMENTOW || liczba_elementow < 1) {
    printf("Nieprawidlowa liczba elementow. Zakres: 1-100.\n");
    return 1;
  }

  printf("Czy chcesz wprowadzic liczby recznie? (tak/nie): ");
  scanf("%s", metoda_generowania);

  int lista_wartosci[liczba_elementow];

  if (strcmp(metoda_generowania, "tak") == 0) {
    for (int i = 0; i < liczba_elementow; i++) {
      printf("Podaj wartosc dla elementu %d: ", i + 1);
      scanf("%d", &lista_wartosci[i]);
    }
  } else {
    for (int i = 0; i < liczba_elementow; i++) {
      lista_wartosci[i] = rand() % 100 + 1;
    }
  }

  printf("Wybierz algorytm sortowania (babelkowe/wybieranie/wstawianie): ");
  scanf("%s", algorytm);

  if (strcmp(algorytm, "babelkowe") == 0) {
    sortowanie_babelkowe(lista_wartosci, liczba_elementow);
  } else if (strcmp(algorytm, "wybieranie") == 0) {
    sortowanie_przez_wybieranie(lista_wartosci, liczba_elementow);
  } else if (strcmp(algorytm, "wstawianie") == 0) {
    sortowanie_przez_wstawianie(lista_wartosci, liczba_elementow);
  } else {
    printf("Nieznany algorytm sortowania.\n");
    return 1;
  }

  return 0;
}

void sortowanie_babelkowe(int *lista, int n) {
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n - i - 1; j++) {
      if (lista[j] > lista[j + 1]) {
        int temp = lista[j];
        lista[j] = lista[j + 1];
        lista[j + 1] = temp;
      }
    }
    wyswietl(lista, n);
  }
}

void sortowanie_przez_wybieranie(int *lista, int n) {
  for (int i = 0; i < n - 1; i++) {
    int min_indeks = i;
    for (int j = i + 1; j < n; j++) {
      if (lista[j] < lista[min_indeks]) {
        min_indeks = j;
      }
    }
    int temp = lista[min_indeks];
    lista[min_indeks] = lista[i];
    lista[i] = temp;
    wyswietl(lista, n);
  }
}

void sortowanie_przez_wstawianie(int *lista, int n) {
  for (int i = 1; i < n; i++) {
    int klucz = lista[i];
    int j = i - 1;
    while (j >= 0 && lista[j] > klucz) {
      lista[j + 1] = lista[j];
      j = j - 1;
    }
    lista[j + 1] = klucz;
    wyswietl(lista, n);
  }
}

void wyswietl(int *lista, int n) {
  for (int i = 0; i < n; i++) {
    printf("%d ", lista[i]);
  }
  printf("\n");
}
