#include <stdio.h>
#include <x86intrin.h>
#include <time.h>
#include <stdlib.h>
#include <unistd.h>

//#define VERBOSE

#define MAX_DATA 1048

void randomize(int* vec, size_t size)
{
	for(size_t i=0; i < size; i++)
	{
		vec[i] = rand()%1000;
	}
}

void add_normal(int* vec1, int* vec2, size_t size)
{
	for(size_t i=0; i<size; i++)
	{
		vec1[i] += vec2[i];  
	}
}

//In this particular case it is not big deal but shows how it works
void add_powerfull(int* vec1, int* vec2, size_t size)
{
	__m256i data_in1;
	__m256i data_in2;
	__m256i data_out;
	int out;

	for(size_t i=0; i<size; i+=8)
	{
		data_in1 = _mm256_set_epi32(vec1[i+0], vec1[i+1], vec1[i+2], vec1[i+3], vec1[i+4], vec1[i+5], vec1[i+6], vec1[i+7]);
		data_in2 = _mm256_set_epi32(vec2[i], vec2[i+1], vec2[i+2], vec2[i+3], vec2[i+4], vec2[i+5], vec2[i+6], vec2[i+7]);
		data_out = _mm256_add_epi32(data_in1, data_in2);

		vec1[i+0] = ((int*)&data_out)[0];
		vec1[i+1] = ((int*)&data_out)[1];
		vec1[i+2] = ((int*)&data_out)[2];
		vec1[i+3] = ((int*)&data_out)[3];
		vec1[i+4] = ((int*)&data_out)[4];
		vec1[i+5] = ((int*)&data_out)[5];
		vec1[i+6] = ((int*)&data_out)[6];
		vec1[i+7] = ((int*)&data_out)[7];

	}
}

void print_data(int* vec, size_t size)
{
	for(size_t i=0; i < size; i++)
		printf("%d ",vec[i]);
	putchar('\n');
}

int main()
{
	struct timespec start_time, end_time;
        srand(time(NULL));
	
	int a[MAX_DATA] = {0};
	int b[MAX_DATA] = {0};

	//Randomize data:
	randomize(a, MAX_DATA);
	randomize(b, MAX_DATA);

	#ifdef VERBOSE
		printf("Data in a:\n");
		print_data(a, MAX_DATA);
		printf("Data in b:\n");
		print_data(b, MAX_DATA);
	#endif

	//Normal solution:
	add_normal(a, b, MAX_DATA);
	
	#ifdef VERBOSE
		printf("After add() data in a:\n");
		print_data(a, MAX_DATA);
	#endif
	
	randomize(a, MAX_DATA);
	randomize(b, MAX_DATA);
	
	#ifdef VERBOSE
		printf("\nUsing AVX2!\nData in a:\n");
		print_data(a, MAX_DATA);
		printf("Data in b:\n");
		print_data(b, MAX_DATA);
	#endif

	//Hardcore version:
	add_powerfull(a, b, MAX_DATA);

	#ifdef VERBOSE
		printf("After add() data in a:\n");
		print_data(a, MAX_DATA);
	#endif
	

	return 0;
}
