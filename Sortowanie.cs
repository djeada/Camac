 using System;
class Sortowanie
{
    public static int[] Losowa(int[] tablica)
    {
        int[] tab = new int[10000];
        Random losowa = new Random(100);
        for (int i = 0; i < tab.Length; i++)
        {
            tab[i] = losowa.Next(1, 10000);
        }
        return tab;
    }

    public static void Swap(int[] a, int uno)
    {
        int trzym = a[uno];
        a[uno] = a[uno + 1];
        a[uno + 1] = trzym;
    }

    public static int[] Buble(int[] a)
    {
        for(int i = 1; i < a.Length; i++)
        {
            for (int j = 0; j < a.Length - 1; j++)
            {
                if (a[j] > a[j + 1])
                {
                    Swap(a, j);
                }
            }
        }
        return a;
    }

    public static int[] Selection(int[] a)
    {
        int min;
        for(int i = 0; i < a.Length - 1; i++)
        {
            min = i;
            for(int j = i+1; j < a.Length; j++)
            {
                if (a[j] < a[min])
                {
                    min = j;
                }
            }
            Swap(a, i);
            /*var hold = a[min];
            a[min] = a[i];
            a[i] = hold;*/
        }
        return a;
    }

    public static int[] Quick(int[] a, int lewy, int prawy)
    {
        var i = lewy;
        var j = prawy;
        var srodek = a[(lewy + prawy) / 2];
        while (i < j)
        {
            while (a[i] < srodek) i++;
            while (a[j] > srodek) j--;
            if (i <= j)
            {
                var hold = a[i];
                a[i++] = a[j];
                a[j--] = hold;
            }
        }
        if (lewy < j) Quick(a, lewy, j);
        if (i < prawy) Quick(a, i, prawy);
        return a;
    }

    static void Main(string[] args)
    {
        long czas = 0;
        long czas1 = 0;
        long czas2 = 0;
        int[] losowa = new int[10000];
        int[] tab = new int[10000];

        //Bubblesort
        int[] buble = new int[10000];
        losowa = Losowa(tab);
        czas1 = new DateTimeOffset(DateTime.UtcNow).ToUnixTimeMilliseconds();
        buble = Buble(losowa);
        czas2 = new DateTimeOffset(DateTime.UtcNow).ToUnixTimeMilliseconds();
        czas = czas2 - czas1;
        //Console.WriteLine("[{0}]", string.Join(" , ", buble));        //Jak ktoś potrzebuje wypisania tablicy
        Console.WriteLine("\n");
        Console.Write("(buble) Operacja zajęła:" + czas + "milisekund");
        Console.WriteLine("\n");

        //Selection sort
        int[] select = new int[10000];
        czas = czas1 = czas2 = 0;
        losowa = Losowa(tab);
        czas1 = new DateTimeOffset(DateTime.UtcNow).ToUnixTimeMilliseconds();
        select = Selection(losowa);
        czas2 = new DateTimeOffset(DateTime.UtcNow).ToUnixTimeMilliseconds();
        czas = czas2 - czas1;
        //Console.WriteLine("[{0}]", string.Join(" , ", select));        //Wypisanie
        Console.WriteLine("\n");
        Console.Write("(select) Operacja zajęła:" + czas + "milisekund");
        Console.WriteLine("\n");

        //Quick sort
        int[] quick = new int[10000];
        czas = czas1 = czas2 = 0;
        losowa = Losowa(tab);
        czas1 = new DateTimeOffset(DateTime.UtcNow).ToUnixTimeMilliseconds();
        quick = Quick(losowa, 0, losowa.Length - 1);
        czas2 = new DateTimeOffset(DateTime.UtcNow).ToUnixTimeMilliseconds();
        czas = czas2 - czas1;
        //Console.WriteLine("[{0}]", string.Join(" , ", quick));        //Wypisanie
        Console.WriteLine("\n");
        Console.Write("(quick) Operacja zajęła:" + czas + "milisekund");
        Console.WriteLine("\n");


    }
}


