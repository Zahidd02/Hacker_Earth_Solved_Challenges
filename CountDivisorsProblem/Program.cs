using System;

namespace CountDivisorsProblem
{
    class Program
    {
        static void Main(string[] args)
        {
            string input;
            string[] array = new string[3];
            int l;
            int r;
            int k;
            int count = 0;

            //Console.Write("Enter 3 numbers with space between them : ");
            input = Console.ReadLine();

            array = input.Split();

            l = Convert.ToInt32(array[0]);
            r = Convert.ToInt32(array[1]);
            k = Convert.ToInt32(array[2]);

            while (l <= r)
            {
                if (l%k == 0)
                {
                    count++;
                }
                l++;
            }
            //Console.Write("No. of numbers divisible by k between l & r are : ");
            Console.WriteLine(count);
        }
    }
}
