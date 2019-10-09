import kotlin.random.Random


fun sortowanieBabelkowe(tablica: MutableList<Int>) {
    for (i in tablica.indices) {
        for (j in tablica.indices) {
            if (tablica[i] < tablica[j])
                swap(i, j, tablica)
        }
    }
}


fun swap(i: Int, j: Int, tablica: MutableList<Int>) {
    val temp = tablica[i]
    tablica[i] = tablica[j]
    tablica[j] = temp
}

fun znajdzMin(tablica: MutableList<Int>): Int {
    var minimum = tablica[0]
    var indeks = 0

    for (i in 1 until tablica.size) {
        if (tablica[i] < minimum) {
            minimum = tablica[i]
            indeks = i
        }
    }
    return indeks
}

fun przezWybieranie(tablica: MutableList<Int>) {
    for (i in tablica.indices) {
        val indeks = znajdzMin(tablica.subList(i, tablica.size)) + i
        swap(i, indeks, tablica)
    }
}

fun sortowanieSzybkie(tablica: MutableList<Int>): MutableList<Int> {
    return if (tablica.size > 1)
        (sortowanieSzybkie(tablica.subList(1, tablica.size).filter { it < tablica[0] } as MutableList<Int>)
                + (tablica.filter { it == tablica[0] } as MutableList<Int>)
                + sortowanieSzybkie(tablica.subList(1, tablica.size).filter { it > tablica[0] } as MutableList<Int>))
                as MutableList<Int>
    else
        tablica
}


fun main() {

    val tab: MutableList<MutableList<Int>> =
        mutableListOf(mutableListOf(), mutableListOf(), mutableListOf())
    val czas = mutableListOf<Long>()

    for (j in 0 until 10000) {
        val random = Random.nextInt(0, 10000)
        tab[0].add(random)
        tab[1].add(random)
        tab[2].add(random)
    }

    var start_time = System.currentTimeMillis()
    sortowanieBabelkowe(tab[0])
    czas.add(System.currentTimeMillis() - start_time)

    start_time = System.currentTimeMillis()
    przezWybieranie(tab[1])
    czas.add(System.currentTimeMillis() - start_time)

    start_time = System.currentTimeMillis()
    val tab0 = sortowanieSzybkie(tab[2])
    czas.add(System.currentTimeMillis() - start_time)

    println(czas)

    if(tab[0] == tab[1] && tab[0] == tab0) {
        print("OK")
    }

}