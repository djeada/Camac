#include "lists.h"

struct List* init_list(size_t type_size)
{
	static size_t ID_counter = 0;
	struct List* list = (struct List*) malloc(sizeof(struct List));

	//Maybe used to distinguish lists in future:
	list->List_ID = ID_counter;
	ID_counter += 1;
	
	list->start = NULL;
	list->end = NULL;
	
	list->num = 0;
	list->size = 0;
	list->type_size = type_size;
	
	return list;
}

void free_list(struct List* list)
{
	if(list->num != 0)
	{
		//Delete all elements
	}

	free(list);
}

//Basic functions:
void push(struct List* list, void* data)
{
	if(NULL == list->start)
	{
		list->start = (struct Container*) malloc(sizeof(struct Container));
		list->start->ptr = malloc(list->type_size);
		list->start->ptr = memcpy(list->start->ptr, data, list->type_size);	
		list->start->next = NULL;
		list->start->prev = NULL;
		
		list->end = list->start;
	}
	else
	{	
		list->end->next = (struct Container*) malloc(sizeof(struct Container));
		list->end->next->ptr = malloc(list->type_size);
		list->end->next->ptr = memcpy(list->end->next->ptr, data, list->type_size);	
		list->end->next->next = NULL;
		list->end->next->prev = list->end;

		list->end = list->end->next; 
	}
	
	list->num++;
	list->size += list->type_size;
}

void pop(struct List* list)
{
	if(NULL != list->end)
	{
		if(list->start == list->end)
		{
			free(list->start->ptr);
			free(list->start);
			list->start = NULL;
			list->end = NULL;
		}
		else
		{
			free(list->end->ptr);
			list->end = list->end->prev;
			free(list->end->next);
			list->end->next = NULL;
		}

		list->num--;
		list->size -= list->type_size;
	}
	else
		perror("No more elements in list!\n");
}

void* get(struct List* list, size_t index)
{
	struct Container* ptr;
	size_t i = 0;

	if(index > list->num || index < 0)
	{
		perror("No such index in list!\n");
		return NULL;
	}

	if(0 == index)
		return list->start->ptr;
	if(list->num-1 == index)
		return list->end->ptr;

	if(index < list->num/2)
	{
		ptr = list->start;
		while(ptr->next != NULL && i != index)
		{
			ptr = ptr->next; 
			i++;
		}
		return ptr->ptr;
	}
	else
	{
		ptr = list->end;
		i = list->num-1;
		while(ptr->prev != NULL && i != index)
		{
			ptr = ptr->prev;
			i--;
		}
		return ptr->ptr;
	}
}

void insert(struct List* list, void* data, size_t index)
{
	struct Container* ptr;
	size_t i = 0;

	if(index > list->num || index < 0)
	{
		perror("No such index in list!\n");
	}
	else if(0 == index)
	{
		ptr = list->start;
		list->start = (struct Container*) malloc(sizeof(struct Container));
		
		list->start->ptr = malloc(list->type_size);
		memcpy(list->start->ptr, data, list->type_size);
		list->start->prev = NULL;
		list->start->next = ptr;
		ptr->prev = list->start;
		list->num++;
		list->size += list->type_size;
	}
	else if(list->num-1 == index)
	{
		ptr = list->end;
		list->end = (struct Container*) malloc(sizeof(struct Container));
		
		list->end->ptr = malloc(list->type_size);
		memcpy(list->end->ptr, data, list->type_size);
		list->end->next = NULL;
		list->end->prev = ptr;
		ptr->next = list->end;
		list->num++;
                list->size += list->type_size;
	}
	else if(index < list->num/2) //Error here wrong index 
	{
		struct Container* prev;
		struct Container* next;
		ptr = list->start;
		while(ptr->next != NULL && i != (index - 1))
		{
			ptr = ptr->next; 
			i++;
		}
		prev = ptr->next->prev;
		next = ptr->next->next;
		
		ptr->next = (struct Container*) malloc(sizeof(struct Container));
		ptr->next->ptr = malloc(list->type_size);
		memcpy(ptr->next->ptr, data, list->type_size);
		ptr->next->next = next;
		ptr->next->prev = prev;

		prev->next = ptr->next;
		next->prev = ptr->next;		

		list->num++;
		list->size += list->type_size;
		
	}
	else
	{
		struct Container* prev;
		struct Container* next;
		ptr = list->end;
		i = list->num-1;
		while(ptr->prev != NULL && i != (index + 1))
		{
			ptr = ptr->prev;
			i--;
		}
		prev = ptr->prev->next;
		next = ptr->prev->prev;

		ptr->prev = (struct Container*) malloc(sizeof(struct Container));
		ptr->prev->ptr = malloc(list->type_size);
		memcpy(ptr->prev->ptr, data, list->type_size);
		ptr->prev->prev = prev;
		ptr->prev->next = next;
		
		prev->prev = ptr->prev;
		prev->next = ptr->next;
		
		list->num++;
		list->size += list->type_size;
		
	}

}

void clear(struct List* list)
{

}

void del(struct List* list, size_t index)
{

}

void lenght(struct List* list)
{

}

void print(struct List* list, size_t index)
{

}

size_t find(struct List* list, void* data)
{
	size_t index = 0;
	return index;
}

//Advanced functions:
struct List* split(struct List* list, float ratio)
{
	struct List* lista2 = NULL;
	return lista2;
}

struct List* copy(struct List* list)
{
	struct List* lista2 = NULL;
	return lista2;

}

void shuffle(struct List* list)
{

}

void quick_sort(struct List* list)
{

}

