using System;

namespace RotateMatrixby90
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Write number of rows and columns of a matrix : ");
            string[] values = Console.ReadLine().Split(" ");

            int rows = Convert.ToInt32(values[0]);
            int cols = Convert.ToInt32(values[1]);

            int iteration = rows * cols;
            string[,] A = new string[rows, cols];
            string[,] B = new string[cols, rows];

            Console.WriteLine("Enter matrix : ");
            for (int i = 0; i <= rows - 1; i++)
            {
                string[] matrixRead = Console.ReadLine().Split(" ");
                for (int j = 0; j < cols; j++)
                {
                    A[i, j] = matrixRead[j];
                }
            }
            //Obi wan Kenobi & Darth Vader Easter Egg

            int temp = rows - 1;
            int count = 0;
            for (int i = 0; i <= iteration - 1; i++)
            {
                temp = rows - 1;
                if (count == iteration)
                {
                    break;
                }
                for (int j = 0; j <= (iteration / cols) - 1; j++)
                {
                    B[i, j] = A[temp--, i];
                    if (count == iteration)
                    {
                        break;
                    }
                    count++;
                }
            }

            Console.WriteLine("Rotated matrix by 90 degress : ");
            for (int i = 0; i <= cols - 1; i++)
            {
                for (int j = 0; j <= rows - 1; j++)
                {
                    Console.Write(B[i, j] + " ");
                }
                Console.WriteLine();
            }
        }
    }
}
