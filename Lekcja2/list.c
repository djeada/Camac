#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

struct Pudelko{
	char ksiazka[64];
	int liczba_stron;

	struct Pudelko* next;

	//Lubicie programowanie obiektowe? Po co to komu:
	struct Pudelko* ja;
	void (*dodaj)( const char*, int);
	void (*usun)();
	void (*usun_wszystko)();
	void (*wypisz)();
	void (*wypisz_wszystko)();
	int (*dlugosc)();
}* lista;

void dodaj_pudelko(struct Pudelko* poczatek, const char* nazwa, int strony);
int usun_pudelko(struct Pudelko* poczatek);
int dlugosc_lista(struct Pudelko* poczatek);
void usun_liste(struct Pudelko* poczatek);
void wypisz_pudelko(struct Pudelko* ptr);
void wypisz_liste(struct Pudelko* poczatek);

//Pozorowanie obiektowości:
void dodaj_obiektowy(const char* nazwa, int str)
{
	dodaj_pudelko(lista, nazwa, str);
}

void usun_obiektowy()
{
	usun_pudelko(lista);
}

void usun_wszystko_obiektowy()
{
	usun_liste(lista);
}

void wypisz_obiektowy()
{
	
	wypisz_pudelko(lista);
}

void wypisz_wszystko_obiektowy()
{
	wypisz_liste(lista);
}

int dlugosc_obiektowy()
{
	dlugosc_lista(lista);
}
//Koniec shizy Maxwella

struct Pudelko* init_pudelko(const char* nazwa, int strony)
{
	struct Pudelko* lista = (struct Pudelko*) malloc(sizeof(struct Pudelko));
	if(lista == NULL)
	{
		perror("Alkoacja pamięci się nie powiodła\n");
		exit(-1);
	}
	strncpy(lista->ksiazka, nazwa, 32);
	lista->liczba_stron = strony;
	lista->next = NULL;

	//Inicjalizacja obiektowosci:
	lista->ja = lista;
	lista->dodaj = dodaj_obiektowy;
	lista->usun = usun_obiektowy;
	lista->usun_wszystko = usun_wszystko_obiektowy;
	lista->wypisz = wypisz_obiektowy;
	lista->wypisz_wszystko = wypisz_wszystko_obiektowy;
	lista->dlugosc = dlugosc_obiektowy;
	return lista;			
}

void dodaj_pudelko(struct Pudelko* poczatek, const char* nazwa, int strony)
{
	struct Pudelko* ptr = poczatek;

	while(ptr->next != NULL)
	{
		ptr = ptr->next;
	}

	ptr->next = (struct Pudelko*) malloc(sizeof(struct Pudelko)); 
	
	if(ptr == NULL)
	{
		perror("Alkoacja pamięci się nie powiodła\n");
		exit(-1);
	}

	strncpy(ptr->next->ksiazka, nazwa, 32);
	ptr->next->liczba_stron = strony;
	ptr->next->next = NULL;
	
	//Dodanie obiektowosci:
	ptr->ja = ptr;
	lista->ja = lista;
	lista->dodaj = dodaj_obiektowy;
	lista->usun = usun_obiektowy;
	lista->usun_wszystko = usun_wszystko_obiektowy;
	lista->wypisz = wypisz_obiektowy;
	lista->wypisz_wszystko = wypisz_wszystko_obiektowy;
	lista->dlugosc = dlugosc_obiektowy;
}


int usun_pudelko(struct Pudelko* poczatek)
{
	if(poczatek != NULL)
	{
		struct Pudelko* ptr = poczatek;
		struct Pudelko* ptr_prev = poczatek;

		while(ptr->next != NULL)
		{
			ptr_prev = ptr;
			ptr = ptr->next;
		}
		if(ptr != ptr_prev)
		{
			free(ptr);
			ptr_prev->next = NULL;
		}
		else
		{
			free(ptr);
			return 1;
		}
	}
	else
		perror("Nie ma więcej elementów w liście!");
	return 0;
}

int dlugosc_lista(struct Pudelko* poczatek)
{
	int d = 1;
	struct Pudelko* ptr = poczatek;

	while(ptr->next != NULL)
	{
		d++;
		ptr = ptr->next;
	}

	return d;
}

void usun_liste(struct Pudelko* poczatek)
{
	while(!usun_pudelko(poczatek)){};	
}

void wypisz_pudelko(struct Pudelko* ptr)
{
	printf("Tytuł: %s\tLiczba stron: %d\n", ptr->ksiazka, ptr->liczba_stron);
}

void wypisz_liste(struct Pudelko* poczatek)
{
	struct Pudelko* ptr = poczatek;
	wypisz_pudelko(ptr);

	while(ptr->next != NULL)
	{
		wypisz_pudelko(ptr->next);
		ptr = ptr->next;
	}
}

int main(void)
{
	lista = init_pudelko("Dziady\0", 300);
	lista->dodaj("Kordian\0", 50);
	lista->dodaj("Przepisy babuni\0", 111);
	lista->dodaj("W jakim języku nie programować\0", 57);

	printf("Dlugosc listy: %d\n", lista->dlugosc());

	lista->wypisz_wszystko();

	lista->usun_wszystko();

	return 0;
}
