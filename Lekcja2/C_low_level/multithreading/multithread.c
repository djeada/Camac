#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>

#include <gsl/gsl_sf_bessel.h>

#define NUM_THREADS 8

struct Args args;
pthread_t threads[NUM_THREADS];
pthread_attr_t attr;
//pthread_mutex_t mutexcreate;

struct Args{
	long int thread_num;
	int mass;
	int planck;
	int n;
	int m;
	double** matrix;
};

void* Calculate_Matrix(void* num){
	int my_num = *((int*) num);

	printf("It's thread: %d!\n", my_num);

	int table_beg = 0;				//Begining adress
	int table_part_size = args.n / NUM_THREADS;	//Sizeof block in matrix
	if(args.n % NUM_THREADS != 0 && my_num == 0){
		table_part_size += args.n % NUM_THREADS;
	}
	else{
		table_beg = 0 + my_num*table_part_size;
		table_beg += args.n % NUM_THREADS;
	}
	
	printf("Thread #%d: Procesing table part %d-%d\n", my_num, table_beg, table_beg + table_part_size);
	//Place for calculations:
	int i, j;
	for(i=table_beg; i < table_beg+table_part_size; i++){
		for(j=0; j < args.m; j++){
			args.matrix[i][j] = j + i*args.m + 1;
		}
	}

	pthread_exit(NULL);
}	

int create_Matrix(struct Args* problem, int n, int m){
	problem->n = 0;
	problem->m = 0;

	problem->matrix = (double**) malloc(n*sizeof(double*));
	if(problem->matrix == NULL){
		perror("[ERROR] In function create_Matrix when allocating memory for n rows\n");
		return -1;
	}

	int i;
	int j;
	for(i=0; i < n; i++){
		problem->matrix[i] = (double*) malloc(m*sizeof(double));
		if(NULL == problem->matrix[i]){
			perror("[ERROR] In function create_Matrix when allocating memory for m colums\n");
			break;
		}
		for(j=0; j < m; j++ ){
			problem->matrix[i][j] = 0;
		}
	}

	if(i < n){
		perror("[ERROR] In create_Matrix(), not all of arrays are allocated\n");
		int j;
		for(j=i; j != 0; j--){
			free(problem->matrix[j]);
		}
		free(problem->matrix);
		return -1;
	}
	problem->n = n;
	problem->m = m;

	return 0;
};

int delete_Matrix(struct Args* problem){
	int i;
	if(NULL == problem->matrix){
		perror("[WARRNING] In delete_Matrix(), there is no memory allocated under this address\n");
		return -1;
	}
	
	for(i=0; i < problem->n; i++){
		if(problem->matrix[i] != NULL){
			free(problem->matrix[i]);
			problem->matrix[i] = NULL;
		}	
	}
	
	free(problem->matrix);
	problem->matrix = NULL;
	problem->n = 0;
	problem->m = 0;
	return 0;
}

void print_Matrix(struct Args *problem){
	if(problem->n == 0 || problem->m == 0)
		printf("There is no matrix!\n");
	else{
		printf("Matrix is %d x %d size.\n", problem->n, problem->m);
		int i, j;
		for(i=0; i < problem->n; i++){
			printf("Clumn %d data:\n", i+1);
			for(j=0; j < problem->m; j++){
				printf("%lf\t", problem->matrix[i][j]);
			}
			putchar('\n');
		}
	}
}

void print_partof_Matrix(struct Args *problem, int n_beg, int n_end, int m_beg, int m_end){
	if(problem->n == 0 || problem->m == 0)
                printf("There is no matrix!\n");
	else{
		if((n_beg <= problem->n && n_beg >= 0 && n_end >= n_beg) && (m_beg <= problem->m && m_beg >= 0 && m_end >= m_beg)){
			printf("Part of Martix begining at (n=%d, m=%d) and ending at (n=%d, m=%d)\n",n_beg, m_beg, n_end, m_end);
			puts("Have following values: ");
			int i, j;
			for(i=n_beg; i < n_end; i++){
				printf("Column %d:\n", i);
				for(j=m_beg; j < m_end; j++){
					printf("%lf\t", problem->matrix[i][j]);
				}
				putchar('\n');
			}
		
		}
		else{
			printf("Cannot print that matrix!\n");
		}
		
		
	}
}

int main(){

	int rc;
	int ret = create_Matrix(&args, 55500, 55500);	
	if(ret != 0){
		perror("In main(), no matrix!");
		exit(-1);
	}
	//print_Matrix(&args);

	int thread_numbers[NUM_THREADS];
	pthread_attr_init(&attr);
    	pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);

	int i;	
	for(i=0; i<NUM_THREADS; i++){
		printf("In main: creating thread %ld\n", args.thread_num);
		thread_numbers[i]=i;
		rc = pthread_create(&threads[args.thread_num], &attr, Calculate_Matrix, (void*) &thread_numbers[i]);
		args.thread_num++;
		if(rc){
			printf("ERROR: return code from pthread_create() is %d\n", rc);
			exit(-1);
		}
			
	}

	//print_Matrix(&args);
	//print_partof_Matrix(&args, 20000, 20010, 130, 200);
	void* status;
	pthread_attr_destroy(&attr);
	for(i=0; i < NUM_THREADS; i++) {
       		rc = pthread_join(threads[i], &status);
       		if (rc) {
          		printf("ERROR; return code from pthread_join() is %d\n", rc);
          		exit(-1);
          	}
       		printf("Main: completed join with thread %d having a status of %ld\n",i,(long)status);
	}
	print_partof_Matrix(&args, 20000, 20010, 130, 200);
	delete_Matrix(&args);

	pthread_exit(NULL);
}


