using System;

namespace _100_Doors_Problem
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //0 - closed ; 1 - open
            int[] arr = new int[100];

            for (int i = 0; i < arr.Length; i++)
            {
                arr[i] = 0;
            }

            Console.WriteLine("Before process : ");

            foreach (var item in arr)
            {
                Console.Write(item + " ");
            }

            Console.WriteLine("##################################################################################################################################");

            for (int i = 1; i <= 100; i++)
            {
                for (int j = 0; j < 100; j++)
                {
                    if ((j + 1) % i == 0)
                    {
                        if (arr[j] == 0)
                        {
                            arr[j] = 1;
                        }
                        else
                        {
                            arr[j] = 0;
                        }
                    }
                }
            }

            Console.WriteLine("After process : ");

            int l = 1;
            foreach (var item in arr)
            {
                Console.Write(item + " ");
                if (item == 1)
                {
                    Console.Write("//" + l + "//");
                }
                l++;
            }
        }
    }
}
