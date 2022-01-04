using System;

namespace DivisibilityProblem
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int num;
            int[] array;

            Console.WriteLine("Enter number of numbers : ");
            num = Convert.ToInt32(Console.ReadLine());
            array = new int[num];


            Console.WriteLine("Enter numbers : ");
            string[] temp = Console.ReadLine().Split(" ");
            if (temp[num - 1].ToString().EndsWith("0"))
            {
                Console.WriteLine("Yes");
            }
            else
            {
                Console.WriteLine("No");
            }
        }
    }
}
