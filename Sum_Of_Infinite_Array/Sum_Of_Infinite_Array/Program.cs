using System;
using System.Collections.Generic;

namespace Sum_Of_Infinite_Array
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int test = 0;

            Console.WriteLine("Enter test cases : ");
            test = Convert.ToInt32(Console.ReadLine());

            for (int i = 1; i <= test; i++)
            {
                Console.WriteLine("Enter size of the array : ");
                int size = Convert.ToInt32(Console.ReadLine());

                int[] array = new int[size];

                Console.WriteLine("Enter the array : ");
                string[] arrayTemp = Console.ReadLine().Split(" ");

                for (int j = 0; j < size; j++)
                {
                    array[j] = Convert.ToInt32(arrayTemp[j]);
                }

                Console.WriteLine("Enter the L and R values : ");
                string[] LR = Console.ReadLine().Split(" ");

                int L = Convert.ToInt32(LR[0]);
                int R = Convert.ToInt32(LR[1]);

                List<int> newArray = new List<int>();

                for (int k = 0; k <= R ; k++)
                {
                    foreach (var item in array)
                    {
                        newArray.Add(item);
                    }
                }
                int sum = 0;
                for (int m = L; m <= R; m++)
                {
                    sum += newArray[m];
                }
                Console.WriteLine(sum);
            }
        }
    }
}
