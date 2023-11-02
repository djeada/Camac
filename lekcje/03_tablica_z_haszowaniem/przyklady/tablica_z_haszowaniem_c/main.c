#include "hasz_tablica.h"
#include <stdio.h>

int main() {
  // Utworz nowa tablice haszujaca
  HaszTablica *ht = utworz_tablice();

  // Dodaj elementy do tablicy haszujacej
  dodaj_element(ht, "imie", "Jan");
  dodaj_element(ht, "nazwisko", "Kowalski");
  dodaj_element(ht, "wiek", "30");

  // Szukaj elementow w tablicy haszujacej
  printf("Imie: %s\n", znajdz_element(ht, "imie"));
  printf("Nazwisko: %s\n", znajdz_element(ht, "nazwisko"));
  printf("Wiek: %s\n", znajdz_element(ht, "wiek"));

  // Usun element z tablicy haszujacej
  usun_element(ht, "wiek");

  // Probuj znalezc usuniety element
  if (znajdz_element(ht, "wiek") == NULL) {
    printf("Element o kluczu 'wiek' zostal usuniety.\n");
  }

  // Zwolnij pamiec
  zwolnij_tablice(ht);

  return 0;
}
