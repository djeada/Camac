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
#include <setjmp.h> //Not dead jet
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

	//This shit is back again:
	void (*push)(void*);
	void (*pop)();
	void* (*get)(size_t);
	void (*insert)(void*, size_t);
	void (*clear)();
	void (*del)(size_t);
	size_t (*lenght)();
};

//Initialization and destruction of list:
struct List* init_list(size_t type_size);
void free_list(struct List* list);

//Basic functions:
void push_list(struct List* list, void* data); //Add element to end of list
void pop_list(struct List* list); //Remove element from end of list
void* get_list(struct List* list, size_t index); //Get data stored on specified list index
void insert_list(struct List* list, void* data, size_t index); //Insert data on specified list index
void clear_list(struct List* list); //Remove all elements form list
void del_list(struct List* list, size_t index); //Remove data on specified list index
size_t lenght_list(struct List* list); //Return list lenght
//void print(struct List* list, size_t index, const char* format); //Print data stored on specified list index

//Advanced functions (not implemented):
size_t find_list(struct List* list, void* data); //Find list index where specified data is stored
struct List* split(struct List* list, float ratio); //Split list in specified ratio, return new list 
struct List* copy(struct List* list); //Make copy of list
void shuffle(struct List* list); //Shuffle data in list
void quick_sort(struct List* list); //Quick sort data in list based on memory adresses

//Printing data like C(dungeon) master:
#define print_data(list,index,type_t,format) ({ \
	void* data = get_list(list,index);\
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

//[WARNING] Maxwell revealed programming:

#define init(list,type_size) \
	list = init_list(type_size);\
	\
	\
	void push_##list(void* data)\
	{\
		struct List* list_in_macro_##list = list; \
		push_list(list_in_macro_##list, data);\
	}\
	\
	void pop_##list()\
	{\
		struct List* list_in_macro_##list = list; \
		pop_list(list_in_macro_##list);\
	}\
	\
	void* get_##list(size_t index)\
	{\
		struct List* list_in_macro_##list = list; \
		return get_list(list_in_macro_##list, index);\
	}\
	\
	void insert_##list(void* data, size_t index)\
	{\
		struct List* list_in_macro_##list = list; \
		insert_list(list_in_macro_##list, data, index);\
	}\
	\
	void clear_##list()\
	{\
		struct List* list_in_macro_##list = list; \
		clear_list(list_in_macro_##list);\
	}\
	\
	void del_##list(size_t index)\
	{\
		struct List* list_in_macro_##list = list; \
		del_list(list_in_macro_##list, index);\
	}\
	\
	size_t lenght_##list()\
	{\
		struct List* list_in_macro_##list = list; \
		return lenght_list(list_in_macro_##list);\
	}\
	\
	list->push = push_##list;\
	list->pop = pop_##list;\
	list->get = get_##list;\
	list->insert = insert_##list;\
	list->clear = clear_##list;\
	list->del = del_##list;\
	list->lenght = lenght_##list


#endif
