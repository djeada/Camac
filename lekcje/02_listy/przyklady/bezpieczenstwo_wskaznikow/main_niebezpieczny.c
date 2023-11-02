#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#include "hasz.h"

struct DaneOsobowe {
  char imie[64];
  int wiek;
  char pesel[12];
};

struct DaneOsobowe osoby[3] = {{"Andrzej", 37, "82072356132"},
                               {"Barbara", 63, "56011256731"},
                               {"Karol", 14, "05112235614"}};

// 'password' przechowuje haslo wpisane przez uzytkownika
char password[128] = {"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"};

// 'reference_password' to haslo, ktore jest sprawdzane
char reference_password[128] = {"Lubie"};

// Funkcja, ktora powinna czyscic dane wrazliwe z pamieci
void wyczysc_pamiec(void *ptr, size_t size) {
  size_t i = 0;
  for (i = 0; i < size; i++)
    *((char *)ptr) = '\0';
}

void wyswietl_dane(struct DaneOsobowe *dane) {
  printf("Imie: %s\tWiek: %d\tPESEL: %s\n", dane->imie, dane->wiek,
         dane->pesel);
}

int main(int argc, char *args[]) {
  printf("To ja: %p\n", __func__);

  // Niebezpieczenstwo: Uzycie funkcji 'scanf' z '%s' bez ograniczenia dlugosci
  // moze prowadzic do przepelnienia bufora (buffer overflow)
  printf("Haslo: ");
  scanf("%s", password);

  // Niebezpieczenstwo: Porownywanie hasel przy uzyciu 'strncmp' z ustalona
  // dlugoscia moze prowadzic do falszywego pozytywnego wyniku, jesli haslo jest
  // krotsze
  if (!strncmp(password, reference_password, 12)) {
    // Pomysl na wyczyszczenie hasla jest dobry, ale nie gwarantuje
    // ze dane rzeczywiscie zostana usuniete z pamieci
    wyczysc_pamiec((void *)password, 128);

    printf("Dostep przyznany!\n");
    struct DaneOsobowe *wskaznik_danych = osoby;

    for (int i = 0; i < 3; i++) {
      wyswietl_dane(wskaznik_danych++);
    }
  } else {
    printf("Dostep zabroniony!\n");
  }

  return 0;
}
