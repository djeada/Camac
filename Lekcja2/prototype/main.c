#include "lists.h"

int main()
{
	char a = 'A';
	struct List* l;
	init(l, sizeof(char));
	push(l, (void*) &a);
	a = 'b';
	push(l, (void*) &a);
	a = 'c';
	push(l, (void*) &a);
	a = 'D';
	insert(l, (void*) &a, 0);

	printf("Dana z listy %c\n", *((char*) get(l, 0)));
	printf("Dana z listy %c\n", *((char*) get(l, 1)));
	printf("Dana z listy %c\n", *((char*) get(l, 2)));
	printf("Dana z listy %c\n", *((char*) get(l, 3)));
	printf("Dlugosc: %ld\n", l->num);

	print_data(l, 2, char, "Wartosc: %c\n");
	del(l, 1);
	print_all(l, char, "Wartosc: %c\n");

	pop(l);
	pop(l);
	printf("Dlugosc: %ld\n", l->num);
	clear(l);
	free_list(l);

	return 0;
}
