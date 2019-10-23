#ifndef _HASH_MAP_
#define _HASH_MAP_

/*
	If this works I am not that crappy programmer I was thinking I am.
	- Maxwell, 23.10.2019/21:29
	General data type hash map for other projects.
*/

struct Hashed_data{
	size_t hash_ID; //Calculated based on stored data;
	size_t size;
	void* data;
};

//General info structure: 
struct Hash_Map{
	size_t size;
	size_t num;

	void* min_address;
	void* max_address;

	size_t* key_words;
	size_t max_keys; 	
}; 

struct Hash_Map* init_hashmap(size_t max_keys);
void free_hashmap(struct Hash_Map* map);

void* insert_hashmap(struct Hash_Map* map, void* data, size_t size);

size_t hash_function_01(void* data, size_t size);
#endif

