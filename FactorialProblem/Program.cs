using System;

namespace FactorialProblem
{
    class Program
    {
        static void Main(string[] args)
        {
            Int64 num;
            string stringNum;

            Console.Write("Enter number to find factorial of : ");
            stringNum = Console.ReadLine();

            num = Convert.ToInt64(stringNum);

            Int64 result = 1;
            for (Int64 i = 1; i <= num; i++)
            {
                result = result * i;
            }

            Console.WriteLine("The factorial of the number is : " + result);

        }
    }
}
