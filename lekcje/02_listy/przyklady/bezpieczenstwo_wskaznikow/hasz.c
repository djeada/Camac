#include "hasz.h"

char *pobierz_losowy_hash512(void) {
  FILE *wyjscie;
  char nazwa_pliku_danych[11] = "data.tmp";
  char bufor_polecenia[128] = {0};
  size_t ziarno = 10000;
  char *hash = (char *)malloc(sizeof(char) * 128);

  generuj_losowy_plik(nazwa_pliku_danych, ziarno);
  sprintf(bufor_polecenia, "sha512sum %s", nazwa_pliku_danych);
  wyjscie = popen(bufor_polecenia, "r");

  for (int i = 0; i < 128; i++) {
    hash[i] = (char)fgetc(wyjscie);
  }

  pclose(wyjscie);
  remove(nazwa_pliku_danych);
  return hash;
}

void oblicz_hash(char *tekst, char *hash) {
  FILE *wyjscie;
  char nazwa_pliku_danych[11] = "data.tmp";
  char bufor_polecenia[128] = {0};

  FILE *fd = fopen(nazwa_pliku_danych, "w");
  fprintf(fd, "%s", tekst);
  fflush(fd);
  fclose(fd);

  sprintf(bufor_polecenia, "sha512sum %s", nazwa_pliku_danych);
  wyjscie = popen(bufor_polecenia, "r");

  for (int i = 0; i < 128; i++) {
    hash[i] = (char)fgetc(wyjscie);
  }

  pclose(wyjscie);
  remove(nazwa_pliku_danych);
}

void generuj_losowy_plik(char *nazwa, size_t rozmiar) {
  FILE *fd;
  char losowy_bajt;

  srand((unsigned)time(NULL));
  fd = fopen(nazwa, "wb");

  for (size_t i = 0; i < rozmiar; i++) {
    losowy_bajt = (char)rand();
    fwrite(&losowy_bajt, sizeof(char), 1, fd);
  }

  fclose(fd);
}

void szyfruj_dane(char *wsk_danych, size_t dlugosc_danych, char *hash) {
  for (size_t i = 0, j = 0; i < dlugosc_danych; i++, j++) {
    if (j >= 128) {
      j = 0;
    }
    wsk_danych[i] ^= hash[j];
  }

  free(hash);
}

void deszyfruj_dane(char *wsk_danych, size_t dlugosc_danych, char *hash) {
  for (size_t i = 0, j = 0; i < dlugosc_danych; i++, j++) {
    if (j >= 128) {
      j = 0;
    }
    wsk_danych[i] ^= hash[j];
  }

  free(hash);
}
