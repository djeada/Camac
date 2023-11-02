class Wezel:
    def __init__(self, klucz):
        self.klucz = klucz
        self.lewy = None
        self.prawy = None
        self.wysokosc = 1


class DrzewoAVL:
    def __init__(self):
        self.korzen = None

    def _wysokosc(self, wezel):
        if not wezel:
            return 0
        return wezel.wysokosc

    def _aktualizuj_wysokosc(self, wezel):
        if wezel:
            wezel.wysokosc = 1 + max(
                self._wysokosc(wezel.lewy), self._wysokosc(wezel.prawy)
            )

    def _rownowaga(self, wezel):
        if not wezel:
            return 0
        return self._wysokosc(wezel.lewy) - self._wysokosc(wezel.prawy)

    def _rotacja_prawo(self, y):
        x = y.lewy
        T = x.prawy
        x.prawy = y
        y.lewy = T
        self._aktualizuj_wysokosc(y)
        self._aktualizuj_wysokosc(x)
        return x

    def _rotacja_lewo(self, x):
        y = x.prawy
        T = y.lewy
        y.lewy = x
        x.prawy = T
        self._aktualizuj_wysokosc(x)
        self._aktualizuj_wysokosc(y)
        return y

    def wstaw(self, klucz):
        if not self.korzen:
            self.korzen = Wezel(klucz)
        else:
            self.korzen = self._wstaw(self.korzen, klucz)

    def _wstaw(self, wezel, klucz):
        if not wezel:
            return Wezel(klucz)

        if klucz < wezel.klucz:
            wezel.lewy = self._wstaw(wezel.lewy, klucz)
        elif klucz > wezel.klucz:
            wezel.prawy = self._wstaw(wezel.prawy, klucz)
        else:
            # duplikaty kluczy nie sa dozwolone
            return wezel

        self._aktualizuj_wysokosc(wezel)
        return self._zbalansuj_wezel(wezel)

    def _zbalansuj_wezel(self, wezel):
        if self._rownowaga(wezel) > 1:
            if self._rownowaga(wezel.lewy) < 0:
                wezel.lewy = self._rotacja_lewo(wezel.lewy)
            wezel = self._rotacja_prawo(wezel)
        elif self._rownowaga(wezel) < -1:
            if self._rownowaga(wezel.prawy) > 0:
                wezel.prawy = self._rotacja_prawo(wezel.prawy)
            wezel = self._rotacja_lewo(wezel)
        return wezel

    def wyswietl(self):
        if not self.korzen:
            print("Drzewo jest puste.")
        else:
            self._inorder(self.korzen)

    def _inorder(self, wezel):
        if wezel:
            self._inorder(wezel.lewy)
            print(wezel.klucz, end=" ")
            self._inorder(wezel.prawy)


# Przykladowe uzycie:
if __name__ == "__main__":
    drzewo = DrzewoAVL()
    drzewo.wstaw(9)
    drzewo.wstaw(5)
    drzewo.wstaw(10)
    drzewo.wstaw(0)
    drzewo.wstaw(6)
    drzewo.wstaw(11)
    drzewo.wstaw(-1)
    drzewo.wstaw(1)
    drzewo.wstaw(2)

    print("Inorder:")
    drzewo.wyswietl()
