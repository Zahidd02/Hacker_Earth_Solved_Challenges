using System;

namespace ZoosProblem
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string input;
            string[] inputChars;

            //Console.WriteLine("Enter the word : ");
            input = Console.ReadLine();
            inputChars = new string[input.Length];

            for (int i = 0; i <= input.Length - 1; i++)
            {
                inputChars[i] = input[i] + "";
            }

            int countZ = 0;
            int countO = 0;

            for (int i = 0; i <= input.Length - 1; i++)
            {
                if(inputChars[i].Equals("z"))
                {
                    countZ++;
                }
                else if (inputChars[i].Equals("o"))
                {
                    countO++;
                }
            }

            if(countO == (countZ * 2))
            {
                Console.WriteLine("Yes");//Considered as Zoo
            }
            else
            {
                Console.WriteLine("No");//Not considered as Zoo
            }
        }
    }
}
