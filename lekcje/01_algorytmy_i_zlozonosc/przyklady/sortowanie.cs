using System;
using System.Collections.Generic;

namespace SortingApplication
{
    class Program
    {
        const int MAX_LICZBA_ELEMENTOW = 100;

        static void Main(string[] args)
        {
            var rand = new Random();

            Console.Write("Podaj liczbe elementow do posortowania (max 100): ");
            int liczbaElementow = int.Parse(Console.ReadLine());

            if (liczbaElementow > MAX_LICZBA_ELEMENTOW || liczbaElementow < 1)
            {
                Console.WriteLine("Nieprawidlowa liczba elementow. Zakres: 1-100.");
                return;
            }

            Console.Write("Czy chcesz wprowadzic liczby recznie? (tak/nie): ");
            string metodaGenerowania = Console.ReadLine();

            List<int> listaWartosci = new List<int>(liczbaElementow);

            if (metodaGenerowania.ToLower() == "tak")
            {
                for (int i = 0; i < liczbaElementow; i++)
                {
                    Console.Write("Podaj wartosc dla elementu " + (i + 1) + ": ");
                    listaWartosci.Add(int.Parse(Console.ReadLine()));
                }
            }
            else
            {
                for (int i = 0; i < liczbaElementow; i++)
                {
                    listaWartosci.Add(rand.Next(1, 101));
                }
            }

            Console.Write("Wybierz algorytm sortowania (babelkowe/wybieranie/wstawianie): ");
            string algorytm = Console.ReadLine();

            if (algorytm.ToLower() == "babelkowe")
            {
                SortowanieBabelkowe(listaWartosci);
            }
            else if (algorytm.ToLower() == "wybieranie")
            {
                SortowaniePrzezWybieranie(listaWartosci);
            }
            else if (algorytm.ToLower() == "wstawianie")
            {
                SortowaniePrzezWstawianie(listaWartosci);
            }
            else
            {
                Console.WriteLine("Nieznany algorytm sortowania.");
                return;
            }
        }

        static void SortowanieBabelkowe(List<int> lista)
        {
            int n = lista.Count;
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n - i - 1; j++)
                {
                    if (lista[j] > lista[j + 1])
                    {
                        int temp = lista[j];
                        lista[j] = lista[j + 1];
                        lista[j + 1] = temp;
                    }
                }
                Wyswietl(lista);
            }
        }

        static void SortowaniePrzezWybieranie(List<int> lista)
        {
            int n = lista.Count;
            for (int i = 0; i < n - 1; i++)
            {
                int minIndeks = i;
                for (int j = i + 1; j < n; j++)
                {
                    if (lista[j] < lista[minIndeks])
                    {
                        minIndeks = j;
                    }
                }
                int temp = lista[minIndeks];
                lista[minIndeks] = lista[i];
                lista[i] = temp;
                Wyswietl(lista);
            }
        }

        static void SortowaniePrzezWstawianie(List<int> lista)
        {
            int n = lista.Count;
            for (int i = 1; i < n; i++)
            {
                int klucz = lista[i];
                int j = i - 1;
                while (j >= 0 && lista[j] > klucz)
                {
                    lista[j + 1] = lista[j];
                    j = j - 1;
                }
                lista[j + 1] = klucz;
                Wyswietl(lista);
            }
        }

        static void Wyswietl(List<int> lista)
        {
            foreach (var item in lista)
            {
                Console.Write(item + " ");
            }
            Console.WriteLine();
        }
    }
}
