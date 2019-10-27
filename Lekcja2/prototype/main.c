#include "lists.h"

int main()
{
	char a = 'A';
	struct List* l;
	struct List* l2;

	init(l,sizeof(char));
	init(l2, sizeof(int));

	l->push((void*) &a);
	//push_list(l, (void*) &a);
	a = 'b';
	l->push((void*) &a);
	a = 'c';
	push_list(l, (void*) &a);
	a = 'D';
	l->insert((void*) &a, 0);

	//l2
	int b = 5;
	l2->push((void*) &b);
	b = 12;
	l2->insert((void*) &b, l2->lenght() - 1);
	print_all(l2, int, "Lista 2, wartosc:%d\n");
	l2->clear();
	free_list(l2);

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
	l->clear();
	free_list(l);
	
	return 0;
}
