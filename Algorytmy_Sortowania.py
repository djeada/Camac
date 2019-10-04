import random
import time

def sortowanie_babelkowe(tablica):
    for i in range(len(tablica)):
        for j in range(len(tablica)):
            if tablica[i] > tablica[j]:
                swap(i, j, tablica)

def znajdzMin(tablica):
    minimum = tablica[0]
    indeks = 0
    for i in range(1,len(tablica)):
        if tablica[i] < minimum:
            minimum = tablica[i]
            indeks = i
    return indeks

def przez_wybieranie(tablica):
    for i in range(len(tablica)):
        indeks = znajdzMin(tablica[i:len(tablica)]) + i
        swap(i,indeks,tablica)

def sortowanie_szybkie(tablica):
    if len(tablica) > 1:
        return sortowanie_szybkie([x for x in tablica[1:] if x < tablica[0]]) + [x for x in tablica if x == tablica[0]] + sortowanie_szybkie([x for x in tablica[1:] if x > tablica[0]])
    else:
        return tablica
    
def swap(i,j, tablica):
    temp = tablica[i]
    tablica[i] = tablica[j]
    tablica[j] = temp

tab = [[],[],[]]
czas = []

for i in range(10000):
    losowa = random.randint(0,10000)
    tab[0].append(losowa)
    tab[1].append(losowa)
    tab[2].append(losowa)


start_time = time.time()
sortowanie_babelkowe(tab[0])
czas.append(time.time() - start_time)

start_time = time.time()
przez_wybieranie(tab[1])
czas.append(time.time() - start_time)

start_time = time.time()
tab = sortowanie_szybkie(tab[2])
czas.append(time.time() - start_time)

print(czas)
