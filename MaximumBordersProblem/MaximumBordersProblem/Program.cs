using System;
using System.Collections.Generic;

namespace MaximumBordersProblem
{
    public class Program
    {
        static void Main(string[] args)
        {
            int rows;
            int cols;
            int test;
            String[] values = new string[2];

            Console.Write("Number of Test cases : ");
            test = Convert.ToInt32(Console.ReadLine());

            Cases:
            List<int> result = new List<int>();

            Console.Write("Number of rows and columns with space between them : ");
            values = Console.ReadLine().Split(" ");

            rows = Convert.ToInt32(values[0]);
            cols = Convert.ToInt32(values[1]); 

            String[,] origPattern = new string[rows, cols];
            String[,] rotPattern = new string[cols, rows];
            int iteration = rows * cols;

            //Calculating # for Original Pattern
            for (int i = 0; i <= rows - 1; i++)
            {
                String x = Console.ReadLine();
                for (int j = 0; j <= cols - 1; j++)
                {
                    origPattern[i, j] = x[j] + "";
                }
            }
            int count = 0;
            for (int i = 0; i <= rows - 1; i++)
            {
                for (int j = 0; j <= cols - 1; j++)
                {
                    if (origPattern[i, j].Equals("#"))
                    {
                        count++;
                    }
                    if (j == (cols - 1) || origPattern[i, j+1].Equals("."))
                    {
                        result.Add(count);
                        count = 0;
                    }
                }
            }

            //Calculating # for Rotated Matrix
            int temp = rows - 1;
            count = 0;
            for (int i = 0; i <= iteration - 1; i++)
            {
                temp = rows - 1;
                if (count == iteration)
                {
                    break;
                }
                for (int j = 0; j <= (iteration / cols) - 1; j++)
                {
                    rotPattern[i, j] = origPattern[temp--, i];
                    if (count == iteration)
                    {
                        break;
                    }
                    count++;
                }
            }

            count = 0;
            for (int i = 0; i <= cols - 1; i++)
            {
                for (int j = 0; j <= rows - 1; j++)
                {
                    if (rotPattern[i, j].Equals("#"))
                    {
                        count++;
                    }
                    if (j == (rows - 1) || rotPattern[i, j + 1].Equals("."))
                    {
                        result.Add(count);
                        count = 0;
                    }
                }
            }

            result.Sort();
            result.Reverse();
            result.RemoveAll(x => x.Equals(0));
            Console.WriteLine(result[0]);

            test--;
            if(test != 0)
            {
                goto Cases;
            }
        }
    }
}