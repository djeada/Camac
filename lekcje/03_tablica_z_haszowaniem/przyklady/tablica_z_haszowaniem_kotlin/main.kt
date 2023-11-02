data class HashElement(val klucz: String, var wartosc: String)

class HashTabela {
    private val rozmiar = 100
    private val tabela: Array<MutableList<HashElement>?> = arrayOfNulls(rozmiar)

    private fun obliczHash(klucz: String): Int {
        return klucz.hashCode() % rozmiar
    }

    fun dodajElement(klucz: String, wartosc: String) {
        val indeks = obliczHash(klucz)
        if (tabela[indeks] == null) {
            tabela[indeks] = mutableListOf()
        }

        val lista = tabela[indeks]!!
        for (element in lista) {
            if (element.klucz == klucz) {
                element.wartosc = wartosc
                return
            }
        }

        lista.add(HashElement(klucz, wartosc))
    }

    fun znajdzElement(klucz: String): String? {
        val indeks = obliczHash(klucz)
        val lista = tabela[indeks] ?: return null

        for (element in lista) {
            if (element.klucz == klucz) {
                return element.wartosc
            }
        }

        return null
    }

    fun usunElement(klucz: String) {
        val indeks = obliczHash(klucz)
        val lista = tabela[indeks] ?: return

        lista.removeIf { it.klucz == klucz }
    }
}

fun main() {
    // Utworz nowa tabele haszujaca
    val ht = HashTabela()

    // Dodaj elementy do tabeli haszujacej
    ht.dodajElement("imie", "Jan")
    ht.dodajElement("nazwisko", "Kowalski")
    ht.dodajElement("wiek", "30")

    // Szukaj elementow w tabeli haszujacej
    println("Imie: ${ht.znajdzElement("imie")}")
    println("Nazwisko: ${ht.znajdzElement("nazwisko")}")
    println("Wiek: ${ht.znajdzElement("wiek")}")

    // Usun element z tabeli haszujacej
    ht.usunElement("wiek")

    // Probuj znalezc usuniety element
    if (ht.znajdzElement("wiek") == null) {
        println("Element o kluczu 'wiek' zostal usuniety.")
    }
}
