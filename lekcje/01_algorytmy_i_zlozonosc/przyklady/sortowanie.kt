import kotlin.random.Random

const val MAX_LICZBA_ELEMENTOW = 100

fun main() {
    println("Podaj liczbe elementow do posortowania (max 100): ")
    val liczbaElementow = readLine()!!.toInt()

    if (liczbaElementow > MAX_LICZBA_ELEMENTOW || liczbaElementow < 1) {
        println("Nieprawidlowa liczba elementow. Zakres: 1-100.")
        return
    }

    println("Czy chcesz wprowadzic liczby recznie? (tak/nie): ")
    val metodaGenerowania = readLine()!!

    val listaWartosci = mutableListOf<Int>()

    if (metodaGenerowania.toLowerCase() == "tak") {
        for (i in 0 until liczbaElementow) {
            println("Podaj wartosc dla elementu ${i + 1}: ")
            listaWartosci.add(readLine()!!.toInt())
        }
    } else {
        for (i in 0 until liczbaElementow) {
            listaWartosci.add(Random.nextInt(1, 101))
        }
    }

    println("Wybierz algorytm sortowania (babelkowe/wybieranie/wstawianie): ")
    val algorytm = readLine()!!

    when (algorytm.toLowerCase()) {
        "babelkowe" -> sortowanieBabelkowe(listaWartosci)
        "wybieranie" -> sortowaniePrzezWybieranie(listaWartosci)
        "wstawianie" -> sortowaniePrzezWstawianie(listaWartosci)
        else -> {
            println("Nieznany algorytm sortowania.")
            return
        }
    }
}

fun sortowanieBabelkowe(lista: MutableList<Int>) {
    val n = lista.size
    for (i in 0 until n) {
        for (j in 0 until n - i - 1) {
            if (lista[j] > lista[j + 1]) {
                val temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
            }
        }
        wyswietl(lista)
    }
}

fun sortowaniePrzezWybieranie(lista: MutableList<Int>) {
    val n = lista.size
    for (i in 0 until n - 1) {
        var minIndeks = i
        for (j in i + 1 until n) {
            if (lista[j] < lista[minIndeks]) {
                minIndeks = j
            }
        }
        val temp = lista[minIndeks]
        lista[minIndeks] = lista[i]
        lista[i] = temp
        wyswietl(lista)
    }
}

fun sortowaniePrzezWstawianie(lista: MutableList<Int>) {
    val n = lista.size
    for (i in 1 until n) {
        val klucz = lista[i]
        var j = i - 1
        while (j >= 0 && lista[j] > klucz) {
            lista[j + 1] = lista[j]
            j -= 1
        }
        lista[j + 1] = klucz
        wyswietl(lista)
    }
}

fun wyswietl(lista: List<Int>) {
    println(lista.joinToString(" "))
}
