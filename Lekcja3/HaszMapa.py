import random

class HashMap:
    def __init__(self, rozmiar=10):
        self.rozmiar = rozmiar
        self.tablica = [None] * self.rozmiar

    def transformacja_kluczowa(self, klucz):
        hash = 0
        for c in str(klucz):
            hash += ord(c)
        return hash % self.rozmiar
    
    def dodaj(self, klucz, value):
        klucz_hash = self.transformacja_kluczowa(klucz)
        klucz_value = [klucz, value]

        if self.tablica[klucz_hash] is None:
            self.tablica[klucz_hash] = list([klucz_value])
            return
        else:
            for para in self.tablica[klucz_hash]:
                if para[0] == klucz:
                    para[1] = value
                    return
                self.tablica[klucz_hash].append(klucz_value)
                return

    def pobierz(self, klucz):
        klucz_hash = self.transformacja_kluczowa(klucz)
        if self.tablica[klucz_hash] is not None:
            for para in self.tablica[klucz_hash]:
                if para[0] == klucz:
                    return para[1]
        return None

    def delete(self, klucz):
        klucz_hash = self.transformacja_kluczowa(klucz)

        if self.tablica[klucz_hash] is None:
            return False
        for i in range(0, len(self.tablica[klucz_hash])):
            if self.tablica[klucz_hash][i][0] == klucz:
                self.tablica[klucz_hash].pop(i)
                return True
            
    def print(self):
        for item in self.tablica:
            if item:
                for x in item:
                    print(x[0], ' : ', x[1])

h = HashMap(12)
h.dodaj('Bob', '31232')
h.dodaj('Adam', '31232')
h.dodaj('Kaczka', '31232')
h.dodaj('Maxwell', '31232')
h.dodaj('Adamko', '31232')
h.dodaj('Sramzes', '31232')
h.dodaj('Faraon', '31232')

h.print()
