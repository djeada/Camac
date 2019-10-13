#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>


struct Lista{
	char ksiazka[64]; //W przyszlosci należy zmienić na void* i size_t albo coś innego
	int liczba_stron;

	struct Lista* next;

	//Lubicie programowanie obiektowe? Po co to komu:
	struct Lista* ja;
	void (*dodaj)(const char*, int);
	int (*wstaw)(int, const char*, int);
	void (*usun)();
	void (*usun_wszystko)();
	int (*usun_index)(int);
	void (*wypisz)();
	void (*wypisz_wszystko)();
	int (*dlugosc)();
}* lista;

void dodaj_element(struct Lista* poczatek, const char* nazwa, int strony);
int wstaw_element(struct Lista* poczatek, int num, const char* ksiazka, int strony);
int usun_element(struct Lista* poczatek);
int usun_element_index(struct Lista* poczatek, int miejsce);
int dlugosc_lista(struct Lista* poczatek);
void usun_liste(struct Lista* poczatek);
void wypisz_element(struct Lista* ptr);
void wypisz_liste(struct Lista* poczatek);

//Pozorowanie obiektowości:
void dodaj_obiektowy(const char* nazwa, int str)
{
	dodaj_element(lista, nazwa, str);
}

int wstaw_obiektowy(int num, const char* ksiazka, int strony)
{
	wstaw_element(lista, num, ksiazka, strony);
}

void usun_obiektowy()
{
	usun_element(lista);
}

void usun_wszystko_obiektowy()
{
	usun_liste(lista);
}

int usun_index_obiektowy(int num)
{
	usun_element_index(lista, num);
}

void wypisz_obiektowy()
{
	
	wypisz_element(lista);
}

void wypisz_wszystko_obiektowy()
{
	wypisz_liste(lista);
}

int dlugosc_obiektowy()
{
	dlugosc_lista(lista);
}

struct Lista* init_element(const char* nazwa, int strony)
{
	struct Lista* lista = (struct Lista*) malloc(sizeof(struct Lista));
	if(lista == NULL)
	{
		perror("Alkoacja pamięci się nie powiodła\n");
		exit(-1);
	}
	strncpy(lista->ksiazka, nazwa, 64);
	lista->liczba_stron = strony;
	lista->next = NULL;

	//Inicjalizacja obiektowosci:
	lista->ja = lista;
	lista->dodaj = dodaj_obiektowy;
	lista->wstaw = wstaw_obiektowy;
	lista->usun = usun_obiektowy;
	lista->usun_index = usun_index_obiektowy;
	lista->usun_wszystko = usun_wszystko_obiektowy;
	lista->wypisz = wypisz_obiektowy;
	lista->wypisz_wszystko = wypisz_wszystko_obiektowy;
	lista->dlugosc = dlugosc_obiektowy;
	return lista;			
}

void dodaj_element(struct Lista* poczatek, const char* nazwa, int strony)
{
	struct Lista* ptr = poczatek;

	while(ptr->next != NULL)
	{
		ptr = ptr->next;
	}

	ptr->next = (struct Lista*) malloc(sizeof(struct Lista)); 
	
	if(ptr == NULL)
	{
		perror("Alkoacja pamięci się nie powiodła\n");
		exit(-1);
	}

	strncpy(ptr->next->ksiazka, nazwa, 64);
	ptr->next->liczba_stron = strony;
	ptr->next->next = NULL;
	
	//Dodanie obiektowosci:
	ptr->ja = ptr;
	ptr->next->ja = lista;
	ptr->next->dodaj = dodaj_obiektowy;
	ptr->next->wstaw = wstaw_obiektowy;
	ptr->next->usun = usun_obiektowy;
	ptr->next->usun_index = usun_index_obiektowy;
	ptr->next->usun_wszystko = usun_wszystko_obiektowy;
	ptr->next->wypisz = wypisz_obiektowy;
	ptr->next->wypisz_wszystko = wypisz_wszystko_obiektowy;
	ptr->next->dlugosc = dlugosc_obiektowy;
}


int usun_element(struct Lista* poczatek)
{
	if(poczatek != NULL)
	{
		struct Lista* ptr = poczatek;
		struct Lista* ptr_prev = poczatek;

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

int dlugosc_lista(struct Lista* poczatek)
{
	int d = 1;
	struct Lista* ptr = poczatek;

	while(ptr->next != NULL)
	{
		d++;
		ptr = ptr->next;
	}

	return d;
}

void usun_liste(struct Lista* poczatek)
{
	while(!usun_element(poczatek)){};	
}

void wypisz_element(struct Lista* ptr)
{
	printf("Tytuł: %s\tLiczba stron: %d\n", ptr->ksiazka, ptr->liczba_stron);
}

void wypisz_liste(struct Lista* poczatek)
{
	struct Lista* ptr = poczatek;
	wypisz_element(ptr);

	while(ptr->next != NULL)
	{
		wypisz_element(ptr->next);
		ptr = ptr->next;
	}
}

int wstaw_element(struct Lista* poczatek, int num, const char* ksiazka, int strony)
{
	struct Lista* ptr = poczatek;
	struct Lista* ptr_old = poczatek;
	
	int i = 1;

	if(num > dlugosc_lista(ptr) || num <= 0)
	{
		perror("Operacja wstawienia jest niemożliwa\n");
		return -1;
	}

	while(i < num)
	{
		ptr = ptr->next;
		i++;
	}

	ptr_old = ptr->next;
	ptr->next = (struct Lista*) malloc(sizeof(struct Lista));
	ptr->next->next = ptr_old;

	strncpy(ptr->next->ksiazka, ksiazka, 64);
	ptr->next->liczba_stron = strony;

	//Obiektowe bajery:
	ptr->ja = ptr;
	ptr->next->ja = lista;
	ptr->next->dodaj = dodaj_obiektowy;
	ptr->next->wstaw = wstaw_obiektowy;
	ptr->next->usun = usun_obiektowy;
	ptr->next->usun_index = usun_index_obiektowy;
	ptr->next->usun_wszystko = usun_wszystko_obiektowy;
	ptr->next->wypisz = wypisz_obiektowy;
	ptr->next->wypisz_wszystko = wypisz_wszystko_obiektowy;
	ptr->next->dlugosc = dlugosc_obiektowy;
	return 0;	
}

int usun_element_index(struct Lista* poczatek, int miejsce)
{
	struct Lista* ptr = poczatek;
	struct Lista* ptr_prev;
	int i=0;
	if(miejsce > dlugosc_lista(ptr) || miejsce <= 0)
	{
		perror("Operacja wstawienia jest niemożliwa\n");
		return -1;
	}

	while(i < miejsce)
	{
		ptr_prev = ptr;
		ptr = ptr->next;
		i++;
	}
	
	ptr_prev->next = ptr->next;
	free(ptr);
	return 0;
}

struct Lista* podzel(struct Lista* poczatek, float stosunek)
{
	struct Lista* ptr = poczatek;
	struct Lista* druga;

	int dlugosc = dlugosc_lista(ptr);
	int dlugosc_pierwsza = stosunek * dlugosc;
	int dlugosc_druga = dlugosc - dlugosc_pierwsza;

	
	//Dopisac!	
	
	return druga;
}

int main(void)
{
	lista = init_element("Dziady\0", 300);
	lista->dodaj("Kordian\0", 50);
	lista->dodaj("Przepisy babuni\0", 111);
	lista->dodaj("W jakim języku nie programować\0", 57);

	printf("Dlugosc listy: %d\n", lista->dlugosc());

	lista->wypisz_wszystko();
	lista->wstaw(1, "Nalepioki", 12);
	printf("#######Druga operacja#######\n");
	lista->wypisz_wszystko();
	lista->usun_index(1);
	printf("#######Trzecia operacja#####\n");
	lista->wypisz_wszystko();
	lista->usun_wszystko();

	return 0;
}
