using System;

namespace Flip_Bits
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int[] arr = { 1, 0, 0, 0, 1 };

            Console.WriteLine(findMaxZeroCount(arr, arr.Length));
        }

        public static int findMaxZeroCount(int[] arr, int n)
        {
            //O(n^2)
            //========================================================================================================
            //int max_diff = 0;

            //int orig_One = 0;

            //for (int i = 0; i < n; i++)
            //{
            //    int count1 = 0;
            //    int count0 = 0;

            //    if (arr[i] == 1)
            //        orig_One++;

            //    for (int j = i; j < n; j++)
            //    {
            //        if (arr[j] == 0)
            //            count0++;

            //        else count1++;
            //        max_diff = Math.Max(max_diff, count0 - count1);
            //    }
            //}
            //return orig_One + max_diff;
            //========================================================================================================

            //O(n)
            int value = 0;
            int orig_One_Count = 0;
            int curr = 0;
            int maximum = int.MinValue;
            for (int i = 0; i < arr.Length; i++)
            {
                if (arr[i] == 1) 
                {
                    orig_One_Count++;
                }

                if(arr[i] == 0)
                {
                    value = 1;
                }
                else
                {
                    value = -1;
                }

                curr = Math.Max(value, curr + value);
                maximum = Math.Max(maximum, curr);
            }

            if(maximum < 0)
            {
                return orig_One_Count;
            }
            return orig_One_Count + maximum;
        }
    }
}
