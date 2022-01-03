using System;
using System.Collections.Generic;

namespace NumberOfSteps
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int num;
            int min;
            List<int> temp = new List<int>();

            Console.Write("Enter a Number : ");
            num = Convert.ToInt32(Console.ReadLine());

            int[] arrA = new int[num];
            int[] arrB = new int[num];

            Console.Write("Enter a values with space between them : ");
            string[] tempA = Console.ReadLine().Split(" ");

            for (int i = 0; i <= arrA.Length - 1; i++)
            {
               arrA[i] = Convert.ToInt32(tempA[i]);
            }

            Console.Write("Enter next set of values with space between them : ");
            string[] tempB = Console.ReadLine().Split(" ");

            for (int i = 0; i <= arrB.Length - 1; i++)
            {
                arrB[i] = Convert.ToInt32(tempB[i]);
            }

            //Finding minimum value inside array
            foreach (var item in arrA)
            {
                temp.Add(item);
            }
            temp.Sort();

            min = temp[0];

            //Subtraction
            int x = 0;
            int step = 0;
            while (true)
            {
                if (arrA[x] != min)
                {
                    arrA[x] = arrA[x] - arrB[x];
                    step++;
                }
                if (arrA[x] == min && x != arrA.Length - 1)
                {
                    x++;
                }
                if (x == arrA.Length - 1 && arrA[arrA.Length - 1] == min)
                {
                    break;
                }
                if (arrA[x] < 0)
                {
                    Console.WriteLine(-1);
                    goto NegativeCase;
                }
            }
            Console.WriteLine(step);

        NegativeCase:
            Console.WriteLine("");
        }
    }
}
