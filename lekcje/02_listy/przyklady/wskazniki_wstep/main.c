#include <stdio.h>
#include <stdlib.h>

int main(void) {
  // Wskazniki typu int:
  puts("\nWskazniki typu int:");

  int a;     // Zmienna typu int
  int *wsk1; // Wskaznik na zmienna typu int

  printf("Przed inicjalizacja:\n");
  printf("Zmienna a = %d, rozmiar: %lu bajtow, adres pamieci: %p\n", a,
         sizeof(int), &a);
  printf("Wskaznik wsk1 = %p, rozmiar: %lu bajtow, adres pamieci: %p\n", wsk1,
         sizeof(int *), &wsk1);
  printf("Po inicjalizacji:\n");

  a = 5;
  wsk1 = &a;

  printf("Zmienna a = %d, rozmiar: %lu bajtow, adres pamieci: %p\n", a,
         sizeof(int), &a);
  printf("Wskaznik wsk1 = %p wskazuje na zmienna a = %d\n", wsk1, *wsk1);

  // Wskazniki typu char:
  puts("\nWskazniki typu char:");

  char b;     // Zmienna typu char
  char *wsk2; // Wskaznik na zmienna typu char

  printf("Przed inicjalizacja:\n");
  printf("Zmienna b = %c, rozmiar: %lu bajtow, adres pamieci: %p\n", b,
         sizeof(char), &b);
  printf("Wskaznik wsk2 = %p, rozmiar: %lu bajtow, adres pamieci: %p\n", wsk2,
         sizeof(char *), &wsk2);
  printf("Po inicjalizacji:\n");

  b = 'A';
  wsk2 = &b;

  printf("Zmienna b = %c, rozmiar: %lu bajtow, adres pamieci: %p\n", b,
         sizeof(char), &b);
  printf("Wskaznik wsk2 = %p wskazuje na zmienna b = %c\n", wsk2, *wsk2);

  // Wskazniki typu float:
  puts("\nWskazniki typu float:");

  float c;     // Zmienna typu float
  float *wsk3; // Wskaznik na zmienna typu float

  printf("Przed inicjalizacja:\n");
  printf("Zmienna c = %f, rozmiar: %lu bajtow, adres pamieci: %p\n", c,
         sizeof(float), &c);
  printf("Wskaznik wsk3 = %p, rozmiar: %lu bajtow, adres pamieci: %p\n", wsk3,
         sizeof(float *), &wsk3);
  printf("Po inicjalizacji:\n");

  c = 0.00123;
  wsk3 = &c;

  printf("Zmienna c = %f, rozmiar: %lu bajtow, adres pamieci: %p\n", c,
         sizeof(float), &c);
  printf("Wskaznik wsk3 = %p wskazuje na zmienna c = %f\n", wsk3, *wsk3);

  // Wskazniki na struktury:
  puts("\nWskazniki na struktury");

  struct Dane {
    int x[100];
    int y[100];
    int z[100];
    float moc;
    struct Dane *nast;
    struct Dane *poprz;
  } d;

  struct Dane *wsk4;

  printf("Przed inicjalizacja:\n");
  printf("Zmienna ma rozmiar %lu bajtow, adres pamieci: %p\n",
         sizeof(struct Dane), &d);
  printf("Wskaznik wsk4 = %p, rozmiar: %lu bajtow, adres pamieci: %p\n", wsk4,
         sizeof(struct Dane *), &wsk4);
  printf("Po inicjalizacji:\n");

  d.moc = 1.0023;
  d.nast = NULL;
  d.poprz = NULL;

  wsk4 = &d;

  printf("Wskaznik wsk4 = %p wskazuje na zmienna o rozmiarze %lu bajtow\n",
         wsk4, sizeof(struct Dane));

  // Wszechstronny wskaznik typu void*:
  puts("\nWskaznik typu void*:");

  void *wsk5;
  wsk5 = &a;
  printf("Wskaznik wsk5 = %p wskazuje na zmienna a = %d\n", wsk5,
         *((int *)wsk5));

  // Niebezpieczny wskaznik
  puts("\nNiebezpieczny wskaznik:");

  // Zmienna 'wsk6' jest zdefiniowana jako 'unsigned long int'. Choc nie jest to
  // wskaznik, moze przechowywac wartosc adresu pamieci, co jednak jest
  // niezalecana praktyka.
  unsigned long int wsk6;

  // Zmienna 'liczba', ktorej adres chcemy przechowac i manipulowac za pomoca
  // 'wsk6'.
  int liczba = 42;
  printf("Oryginalna liczba: %d\n", liczba);

  // Przypisujemy adres zmiennej 'liczba' do 'wsk6', rzutujac go na odpowiedni
  // typ.
  wsk6 = (unsigned long int)&liczba;
  printf("Adres zmiennej 'liczba' przechowany w 'wsk6': %lu\n", wsk6);

  // Teraz mozemy uzyc 'wsk6' do manipulowania zawartoscia zmiennej 'liczba'.
  // Nalezy jednak byc bardzo ostroznym, gdyz taka praktyka moze prowadzic do
  // nieoczekiwanych wynikow i jest trudna do zrozumienia. Oto przyklad zmiany
  // wartosci zmiennej 'liczba' za pomoca 'wsk6'.
  *(int *)wsk6 = 100;
  printf("Zmodyfikowana liczba: %d\n", liczba);

  return 0;
}
