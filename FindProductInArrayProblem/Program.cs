using System;
using System.Numerics;
namespace FindProductInArrayProblem
{
    class Program
    {
        static void Main(string[] args)
        {
            int size;
            BigInteger mul = 1;
            int temp;

            //Console.WriteLine("Enter size of array : ");
            size = Convert.ToInt32(Console.ReadLine());

            string[] strNumbers = new string[size];

            //Console.WriteLine("Enter numbers with space between them : ");
            strNumbers = Console.ReadLine().Split();

            for (int i = 0; i < strNumbers.Length; i++)
            {
                temp = Convert.ToInt32(strNumbers[i]);
                mul = (mul * temp) % (1000000007);
            }

            //Console.WriteLine("Product of the numbers : ");
            Console.WriteLine(mul);

        }
    }
}