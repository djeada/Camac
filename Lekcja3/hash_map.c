#include "hash_map.h"

struct Hash_Map* init_hashmap(size_t max_keys)
{
	struct Hash_Map* map = (struct Hash_Map*) malloc(sizeof(struct Hash_Map));
	
	map->size = 0;
	map->num = 0;
	map->min_address = NULL;
	map->max_address = NULL;
	
	map->max_keys = max_keys; 
	map->key_words = (size_t*) malloc(sizeof(size_t) * max_keys);
	
	return map;
}

void free_hashmap(struct Hash_Map* map)
{
	//Rest of the shit...
	

	free(map->key_words);
	free(map);
}

void* insert_hashmap(struct Hash_Map* map, void* data, size_t size)
{
	
}

size_t hash_function_01(void* data, size_t size)
{
	size_t hash;

	
	
}

