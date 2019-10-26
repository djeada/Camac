#include "lists.h"

int main()
{
	char a = 'A';
	struct List* l;
	init(l, sizeof(char));
	push_list(l, (void*) &a);
	a = 'b';
	push_list(l, (void*) &a);
	a = 'c';
	push_list(l, (void*) &a);
	a = 'D';
	insert_list(l, (void*) &a, 0);

	printf("Dana z listy %c\n", *((char*) get_list(l, 0)));
	printf("Dana z listy %c\n", *((char*) get_list(l, 1)));
	printf("Dana z listy %c\n", *((char*) get_list(l, 2)));
	printf("Dana z listy %c\n", *((char*) get_list(l, 3)));
	printf("Dlugosc: %ld\n", l->num);

	print_data(l, 2, char, "Wartosc: %c\n");
	del_list(l, 1);
	print_all(l, char, "Wartosc: %c\n");

	pop_list(l);
	pop_list(l);
	printf("Dlugosc: %ld\n", l->num);
	clear_list(l);
	free_list(l);

	return 0;
}
