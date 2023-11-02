class Wezel:
    def __init__(self, klucz):
        self.klucz = klucz
        self.lewe = None
        self.prawe = None


class DrzewoBinarne:
    def __init__(self):
        self.korzen = None

    def dodaj(self, klucz):
        if self.korzen is None:
            self.korzen = Wezel(klucz)
        else:
            self._dodaj(klucz, self.korzen)

    def _dodaj(self, klucz, wezel):
        if klucz < wezel.klucz:
            if wezel.lewe is None:
                wezel.lewe = Wezel(klucz)
            else:
                self._dodaj(klucz, wezel.lewe)
        else:
            if wezel.prawe is None:
                wezel.prawe = Wezel(klucz)
            else:
                self._dodaj(klucz, wezel.prawe)

    def wyswietl(self):
        if self.korzen is not None:
            self._wyswietl(self.korzen)

    def _wyswietl(self, wezel):
        if wezel is not None:
            self._wyswietl(wezel.lewe)
            print(str(wezel.klucz) + " ", end="")
            self._wyswietl(wezel.prawe)


# Przyklad uzycia
if __name__ == "__main__":
    drzewo = DrzewoBinarne()
    drzewo.dodaj(10)
    drzewo.dodaj(5)
    drzewo.dodaj(15)
    drzewo.dodaj(2)
    drzewo.dodaj(7)

    print("Elementy drzewa binarnego (w porzadku rosnacym):")
    drzewo.wyswietl()
