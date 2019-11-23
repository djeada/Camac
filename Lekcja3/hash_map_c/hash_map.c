#include "hash_map.h"

//Initialization and destruction of hash table
struct Hash_map* init_hash_map(size_t type_size, size_t table_size)
{
	struct Hash_map* map = (struct Hash_map*) malloc(sizeof(struct Hash_map));
	map->max_elements = table_size;
	map->num_elements = 0;
	map->table = (struct List**) malloc(sizeof(struct List*)*table_size);
	for(int i=0; i < table_size; i++)
	{
		map->table[i] = NULL;
	}
	return map;
}

void free_hash_map(struct Hash_map* map)
{
	for(int i=0; i < map->max_elements; i++)
	{
		if(NULL != map->table[i])
		{
			free_list(map->table[i]);
		}
	}
	free(map);
}

//Basic functions:
void insert_data(struct Hash_map* h, void* key, size_t key_size, void* data, size_t size)
{
	size_t hash_key = hash_func1(h, key, key_size);
	if(NULL == h->table[hash_key])
	{
		h->table[hash_key] = init_list(size);
	}
	push_list(h->table[hash_key], data);
	//h->table[hash_key]; add ID for elements in list or structure
	h->num_elements++;
}

void* get_data(struct Hash_map* h, void* key, size_t key_size, size_t* size)
{
	void* data;
	size_t hash_key = hash_func1(h, key, key_size);
	if(NULL == h->table[hash_key])
	{
		return NULL;
	}

	size_t elements_list = lenght_list(h->table[hash_key]);
	switch(elements_list)
	{
		case 0:
			return NULL;
		case 1:
			data = get_list(h->table[hash_key], 0);
			*size = h->table[hash_key]->type_size;
			break;
		default:
			perror("Collision! Not implemented jet!");
			//size_t index = find_list(h, );
			return NULL;
	}
		
	return data;
}

size_t delete_data(struct Hash_map* h, void* key, size_t key_size)
{
	size_t hash_key = hash_func1(h, key, key_size);
	if(0 == hash_key)
		return 0;
	if(NULL == h->table[hash_key])
		return 0;

	size_t elements = lenght_list(h->table[hash_key]);
	if(0 != elements)
		clear_list(h->table[hash_key]); //Not good enough!
}

void clear_hash_map(struct Hash_map* h)
{
	for(int i=0; i < h->max_elements; i++)
	{
		if(NULL != h->table[i])
		{
			free_list(h->table[i]);
			h->table[i] = NULL;
		}
	}
}

//Hash functions:
size_t hash_func1(struct Hash_map* h, void* key, size_t key_size)
{
	if(NULL == h)
	{
		return 0;	
	}
	size_t hash = 0;
	size_t max_elements = h->max_elements;
	size_t sum = 0;
	for(int i=0; i < key_size; i++)
	{
		sum += (size_t) ((char*) key)[i];
	}

	hash = sum % max_elements;
	//Add check in hashmap and other functions!

	return hash;
}





