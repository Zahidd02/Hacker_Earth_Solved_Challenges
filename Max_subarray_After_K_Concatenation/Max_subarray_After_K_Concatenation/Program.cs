using System;
using System.Collections.Generic;

namespace Max_subarray_After_K_Concatenation
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<int> arr = new List<int>();//10, 20, -30, -1
            arr.Add(10);
            arr.Add(20);
            arr.Add(-30);
            arr.Add(-1);

            var result = maxSubSumKConcat(arr, 1, 11);
            Console.WriteLine(result);
        }

        public static long maxSubSumKConcat(List<int> arr, int n, int k)
        {
            #region Method 1 : Non - Optimal : O(n^2)
            //long max = int.MinValue;
            //long sum = 0;

            //for (int i = 0; i < k - 1; i++)
            //{
            //    for (int j = 0; j < n; j++)
            //    {
            //        arr.Add(arr[j]);
            //    }
            //}

            //if(arr.Exists(x => x > 0))
            //{
            //    for (int l = 0; l < arr.Count; l++)
            //    {
            //        sum = sum + arr[l];
            //        if (sum < 0)
            //        {
            //            sum = 0;
            //        }
            //        max = Math.Max(max, sum);
            //    }
            //}
            //else//-17 -278 -38 -4 -5 -67
            //{
            //    long temp = sum + arr[0];//-17
            //    for (int l = 0; l < arr.Count; l++)
            //    {
            //        sum = arr[l];
            //        if(sum < temp)
            //        {
            //            sum = temp;
            //        }

            //        max = Math.Max(max, sum);

            //    }
            //}

            //return max;
            #endregion
            #region Method 2 : Optimal : O(n * K)
            long max = int.MinValue;
            long sum = 0;

            if (arr.Exists(x => x > 0))
            {
                for (int i = 0, j = 0; i < n * k; i++)
                {
                    sum = sum + arr[j++];
                    if (sum < 0)
                    {
                        sum = 0;
                    }
                    if (j == n)
                    {
                        j = 0;
                    }
                    max = Math.Max(max, sum);
                }
            }
            else
            {
                long temp = arr[0];
                for (int l = 0; l < n; l++)
                {
                    if (arr[l] > temp)
                    {
                        temp = arr[l];
                    }
                    max = Math.Max(max, temp);
                }
            }
            return max;
            #endregion
        }
    }
}
