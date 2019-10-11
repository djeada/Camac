#pragma once

#include <stdio.h>
#include <unistd.h>
#include <time.h>
#include <stdlib.h>


char* get_random_hash512(void);
void get_hash(char* text, char* hash);
void random_file(char *name, size_t size);
void crypt_hash(char* data_ptr, size_t data_len, char* hash);
void decrypt_hash(char* data_ptr, size_t data_len, char* hash);

