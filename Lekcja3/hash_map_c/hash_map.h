#ifndef _HASH_MAP_NORMAL_H_
#define _HASH_MAP_NORMAL_H_
/*
	"Taa z robotami odrazu..." - Maxwell, 22.11.2019/22:15
	General data type hash map for other projects.
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#include "lists.h" 

struct Hash_map{
	size_t max_elements;
	size_t num_elements;

	struct List** table;
};

//Initialization and destruction of hash table
struct Hash_map* init_hash_map(size_t type_size, size_t table_size);
void free_hash_map(struct Hash_map* map);

//Basic functions:
void insert_data(struct Hash_map* h, void* key, size_t key_size, void* data, size_t size);
void* get_data(struct Hash_map* h, void* key, size_t key_size, size_t* size);
size_t delete_data(struct Hash_map* h, void* key, size_t key_size);
void clear_hash_map(struct Hash_map* h);

//Hash functions:
size_t hash_func1(struct Hash_map* h, void* key, size_t key_size);

#endif
