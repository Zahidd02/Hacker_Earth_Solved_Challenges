using System;
using System.Collections.Generic;

namespace Trap_Rain_Water
{
    internal class Program
    {
        static int start = 0;
        static int stop = 0;  
        static void Main(string[] args)
        {
            int[] arr = new int[] { 3, 0, 2, 0, 4 };
            int counter = 0;

            Displacement(arr); //To remove all 0's before and after a wall

            while (start != stop)
            {
                for (int j = start; j <= stop; j++)
                {
                    if (arr[j] == 0)
                    {
                        counter++;
                    }
                    else
                    {
                        arr[j]--;
                    }
                }
                Displacement(arr);
            }
            Console.WriteLine("Units of Water Stored : " + counter);

        }

        static void Displacement(int[] arr)
        {

            for (int i = 0; i < arr.Length; i++)
            {
                if (arr[i] > 0)
                {
                    start = i;
                    break;
                }
            }

            for (int i = 0; i < arr.Length; i++)
            {
                if (arr[i] > 0)
                {
                    stop = i;
                }
            }
        }
    }
}
