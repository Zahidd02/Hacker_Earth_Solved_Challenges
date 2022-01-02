using System;
using System.Collections.Generic;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            int num;
            int x = 0;
            List<int> arr = new List<int>();
            //Console.WriteLine("Enter the numbers : ");

            while (true)
            {
                if(x != 42)
                {
                    num = Convert.ToInt32(Console.ReadLine());
                    if (num != 42)
                        arr.Add(num);
                    x = num;
                }
                else
                {
                    break;
                }

            }

            //Console.WriteLine("The numbers are : ");
            foreach (var item in arr)
            {
                Console.WriteLine(item);
            }
        }
    }
}
