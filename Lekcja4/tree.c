#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

struct Tree{
	int wartosc;
	
	struct Tree* R;
	struct Tree* L;
};

struct Tree* init_tree(int var)
{
	struct Tree* t = (struct Tree*) malloc(sizeof(struct Tree));
	t->wartosc = var;
	t->L = NULL;
	t->R = NULL;
	return t;
}

void free_tree(struct Tree* t)
{	
	//Free all elements
	struct Tree* ptr = t;
	struct Tree* ptr_prev = t;
	int last = 0;
        do
        {
                if(ptr->L != NULL)
                {
			ptr_prev = ptr;
                	ptr = ptr->L;
			last = 0;
			continue;
                }
                else if(ptr->R != NULL)
                {
			ptr_prev = ptr;
                	ptr = ptr->R;
			last = 1;
			continue;
                }
		else
		{
			if(ptr == t)
				break;
			if(last ==0)
				ptr_prev->L = NULL;
			else
				ptr_prev->R = NULL;
			free(ptr);
			ptr = t;
		}

        }while(1);

	free(t);
}
	
void dodaj(struct Tree* t, int var)
{
	struct Tree* ptr = t;
	do
	{
		if(ptr->wartosc > var)
		{
			if(ptr->L != NULL)
			{
				ptr = ptr->L;
			}
			else
			{
				ptr->L = init_tree(var);
				break;
			}
		}
		else
		{
			if(ptr->R != NULL)
			{
				ptr = ptr->R;
			}
			else
			{
				ptr->R = init_tree(var);
				break;
			}
		}
	
	}while(1);
}

void wypisz_VLR(struct Tree* t)
{
	if(t != NULL)
	{
		struct Tree* ptr = t;
		printf("%d\n", t->wartosc);
		if(ptr->L != NULL)
		{
			wypisz_VLR(ptr->L);
		}
		if(ptr->R != NULL)
		{
			wypisz_VLR(ptr->R);
		}
	}
}

void wypisz_VRL(struct Tree* t)
{
	if(t != NULL)
	{
		struct Tree* ptr = t;
		printf("%d\n", t->wartosc);
		if(ptr->R != NULL)
		{
			wypisz_VRL(ptr->R);
		}
		if(ptr->L != NULL)
		{
			wypisz_VRL(ptr->L);
		}
	}
}

int main()
{
	struct Tree* root = init_tree(15);
	dodaj(root, 5);
	dodaj(root, 34);
	dodaj(root, 2);
	dodaj(root, 17);
	dodaj(root, 12);
	dodaj(root, 22);
	dodaj(root, 6);
	dodaj(root, 3);
	dodaj(root, 1);

	printf("VLR: \n");
	wypisz_VLR(root);
	printf("VRL: \n");
	wypisz_VRL(root);

	free_tree(root);	
	return 0;
}

