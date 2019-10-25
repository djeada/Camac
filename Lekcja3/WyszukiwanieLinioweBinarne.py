
def wyszukiwanie_binarne(lista, x):
    lewy = 0
    prawy = len(lista)
    while lewy < prawy:
        srodek = int((lewy + prawy)/2)
        if x == lista[srodek]:
            return srodek
        else:
            if x < lista[srodek]:
                prawy = srodek - 1
            else:
                lewy = srodek + 1
    return -1

def wyszukiwanie_binarne_rekurencyjnie(lista, lewy, prawy, x):
    if prawy < lewy:
            return -1
    srodek = int((lewy + prawy)/2)
    if x == lista[srodek]:
            return srodek
    else:
        if x < lista[srodek]:
            return wyszukiwanie_binarne_rekurencyjnie(lista, lewy, srodek - 1, x)  
        else:
            return wyszukiwanie_binarne_rekurencyjnie(lista, srodek + 1, prawy, x)

def wyszukiwanie_liniowe(lista, x):
    for i in range(len(lista)):
        if x == lista[i]:
            return i
    return -1    

lista = [3, 8, 12, 14, 15, 19, 21, 22, 30, 53, 68]
print(wyszukiwanie_binarne(lista, 14))
print(wyszukiwanie_binarne(lista, 100))
print(wyszukiwanie_binarne_rekurencyjnie(lista, 0, len(lista)-1, 14))
print(wyszukiwanie_binarne_rekurencyjnie(lista, 0, len(lista)-1, 100))
print(wyszukiwanie_liniowe(lista, 14))
print(wyszukiwanie_liniowe(lista, 100))

