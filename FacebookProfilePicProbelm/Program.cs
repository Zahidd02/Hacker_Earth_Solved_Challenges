using System;

namespace FacebookProfilePicProbelm
{
    class Program
    {
        static void Main(string[] args)
        {
            int L;
            int N;
            string strWH;
            string[] arr = new string[2];
            int W;
            int H;

            Console.Write("Enter square image side length : ");
            L = Convert.ToInt32(Console.ReadLine());

            Console.Write("Enter number of images : ");
            N = Convert.ToInt32(Console.ReadLine());

            for (int i = 1; i <= N; i++)
            {
                Console.Write("Enter width and height of image with space in between : ");
                strWH = Console.ReadLine();

                arr = strWH.Split(" ");
                W = Convert.ToInt32(arr[0]);
                H = Convert.ToInt32(arr[1]);

                if (W < L || H < L)
                {
                    Console.WriteLine("UPLOAD ANOTHER");
                }
                if (W >= L && H >= L) {
                     if (W == H)
                    {
                        Console.WriteLine("ACCEPTED");
                    }
                    else
                    {
                        Console.WriteLine("CROP IT");
                    }
                }
            }
        }
    }
}
