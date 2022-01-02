using System;

namespace PalindromicStringProblem
{
    class Program
    {
        static void Main(string[] args)
        {
            string str;
            string reverse = "";
            //Console.WriteLine("Enter a string to check if it's a palindrome : ");
            str = Console.ReadLine().ToLower();

            for (int i = (str.Length - 1); i >= 0; i--)
            {
                reverse += str[i];
            }

            if(reverse.Equals(str))
            {
                Console.WriteLine("YES");
            }
            else
            {
                Console.WriteLine("NO");
            }

        }
    }
}
