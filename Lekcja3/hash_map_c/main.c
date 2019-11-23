#include <stdio.h>

#include "hash_map.h"

int main(void)
{
	struct Hash_map* map = init_hash_map(sizeof(char)*256, 1000);
	char key1[16] = {"Placki2451Andrze"};
	char data[256] = {"Andrzej to bardzo miły człowiek i wgl. Ale nie ma baby..."};
	data[255] = '\0';
	printf("Key for this data: %s\n", key1);
	printf("Hash generated: %ld\n", hash_func1(map, key1, 16));
	insert_data(map, key1, 16, (void*) data, 256);

	size_t data_size = 0;
	printf("Data in hash map: %s\n", (char*) get_data(map, key1, 16, &data_size));
	printf("Have %ld bytes\n", data_size);
	free_hash_map(map);
	return 0;
}
