#include <stdio.h>

int main(void)
{
	//Int pointers:
	puts("\nInt pointers:");
	
	int a;; // Variable: int type
	
	int* ptr1; // Int type pointer

	printf("Before initialization:\n");
	printf("Variable a = %d of size %lu bytes, memory adress: %p of size %lu bytes\n", a, sizeof(int), &a, sizeof(int*));
	printf("Pointer ptr1 = %p of size %lu bytes, memory adress: %p of size %lu bytes\n", ptr1, sizeof(int*), &ptr1, sizeof(int**));
	printf("After initialization:\n");
	
	a = 5;
	ptr1 = &a;
	
	printf("Variable a = %d of size %lu bytes, memory adress: %p of size %lu bytes\n", a, sizeof(int), &a, sizeof(int*));
        printf("Pointer ptr1 = %p of size %lu bytes, memory adress: %p of size %lu bytes\n", ptr1, sizeof(int*), &ptr1, sizeof(int**));
	printf("Pointer ptr1 = %p points to variable a = %d\n", ptr1, *ptr1);	
	
	//Char pointers:
	puts("\nChar pointers:");

	char b; // Variable: char type
	
	char* ptr2; // Char type pointer

	printf("Before initialization:\n");
	printf("Variable b = %c of size %lu bytes, memory adress: %p of size %lu bytes\n", b, sizeof(char), &b, sizeof(char*));
	printf("Pointer ptr2 = %p of size %lu bytes, memory adress: %p of size %lu bytes\n", ptr2, sizeof(char*), &ptr2, sizeof(char**));
	printf("After initialization:\n");
	
	b = 'A';
	ptr2 = &b;
	
	printf("Variable b = %c of size %lu bytes, memory adress: %p of size %lu bytes\n", b, sizeof(char), &b, sizeof(char*));
	printf("Pointer ptr2 = %p of size %lu bytes, memory adress: %p of size %lu bytes\n", ptr2, sizeof(char*), &ptr2, sizeof(char**));
	printf("Pointer ptr2 = %p points to variable b = %c\n", ptr2, *ptr2);	

	//Float pointer:
	puts("\nFloat pointers:");

	float c; // Variable: float type
	
	float* ptr3; // Float type pointer

	printf("Before initialization:\n");
	printf("Variable c = %f of size %lu bytes, memory adress: %p of size %lu bytes\n", c, sizeof(float), &c, sizeof(float*));
	printf("Pointer ptr3 = %p of size %lu bytes, memory adress: %p of size %lu bytes\n", ptr3, sizeof(float*), &ptr3, sizeof(float**));
	printf("After initialization:\n");
	
	c = 0.00123;
	ptr3 = &c;
	
	printf("Variable c = %f of size %lu bytes, memory adress: %p of size %lu bytes\n", c, sizeof(float), &c, sizeof(float*));
	printf("Pointer ptr3 = %p of size %lu bytes, memory adress: %p of size %lu bytes\n", ptr3, sizeof(float*), &ptr3, sizeof(float**));
	printf("Pointer ptr3 = %p points to variable c = %f\n", ptr3, *ptr3);	


	//Pointers on structures:	
	puts("\nStructure pointers");

	struct Dane{
		int x[100];
		int y[100];
		int z[100];
		
		float power;
		
		struct Dane* next;
		struct Dane* prev;
	} d;

	struct Dane* ptr4;

	printf("Before initialization:\n");
        printf("Variable have size %lu bytes, memory adress: %p of size %lu bytes\n", sizeof(struct Dane), &d, sizeof(struct Dane*));
        printf("Pointer ptr4 = %p of size %lu bytes, memory adress: %p of size %lu bytes\n", ptr4, sizeof(struct Dane*), &ptr4, sizeof(struct Dane**));
        printf("After initialization:\n");

        //d.x;
	//d.y;
	//d.z;
	d.power = 1.0023;
	d.next = NULL;
	d.prev = NULL;

        ptr4 = &d;

        printf("Pointer ptr4 = %p of size %lu bytes, memory adress: %p of size %lu bytes\n", ptr4, sizeof(struct Dane*), &ptr4, sizeof(struct Dane**));	

	//Powerfull void* pointer: 	

	//Hacky pointer

	unsigned long int ptr5;

	return 0;
}
