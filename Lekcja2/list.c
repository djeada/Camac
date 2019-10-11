#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

struct Pudelko{
	char ksiazka[32];
	int liczba_stron;

	struct Pudelko* next;
};

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
	  
}

/*
void usun_pudelko(struct Pudelko* ptr)
{
	
}
*/

int main(void)
{
	struct Pudelko* lista = init_pudelko("Dziady", 300);
	dodaj_pudelko(lista, "Kordian", 50);
	dodaj_pudelko(lista, "Przepisy babuni", 111);
	dodaj_pudelko(lista, "W jakim języku nie programować?", 57);

	free(lista->next->next->next);
	free(lista->next->next);
	free(lista->next);
	free(lista);

	return 0;
}
