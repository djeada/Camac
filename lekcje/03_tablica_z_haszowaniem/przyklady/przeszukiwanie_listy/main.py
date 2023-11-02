def czy_posortowana(lista):
    """Sprawdza, czy lista jest posortowana."""
    return all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1))


def wyszukiwanie_binarne(lista, x):
    """Wyszukiwanie binarne elementu x w liscie."""
    if not czy_posortowana(lista):
        raise ValueError("Lista musi byc posortowana.")

    lewy, prawy = 0, len(lista) - 1

    while lewy <= prawy:
        srodek = (lewy + prawy) // 2
        if x == lista[srodek]:
            return srodek
        elif x < lista[srodek]:
            prawy = srodek - 1
        else:
            lewy = srodek + 1

    return -1


def wyszukiwanie_binarne_rekurencyjnie(lista, lewy, prawy, x):
    """Wyszukiwanie binarne elementu x w liscie, wersja rekurencyjna."""
    if not czy_posortowana(lista):
        raise ValueError("Lista musi byc posortowana.")

    if prawy >= lewy:
        srodek = (lewy + prawy) // 2
        if x == lista[srodek]:
            return srodek
        elif x < lista[srodek]:
            return wyszukiwanie_binarne_rekurencyjnie(lista, lewy, srodek - 1, x)
        else:
            return wyszukiwanie_binarne_rekurencyjnie(lista, srodek + 1, prawy, x)
    else:
        return -1


def wyszukiwanie_liniowe(lista, x):
    """Wyszukiwanie liniowe elementu x w liscie."""
    for i, elem in enumerate(lista):
        if x == elem:
            return i
    return -1


if __name__ == "__main__":
    lista = [3, 8, 12, 14, 15, 19, 21, 22, 30, 53, 68]
    szukane_elementy = [14, 100]

    for elem in szukane_elementy:
        print(f"Wyszukiwanie {elem}:")
        print("Binarne:", wyszukiwanie_binarne(lista, elem))
        print(
            "Binarne (rekurencyjne):",
            wyszukiwanie_binarne_rekurencyjnie(lista, 0, len(lista) - 1, elem),
        )
        print("Liniowe:", wyszukiwanie_liniowe(lista, elem))
        print("-" * 20)
