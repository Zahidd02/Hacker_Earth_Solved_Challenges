using System;

namespace Maximum_Sum_Rectangle
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int[,] rect = new int[4, 5];//rows = 4; cols = 5
            rect[0, 0] = -2;  rect[0, 1] = -1;  rect[0, 2] = -3; rect[0, 3] = -4; rect[0, 4] = -5;
            rect[1, 0] = 8;  rect[1, 1] = -6;  rect[1, 2] = -3;  rect[1, 3] = -4;  rect[1, 4] = -1;
            rect[2, 0] = -2;  rect[2, 1] = -2; rect[2, 2] = -1; rect[2, 3] = -4;  rect[2, 4] = -5;
            rect[3, 0] = -3; rect[3, 1] = -3;  rect[3, 2] = -1;  rect[3, 3] = -10;  rect[3, 4] = -3;

            int result = maxSumRectangle(rect, rect.GetLength(0), rect.GetLength(1));
            Console.WriteLine(result);
        }

        public static int maxSumRectangle(int[,] arr, int n, int m)
        {
            int[] kadaneArr;
            int max = int.MinValue;

            for (int l = 0; l < m; l++)
            {
                kadaneArr = new int[n];
                for (int r = l; r < m; r++)
                {
                    for (int i = 0; i < n; i++)
                    {
                        kadaneArr[i] += arr[i, r];
                    }
                    max = Math.Max(max, kadaneAlgo(kadaneArr));
                }
            }
            return max;
        }

        public static int kadaneAlgo(int[] arr)
        {
            int sum = 0;
            int max = int.MinValue;
            bool flag = false;
            
            //For checking if there exists atleast ONE +ve integer
            for (int i = 0; i < arr.Length; i++)
            {
                if(arr[i] > 0)
                {
                    flag = true;
                }
            }

            if(flag)//For atleast ONE +ve integer
            {
                for (int j = 0; j < arr.Length; j++)
                {
                    sum += arr[j];
                    if (sum < 0)
                    {
                        sum = 0;
                    }
                    max = Math.Max(max, sum);
                }
            }
            else//For no +ve integer
            {
                for (int k = 0; k < arr.Length; k++)
                {
                    max = Math.Max(max, arr[k]); 
                }
            }
            return max;
        }
    }
}
