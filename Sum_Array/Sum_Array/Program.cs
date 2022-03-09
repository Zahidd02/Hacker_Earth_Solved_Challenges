using System;

namespace Sum_Array
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int[] array = new int[] { 3, 4, -1, 2, 5 };
            int[] prefix = new int[array.Length];
            int[] suffix = new int[array.Length];
            int sum = 0;

            //Prefix Sum Array :: O(n^2)
            for (int i = 0; i < array.Length; i++)
            {
                sum = 0;
                for (int j = 0; j <= i; j++)
                {
                    sum += array[j];
                }
                prefix[i] = sum;
            }

            foreach (var item in prefix)
            {
                Console.Write(item + "  ");
            }
            Console.WriteLine("\n");

            //Prefix Sum Array :: O(n)
            prefix[0] = array[0];

            for (int i = 1; i < array.Length; i++)
            {
                prefix[i] = prefix[i - 1] + array[i];
            }

            foreach (var item in prefix)
            {
                Console.Write(item + "  ");
            }
            Console.WriteLine("\n");

            //==============================================================================================================
            //==============================================================================================================

            //Suffix Sum Array :: O(n)
            sum = 0;
            for (int j = 0; j < array.Length; j++)
            {
                sum += array[j];
            }

            suffix[0] = sum;

            for (int i = 1; i < array.Length; i++)
            {

                suffix[i] = suffix[i - 1] - array[i - 1];
            }

            foreach (var item in suffix)
            {
                Console.Write(item + "  ");
            }
            Console.WriteLine("\n");
        }
    }
}
