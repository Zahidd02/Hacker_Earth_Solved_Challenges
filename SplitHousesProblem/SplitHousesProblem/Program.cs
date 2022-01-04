using System;

namespace SplitHousesProblem
{
    internal class Program
    {
        static void Main(string[] args)
        {
            char[] array;
            //Console.WriteLine("Enter number of grids : ");
            int grid = Convert.ToInt32(Console.ReadLine());
            array = new char[grid];

            //Console.WriteLine("Enter village : ");
            string village = Console.ReadLine();

            for (int i = 0; i <= grid - 1; i++)
            {
                array[i] = village[i];
            }

            if (grid == 1)
            {
                Console.WriteLine("YES");
                Console.WriteLine(village.Replace('.', 'B'));
                goto NoCase;
            }

            int count = 0;
            for (int j = 0; j <= grid - 2; j++)
            { 
                if (array[j] == 'H' && array[j + 1] == 'H')
                {
                    Console.WriteLine("NO");
                    goto NoCase;
                }
                if(array[j] == '.' && array[j + 1] == '.')
                {
                    count++;
                }
                if(array[j] == '.' && array[j + 1] == 'H')
                {
                    count++;
                }
                if (array[j] == 'H' && array[j + 1] == '.')
                {
                    count++;
                }
            }

            if(count > 0)
            {
                Console.WriteLine("YES");
                Console.WriteLine(village.Replace('.', 'B'));
            }

            NoCase:
            Console.WriteLine("");

        }
    }
}
