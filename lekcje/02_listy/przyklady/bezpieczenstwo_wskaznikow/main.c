#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "hasz.h"

struct DaneOsobowe {
  char imie[64];
  int wiek;
  char pesel[12]; // Zwiekszylem rozmiar, aby pomiescic znak konca ciagu
};

struct DaneOsobowe osoby[3] = {{"Andrzej", 37, "82072356132"},
                               {"Barbara", 63, "56011256731"},
                               {"Karol", 14, "05112235614"}};

char hasz[128] =
    "7e2399e23e6a16ea7b88fb85a3fb6d0550243ba22adf124a0fd00b2da92e1a1b00cffaa1a8"
    "e44c550d7bc71704b195624aa637ebb6d28fd9a8ca5879c77c4339";
char hasz2[128];

char haslo[128] = {'\0'};

void wyczysc_pamiec(void *wsk, size_t rozmiar) {
  memset(wsk, '\0', rozmiar); // Uzywam funkcji memset do wyczyszczenia pamieci
}

void wypisz_dane_osobowe(struct DaneOsobowe *dane) {
  printf("Imie: %s\tWiek: %d\tPESEL: %s\n", dane->imie, dane->wiek,
         dane->pesel);
}

int main(int argc, char *args[]) {
  printf("To ja: %p\n", __func__);

  printf("Haslo: ");
  scanf(
      "%127s",
      haslo); // Dodaje ograniczenie do scanf, aby uniknac przepelnienia bufora

  oblicz_hash(haslo, hasz2);
  wyczysc_pamiec((void *)haslo, 128);

  if (!strncmp(hasz2, hasz, 128)) {
    printf("Dostep przyznany!\n");
    struct DaneOsobowe *wsk_danych = osoby;

    for (int i = 0; i < 3; i++) {
      wypisz_dane_osobowe(wsk_danych++);
    }
  } else {
    printf("Dostep odmowiony!\n");
  }

  return 0;
}
