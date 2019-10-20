#ifndef _LISTS_H_
#define _LISTS_H_
/*  
	"Koniec upośledzenia, początek kalectwa..." - Maxwell, 18.10.2019/23:21
	General data type list for other projects.
*/

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

struct Container{
	void* ptr;
	struct Container* next;
	struct Container* prev;
};

struct List{
	size_t List_ID;
	struct Container* start;
	struct Container* end;
	size_t num;
	size_t size;
	size_t type_size;
};

//Initialization and destruction of list:
struct List* init_list(size_t type_size);
void free_list(struct List* list);

//Basic functions:
void push(struct List* list, void* data); //Add element to end of list
void pop(struct List* list); //Remove element from end of list
void* get(struct List* list, size_t index); //Get data stored on specified list index
void insert(struct List* list, void* data, size_t index); //Insert data on specified list index
void clear(struct List* list); //Remove all elements form list
void del(struct List* list, size_t index); //Remove data on specified list index
size_t lenght(struct List* list); //Return list lenght
//void print(struct List* list, size_t index, const char* format); //Print data stored on specified list index
size_t find(struct List* list, void* data); //Find list index where specified data is stored

//Advanced functions:
struct List* split(struct List* list, float ratio); //Split list in specified ratio, return new list 
struct List* copy(struct List* list); //Make copy of list
void shuffle(struct List* list); //Shuffle data in list
void quick_sort(struct List* list); //Quick sort data in list based on memory adresses

//Printing data like C(dungeon) master:
#define print_data(list,index,type_t,format) ({ \
	void* data = get(list,index);\
	printf(format, *(type_t*) data);\
	})

//Even more divine intelect:
#define print_all(list,type_t,format) ({ \
	int i=0;\
	for(i=0;i<list->num;i++)\
	{ \
		printf("Element %d inside list contain:\n", i);\
		print_data(list,i,type_t,format);\
		putchar('\n');\
	} \
	})
#endif
