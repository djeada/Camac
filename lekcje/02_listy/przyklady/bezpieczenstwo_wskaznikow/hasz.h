#ifndef HASH_H
#define HASH_H

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

char *pobierz_losowy_hash512(void);
void oblicz_hash(char *tekst, char *hash);
void generuj_losowy_plik(char *nazwa, size_t rozmiar);
void szyfruj_dane(char *wsk_danych, size_t dlugosc_danych, char *hash);
void deszyfruj_dane(char *wsk_danych, size_t dlugosc_danych, char *hash);

#endif
