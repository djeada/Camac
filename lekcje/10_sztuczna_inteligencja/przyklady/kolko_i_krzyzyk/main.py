def ocena(plansza):
    for rzad in range(3):
        if (
            plansza[rzad][0] == plansza[rzad][1] == plansza[rzad][2]
            and plansza[rzad][0] != "-"
        ):
            return 1 if plansza[rzad][0] == "X" else -1

    for kolumna in range(3):
        if (
            plansza[0][kolumna] == plansza[1][kolumna] == plansza[2][kolumna]
            and plansza[0][kolumna] != "-"
        ):
            return 1 if plansza[0][kolumna] == "X" else -1

    if plansza[0][0] == plansza[1][1] == plansza[2][2] and plansza[0][0] != "-":
        return 1 if plansza[0][0] == "X" else -1
    if plansza[0][2] == plansza[1][1] == plansza[2][0] and plansza[0][2] != "-":
        return 1 if plansza[0][2] == "X" else -1

    return 0


def czy_koniec(plansza):
    return ocena(plansza) != 0 or all(
        plansza[i][j] != "-" for i in range(3) for j in range(3)
    )


def minimax(plansza, glebokosc, czy_max_gracz):
    if czy_koniec(plansza) or glebokosc == 0:
        return ocena(plansza)

    if czy_max_gracz:
        max_ocena = -float("inf")
        for i in range(3):
            for j in range(3):
                if plansza[i][j] == "-":
                    plansza[i][j] = "X"
                    ocena = minimax(plansza, glebokosc - 1, False)
                    plansza[i][j] = "-"
                    max_ocena = max(max_ocena, ocena)
        return max_ocena
    else:
        min_ocena = float("inf")
        for i in range(3):
            for j in range(3):
                if plansza[i][j] == "-":
                    plansza[i][j] = "O"
                    ocena = minimax(plansza, glebokosc - 1, True)
                    plansza[i][j] = "-"
                    min_ocena = min(min_ocena, ocena)
        return min_ocena


def najlepszy_ruch(plansza):
    max_ocena = -float("inf")
    ruch = (-1, -1)

    for i in range(3):
        for j in range(3):
            if plansza[i][j] == "-":
                plansza[i][j] = "X"
                ocena = minimax(plansza, 5, False)
                plansza[i][j] = "-"

                if ocena > max_ocena:
                    max_ocena = ocena
                    ruch = (i, j)

    return ruch


# Przykladowa plansza
plansza = [["-", "-", "-"], ["-", "O", "-"], ["-", "-", "-"]]

# Znalezienie najlepszego ruchu
ruch = najlepszy_ruch(plansza)
print("Najlepszy ruch dla gracza X: wiersz =", ruch[0], ", kolumna =", ruch[1])
