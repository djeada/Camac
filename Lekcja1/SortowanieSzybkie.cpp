// SortowanieSzybkie.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <ctime>
#include <cstdlib> 

using namespace std;

void swap(int* a, int* b);
void szybkie(int tab[], int left, int right);
void wypisz(int tab[], int dlugosc);

int main() {
	int tab[100];
	int dlugosc = sizeof(tab) / sizeof(*tab);
	for (int i = 0; i < dlugosc; i++) {
		tab[i] = (rand() % 100) + 1;
	}
	wypisz(tab, 10);
	szybkie(tab, 0, dlugosc - 1);
	wypisz(tab, 10);
	return 0;
}

void swap(int* a, int* b){
	int c = *a;
	*a = *b;
	*b = c;
}

void szybkie(int tab[], int lewy, int prawy) {
	if (lewy < prawy) {
		int srodek = lewy;
		for (int i = lewy + 1; i <= prawy; i++)
			if (tab[i] < tab[lewy])
				swap(tab[++srodek], tab[i]);
		swap(tab[lewy], tab[srodek]);
		szybkie(tab, lewy, srodek - 1);
		szybkie(tab, srodek + 1, prawy);
	}
}

void wypisz(int tab[], int dlugosc) {
	for (int i = 0; i < dlugosc; i++)
		cout << tab[i] << " ";
	cout << endl;
}