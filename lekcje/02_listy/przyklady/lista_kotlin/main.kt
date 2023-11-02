// Definicja klasy Wezel reprezentujacej pojedynczy element listy
class Wezel(val wartosc: Int, var nastepny: Wezel? = null)

// Klasa ListaPolaczona implementujaca liste jednokierunkowa
class ListaPolaczona {
    private var glowa: Wezel? = null

    // Metoda dodajaca nowy wezel na koncu listy
    fun dodajNaKoniec(wartosc: Int) {
        val nowyWezel = Wezel(wartosc)
        if (glowa == null) {
            glowa = nowyWezel
        } else {
            var aktualny = glowa
            while (aktualny?.nastepny != null) {
                aktualny = aktualny.nastepny
            }
            aktualny?.nastepny = nowyWezel
        }
    }

    // Metoda wypisujaca wszystkie elementy listy
    fun wypiszListe() {
        var aktualny = glowa
        while (aktualny != null) {
            print("${aktualny.wartosc} -> ")
            aktualny = aktualny.nastepny
        }
        println("NULL")
    }

    // Metoda usuwajaca wszystkie elementy listy
    fun usunListe() {
        glowa = null
    }
}

// Funkcja main demonstrujaca uzycie listy
fun main() {
    val lista = ListaPolaczona()
    lista.dodajNaKoniec(1)
    lista.dodajNaKoniec(2)
    lista.dodajNaKoniec(3)

    println("Lista polaczona: ")
    lista.wypiszListe()

    lista.usunListe()
}
