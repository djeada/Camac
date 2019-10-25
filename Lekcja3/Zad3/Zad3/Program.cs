using System;
using System.Collections.Generic;

namespace Zad3
{
    public class Ksiazka
    {
        public int IloscStron { get; private set; }
        public string Nazwa { get; private set; }
        public string Autor { get; private set; }
        public int RokWydania { get; private set; }

        public Ksiazka(int xIloscStron, string xNazwa, string xAutor, int xRokWydania)
        {
            xIloscStron = IloscStron;
            xNazwa = Nazwa;
            xAutor = Autor;
            xRokWydania = RokWydania;
        }

    }
    class Program
    {
        static void Main(string[] args)
        {
            Dictionary<int, Ksiazka> slownik = new Dictionary<int, Ksiazka>();
            List<Dictionary<int, Ksiazka>> lista = new List<Dictionary<int,Ksiazka>>();


            slownik.Add(1, new Ksiazka(561, "Depresja", "Maxwell", 2019));
            slownik.Add(2, new Ksiazka(1, "XD", "lol", 1997));
            slownik.Add(3, new Ksiazka(1337, "Lit", "LUL", 2000));
            slownik.Add(4, new Ksiazka(2137, "Papaj", "JP2", 2005));
            lista.Add(slownik);

            Console.WriteLine("Którą pozycję z listy?");
            var read = Console.ReadLine();
            Console.WriteLine(lista.Count);
          /*  switch (read)
            {
                case "1":
                    foreach (KeyValuePair<> kvp in lista)
                    {
                        Console.WriteLine("Key = {0}, Value = {1}", kvp.Key, kvp.Value);
                    }
                    break;
                case "2":
                    break;
                default:
                    break;
            }*/
        }
    }
}
