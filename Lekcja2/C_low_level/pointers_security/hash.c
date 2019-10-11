#include "hash.h"

char* get_random_hash512(void)
{
	FILE *output;
	char data_file_name[9] = {"data.tmp\0"};
	char exec_buf[128] = {0};
	size_t seed = 10000;

	char *hash = (char*) malloc(sizeof(char)*128);
	int i;

	random_file(data_file_name, seed);
	sprintf(exec_buf, "sha512sum %s\n", data_file_name);
	output = popen(exec_buf, "r");
	for(i=0; i < 128; i++)
	{
		hash[i] = (char) fgetc(output);
	}
	pclose(output);
	remove(data_file_name);
	return hash;
}

void get_hash(char* text, char* hash)
{
	FILE* output;
	char data_file_name[9] = {"data.tmp\0"};
	char exec_buf[128] = {0};
	size_t seed = 10000;

	int i;

	FILE* fd = fopen(data_file_name, "w");
	fprintf(fd, "%s", text);
	fflush(fd);
	fclose(fd);
	sprintf(exec_buf, "sha512sum %s\n", data_file_name);
	output = popen(exec_buf, "r");
	for(i=0; i < 128; i++)
	{
		hash[i] = (char) fgetc(output);
	}
	pclose(output);
	remove(data_file_name);
}

void random_file(char *name, size_t size)
{
	FILE *fd;
	int i;
	char rand_byte;

	srand(time(NULL));
	fd = fopen(name, "wb");
	for(i=0; i < size; i++)
	{
		rand_byte = (char) random();
		fwrite(&rand_byte, sizeof(char), 1, fd);
	}
	fclose(fd);
}

void crypt_hash(char* data_ptr, size_t data_len, char* hash)
{
	int i, j;
	for(i=0,j=0; i < data_len; i++, j++)
	{
		if(j > 128)
			j=0;
		*data_ptr ^= hash[j];
		data_ptr++;
	}
	free(hash);
}

void decrypt_hash(char* data_ptr, size_t data_len, char* hash)
{
	int i, j;
        for(i=0,j=0; i < data_len; i++, j++)
        {
		if(j > 128)
                        j=0;
                *data_ptr ^= hash[j];
		data_ptr++;
        }
	free(hash);
}
