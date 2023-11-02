#ifndef LISTA_POLACZONA_H
#define LISTA_POLACZONA_H

// Definicja struktury Wezel, reprezentujacej pojedynczy element listy.
typedef struct Wezel {
  int wartosc;            // Wartosc przechowywana w wezle.
  struct Wezel *nastepny; // Wskaznik na nastepny wezel w liscie.
} Wezel;

// Funkcje operujace na liscie polaczonej.
Wezel *utworz_wezel(int wartosc);
void dodaj_na_koniec(Wezel **glowa, int wartosc);
void wypisz_liste(Wezel *glowa);
void usun_liste(Wezel **glowa);

#endif // LISTA_POLACZONA_H
