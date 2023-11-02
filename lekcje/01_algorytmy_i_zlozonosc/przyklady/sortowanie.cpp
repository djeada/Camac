#include <cstdlib>
#include <ctime>
#include <iostream>
#include <string>
#include <vector>

#define MAX_LICZBA_ELEMENTOW 100

void sortowanie_babelkowe(std::vector<int> &lista);
void sortowanie_przez_wybieranie(std::vector<int> &lista);
void sortowanie_przez_wstawianie(std::vector<int> &lista);
void wyswietl(const std::vector<int> &lista);

int main() {
  srand(time(0));

  int liczba_elementow;
  std::string algorytm;
  std::string metoda_generowania;

  std::cout << "Podaj liczbe elementow elementow do posortowania (max 100): ";
  std::cin >> liczba_elementow;

  if (liczba_elementow > MAX_LICZBA_ELEMENTOW || liczba_elementow < 1) {
    std::cout << "Nieprawidlowa liczba elementow. Zakres: 1-100.\n";
    return 1;
  }

  std::cout << "Czy chcesz wprowadzic liczby recznie? (tak/nie): ";
  std::cin >> metoda_generowania;

  std::vector<int> lista_wartosci(liczba_elementow);

  if (metoda_generowania == "tak") {
    for (int i = 0; i < liczba_elementow; i++) {
      std::cout << "Podaj wartosc dla elementu " << i + 1 << ": ";
      std::cin >> lista_wartosci[i];
    }
  } else {
    for (int i = 0; i < liczba_elementow; i++) {
      lista_wartosci[i] = rand() % 100 + 1;
    }
  }

  std::cout
      << "Wybierz algorytm sortowania (babelkowe/wybieranie/wstawianie): ";
  std::cin >> algorytm;

  if (algorytm == "babelkowe") {
    sortowanie_babelkowe(lista_wartosci);
  } else if (algorytm == "wybieranie") {
    sortowanie_przez_wybieranie(lista_wartosci);
  } else if (algorytm == "wstawianie") {
    sortowanie_przez_wstawianie(lista_wartosci);
  } else {
    std::cout << "Nieznany algorytm sortowania.\n";
    return 1;
  }

  return 0;
}

void sortowanie_babelkowe(std::vector<int> &lista) {
  int n = lista.size();
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n - i - 1; j++) {
      if (lista[j] > lista[j + 1]) {
        int temp = lista[j];
        lista[j] = lista[j + 1];
        lista[j + 1] = temp;
      }
    }
    wyswietl(lista);
  }
}

void sortowanie_przez_wybieranie(std::vector<int> &lista) {
  int n = lista.size();
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
    wyswietl(lista);
  }
}

void sortowanie_przez_wstawianie(std::vector<int> &lista) {
  int n = lista.size();
  for (int i = 1; i < n; i++) {
    int klucz = lista[i];
    int j = i - 1;
    while (j >= 0 && lista[j] > klucz) {
      lista[j + 1] = lista[j];
      j = j - 1;
    }
    lista[j + 1] = klucz;
    wyswietl(lista);
  }
}

void wyswietl(const std::vector<int> &lista) {
  for (int i = 0; i < lista.size(); i++) {
    std::cout << lista[i] << " ";
  }
  std::cout << "\n";
}
