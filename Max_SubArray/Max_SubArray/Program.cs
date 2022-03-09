using System;

namespace Max_SubArray
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int[] arr = { 1, -2, -3, 4, -1, 2, 1 };
            int maxSumSoFar = int.MinValue;
            int sum = 0;

            //O(n) -- All test cases passed
            //for (int i = 0; i < arr.Length; i++)
            //{
            //    sum = sum + arr[i];
            //    maxSumSoFar = Math.Max(maxSumSoFar, sum);
            //    if (sum < 0)
            //    {
            //        sum = 0;
            //    }
            //}

            //O(n^2) -- Not all test cases passed
            for (int i = 0; i < arr.Length; i++)
            {
                sum = 0;
                for (int j = i; j < arr.Length; j++)
                {
                    sum = sum + arr[j];
                    maxSumSoFar = Math.Max(maxSumSoFar, sum);
                    if (sum < 0)
                    {
                        sum = 0;
                    }
                }
            }
            Console.WriteLine(maxSumSoFar);
        }
    }
}
