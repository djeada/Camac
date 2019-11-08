class Wezel():
    def __init__(self, dane = None):
        self.dane = dane
        self.lewy = None
        self.prawy = None
        self.rodzic = None
        self.wysokosc = 1

    def liczba_dzieci():
	n = 0
	if self.lewy!=None:
            n+=1
        if self.prawy!=None:
            n+=1
        return n

    def minimum():
        if self.lewy:
            return self.lewy
        return self

class drzewoAVL:
    def __init__(self):
	    self.korzen = None

    def dodaj(self, dane):
        if self.korzen.dane == None:
            self.korzen.dane = dane
        else:
            def dodaj_do_wierzcholka(wierzcholek, dane):
                if dane < wierzcholek.dane:
                    if wierzcholek.lewy == None:
                        wierzcholek.lewy = Wezel(dane)
                        wierzcholek.lewy.rodzic=wierzcholek
			self._inspect_insertion(wierzcholek.lewy)
                    else:
                        dodaj_do_wierzcholka(wierzcholek.lewy, dane)
                elif dane > wierzcholek.dane:
                    if wierzcholek.prawy == None:
                        wierzcholek.prawy = Wezel(dane)
                        wierzcholek.prawy.rodzic=wierzcholek
			self._inspect_insertion(wierzcholek.lewy)
                    else:
                        dodaj_do_wierzcholka(wierzcholek.prawy, dane)
            dodaj_do_wierzcholka(self.korzen, dane)


    def sciezka(self, x):
        def _sciezka(wierzcholek, x, l=[]):
            if not wierzcholek:
                return []
            if wierzcholek.dane == x:
                return [wierzcholek.dane]
            res = _sciezka(wierzcholek.lewy, x)
            if res:
                return [wierzcholek.dane] + res
            res = _sciezka(wierzcholek.prawy, x)
            if res:
                return [wierzcholek.dane] + res
            return []
        return _sciezka(self.korzen, x)

    def usun(self,x):
        wierzcholek = self.wyszukaj(x)
        rodzic = wierzcholek.rodzic

        n = wierzcholek.liczba_dzieci()

	if n == 0:
            if rodzic:
		if rodzic.lewy == wierzcholek:
                    rodzic.lewy = None
		else:
                    rodzic.prawy = None
	    else:
		self.korzen=None

        if n == 1:
	    if wierzcholek.lewy:
		dziecko = wierzcholek.lewy
	    else:
		dziecko = wierzcholek.prawy

	    if rodzic:
		if rodzic.lewy == wierzcholek:
                    rodzic.lewy = dziecko
		else:
                    rodzic.prawy = dziecko
	    else:
		self.korzen = dziecko

	    dziecko.rodzic = rodzic

        if n == 2:
            nastepca = wierzcholek.minimum()
            wierzcholek.dane = nastepca.dane
            self.usun(nastpeca.dane)
            return

        if rodzic:
            rodzic.wysokosc = 1+max(rodzic.lewy.wysokosc,rodzic.prawy.wysokosc)
	    self._inspect_deletion(node_parent)

    def wyszukaj(self, dane):
        if self.korzen.dane == dane:
            return self.korzen        
            def wyszukaj_wierzcholek(wierzcholek, dane):
                if wierzcholek:
                if wierzcholek.dane:
                    if wierzcholek.dane == dane:
                        return wierzcholek
                    elif dane < wierzcholek.dane:
                        return wyszukaj_wierzcholek(wierzcholek.lewy, dane)
                    else:
                        return wyszukaj_wierzcholek(wierzcholek.prawy, dane)
        return wyszukaj_wierzcholek(self.korzen,dane)

    def zbadajWstawienie(self,wierzcholek,sciezka=[]):
	if wierzcholek.rodzic:
	    sciezka += [wierzcholek]

            lewy_wysokosc = wierzcholek.rodzic.lewy.wysokosc
	    prawy_wysokosc = wierzcholek.rodzic.prawy.wysokosc

	    if abs(lewy_wysokosc - prawy_wysokosc) > 1:
                sciezka += [wierzcholek.rodzic]

		self.balansuj(sciezka[0],sciezka[1],sciezka[2])
		return

	    nowa_wysokosc = 1 + wierzcholek.wysokosc 
	    if nowa_wysokosc > wierzcholek.rodzic.wysokosc:
                wierzcholek.rodzic.wysokosc = nowa_wysokosc

	    self.zbadajWstawienie(wierzcholek.rodzic,sciezka)

    def zbadajUsuniecie(self,wierzcholek):
	if wierzcholek:
	    lewy_wysokosc = wierzcholek.lewy.wysokosc
	    prawy_wysokosc = wierzcholek.prawy.wysokosc

	    if abs(lewy_wysokosc - prawy_wysokosc) > 1:
		    y = self.wyzszeDziecko(wierzcholek)
		    x = self.wyzszeDziecko(y)
		    self.balansuj(wierzcholek,y,x)

	self.zbadajUsuniecie(wierzcholek.rodzic)

    def balansuj(self,z,y,x):
	if y == z.lewy and x == y.lewy:
	    self.rotacjaNaPrawo(z)
	elif y == z.lewy and x == y.prawy:
	    self.rotacjaNaLewo(y)
	    self.rotacjaNaPrawo(z)
	elif y == z.prawy and x == y.prawy:
	    self.rotacjaNaLewo(z)
	elif y == z.prawy and x == y.lewy:
	    self.rotacjaNaPrawo(y)
	    self.rotacjaNaLewo(z)

    def rotacjaNaPrawo(self,z):
	sub_korzen = z.rodzic 
	y = z.lewy
	t3 = y.prawy
	y.prawy = z
	z.rodzic = y
	z.lewy = t3
	if t3:
            t3.rodzic = z
	y.rodzic = sub_korzen
	if not y.rodzic:
	    self.korzen = y
	else:
	    if y.rodzic.lewy == z:
		y.rodzic.lewy = y
	    else:
		y.rodzic.prawy = y		
		z.wysokosc = 1 + max(z.lewy.wysokosc,z.prawy.wysokosc)
		y.wysokosc = 1 + max(y.lewy.wysokosc,y.prawy.wysokosc)

    def rotacjaNaLewo(self,z):
        sub_korzen = z.rodzic 
	y = z.prawy
	t3 = y.lewy
	y.lewy = z
	z.rodzic = y
	z.prawy = t3
	if t3:
            t3.rodzic = z
	y.rodzic = sub_korzen
	if not y.rodzic:
	    self.korzen = y
	else:
	    if y.rodzic.lewy == z:
		y.rodzic.lewy = y
	    else:
		y.rodzic.prawy = y		
		z.wysokosc = 1 + max(z.lewy.wysokosc,z.prawy.wysokosc)
		y.wysokosc = 1 + max(y.lewy.wysokosc,y.prawy.wysokosc)
		
    def wyzszeDziecko(self, wierzcholek):
	lewy_wysokosc = wierzcholek.lewy.wysokosc
	prawy_wysokosc = wierzcholek.prawy.wysokosc
	if lewy_wysokosc >= prawy_wysokosc:
            return wierzcholek.lewy
        return wierzcholek.prawy
