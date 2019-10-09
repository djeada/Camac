#include <stdio.h>
#include <unistd.h>
#include <time.h>
#include <stdlib.h>
#include <sys/ioctl.h>
#include <string.h>

#define NUMBER_MAX 10000
#define SORTING_ALGORITHMS 2

void swap(int* a, int* b)
{
	int c = *a;
	*a = *b;
	*b = c;
}	 

void buble_sort(int* tab, int size)
{
	int i, j;
	int buf;
	for(i = 0;i < size; i++)
	{
		for(j = 0; j < size; j++)
		{
			if( tab[i] < tab[j] )
			{
				buf = tab[i];
				tab[i] = tab[j];
				tab[j] = buf; 
			}
		}
	}
}

int find_minimum(int* tab, int size)
{
	int i, min = tab[0];
	for(i=0; i < size; i++)
		min = min > tab[i] ? tab[i] : min;
	return min;
}

int* find_minimum_ptr(int* tab, int size)
{
	int* pointer = tab;
	int i;
	for(i=0; i < size; i++)
		pointer = *pointer > tab[i] ? &tab[i] : pointer;
	return pointer;
}

void selection_sort_mem(int* tab, int size)
{
	int i;
	int* ptr;
	
	for(i=0; i < size; i++)
	{
		ptr = find_minimum_ptr(tab, size-i);
		swap(tab++, ptr);
	}
}

/*
inline int compare_int (int* a, int* b)
{
	if(*a > *b)
		return 1;
	else if (*a < *b)
		return -1;
	else
		return 0;
}

void quick_sort(int* tab, int size)
{
	int i;
	
}
*/

void random_numbers(int* tab, int size, int max_num)
{
	int i = 0;
	for(i=0; i < size; i++)
	{
		tab[i] = rand() % max_num;
	}
}

void print_tab(int* tab, int size)
{
	int i = 0;
	for(i; i < size; i++)
	{
		printf("%d\n", tab[i]);
	}	
}

void print_tab2(int* tab, int size, int max_in_line)
{
	int i = 0;
	int symbols=0;
	for(i; i < size; symbols > max_in_line - 4 ? putchar('\n'), symbols = 0, i++ : i++)
	{
		symbols += printf("%d ", tab[i]);	
	}
}

void draw_line(const char* title, char c, int width)
{
	int i=0;
	int title_width = strlen(title);
	int half_line = (width-title_width)/2;
	putchar('\n');
	for(i=0; i < half_line; i++ )
		putchar(c);
	printf("%s", title);
	for(i=0; i < half_line; i++ )
		putchar(c);
	putchar('\n');
}
	
int main(void)
{
	//FEGELEIN! FEGELEIN! - "Dolfy, Der Untergang" 	
	void (*func_ptr[SORTING_ALGORITHMS])(int*, int) = {buble_sort, selection_sort_mem};

	//Extra small trick: (getting window width and height)
	struct winsize w;
	ioctl(STDOUT_FILENO, TIOCGWINSZ, &w);
	
	//Visuals
	char buf_title[32];

	//Data for time stamping:
	struct timespec start_time, end_time;
	srand(time(NULL));
	long int num_sec[SORTING_ALGORITHMS] = {0,0};
	long int num_nsec[SORTING_ALGORITHMS] = {0,0};

	
	//Data table:
	int tab[NUMBER_MAX];
	
	int i;
	for(i=0; i < SORTING_ALGORITHMS; i++)
	{
		sprintf(buf_title, "Losowe dane nr:%d", i+1);	
		draw_line(buf_title, '#', w.ws_col);
		
		//Random numbers generation
		random_numbers(tab, NUMBER_MAX, 100);
		print_tab2(tab, NUMBER_MAX, w.ws_col);
	
		sprintf(buf_title, "Algorytm pod funkcją ptr:%p", func_ptr[i]);	
		draw_line(buf_title, '#', w.ws_col);

		//First time stamp
		clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &start_time);
		
		func_ptr[i](tab, NUMBER_MAX);
	
		//Second time stamp
		clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &end_time);

		print_tab2(tab, NUMBER_MAX, w.ws_col);

		num_sec[i] = end_time.tv_sec - start_time.tv_sec;
		num_nsec[i] = end_time.tv_nsec - start_time.tv_nsec;
	}

	putchar('\n');
	for(i=0; i < SORTING_ALGORITHMS; i++)
	{
		printf("Funkcja ptr:%p - Czas sortowania: %ld sekund %ld nanosekundy!\n", func_ptr[i], num_sec[i], num_nsec[i]);
	}
	return 0;
}
