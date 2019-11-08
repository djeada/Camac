def generuj_krawedzie(graf):
    krawedzie = []
    for wierzcholek in graf:
        for sasiad in graf[wierzcholek]:
            krawedzie.append((wierzcholek,sasiad))
    return krawedzie

def znajdzSciezke(graf, start, koniec, sciezka=[]):
    if start in graf and koniec in graf:
        sciezka += [start]
        if start == koniec:
            return sciezka
        for sasiad in graf[start]:
            if sasiad not in sciezka:
                nowa_sciezka = znajdzSciezke(graf, sasiad, koniec, sciezka)
                if nowa_sciezka:
                    return sciezka

def najkrotszaSciezka(graf, start, koniec, sciezka=[]):
    if start in graf and koniec in graf:
        sciezka += [start]
        if start == koniec:
            return sciezka
        najkrotsza = None
        for sasiad in graf[start]:
            if sasiad not in sciezka:
                nowa_sciezka = najkrotszaSciezka(graf, sasiad, koniec, sciezka)
                if nowa_sciezka:
                    if not najkrotsza:
                        najkrotsza = nowa_sciezka
                    elif len(najkrotsza) > len(nowa_sciezka):
                        najkrotsza = nowa_sciezka
        return najkrotsza

def wszystkieSciezki(graf, start, koniec, sciezka=[]):
    if start in graf and koniec in graf:
        sciezka += [start]
        if start == koniec:
            return sciezka
        znalezione = []
        for sasiad in graf[start]:
            if sasiad not in sciezka:
                nowa_sciezka = wszystkieSciezki(graf, sasiad, koniec, sciezka)
                if nowa_sciezka and not nowa_sciezka in znalezione:
                    znalezione.append(nowa_sciezka)
        return znalezione

def czyPetla(graf,wierzcholek):
    for sasiad in graf[wierzcholek]:
        if sasaid == wierzcholek:
            return True
    return False

def znajdzIzolowaneWierzcholki(graf):
    izolowane = []
    for wierzcholek in graf:
        if not graf[wierzcholek]:
            izolowane.append(wierzcholek)
    return izolowane

def dodajKrawedz(graf, start, koniec):
    if start in graf:
        graf[start].append(koniec)
    else:
        graf[start] = [koniec]

def stopienWierzcholka(graf, wierzcholek):
    return len(graf[wierzcholek])

def czySpojny(graf):
    for x in graf:
        if not graf[x]:
            return False
    return True

graf = {
    'A' : ['A', 'B', 'C'],
    'B' : ['C', 'D'],
    'C' : ['D'],
    'D' : ['C'],
    'E' : ['F'],
    'F' : ['C'],
    'G' : [],
    'P' : []
}
