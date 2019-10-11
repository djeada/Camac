#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>

#include "hash.h"

struct Personal_data{
	char name[64];
	int age;
	char pesel[11];
};

struct Personal_data people[3] = {{"Andrzej", 37, "82072356132"}, {"Barbara", 63, "56011256731"}, {"Karol", 14, "05112235614"}};

char password[128] = {"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"};

char reference_password[128] = {"Lubie"};

void clear_memory_data(void* ptr, size_t size)
{
	size_t i=0;
	for(i = 0; i < size; i++)
		*((char*) ptr) = '\0';
}

void print_personal_data(struct Personal_data* data)
{
	printf("Name: %s\tAge: %d\tPESEL: %s\n", data->name, data->age, data->pesel);
}

int main(int argc, char* args[])
{
	printf("It's me: %p\n", __func__);
	
	printf("Password: ");
	scanf("%s", password);

	if(!strncmp(password, reference_password, 12))
	{
		clear_memory_data((void*) password, 128);
		printf("Access granted!\n");
		struct Personal_data* data_ptr = people;

		for(int i=0; i < 3; i++)
		{
			print_personal_data(data_ptr++);
		}	
	}
	else
	{
		printf("Access denied!\n");
	}

	return 0;
}
