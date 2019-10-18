
def wyszukiwanie_binarne(lista, x):
    lewy = 0
    prawy = len(lista) - 1
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

def wyszukiwanie_liniowe(lista, x):
    for i in range(len(lista)):
        if x == lista[i]:
            return i
    return -1    

lista = [3, 8, 12, 14, 15, 19, 21, 22, 30, 53, 68]
print(wyszukiwanie_binarne(lista, 14))
print(wyszukiwanie_binarne(lista, 100))
print(wyszukiwanie_liniowe(lista, 14))
print(wyszukiwanie_liniowe(lista, 100))

