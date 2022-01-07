package CostOfBalloonsProblem;

import java.util.Scanner;

public class CostOfBalloons {
    public static void main(String[] args) {
        int test;
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter number of test cases : ");
        test = scan.nextInt();

        for (int m = 1; m <= test; m++) {
            int greenBalloon;
            int purpleBalloon;
            int participants;
            int[] firstScore;
            int[] secondScore;
            int firstTotal = 0;
            int secondTotal = 0;
            int result = 0; 
            System.out.print("Enter the cost of balloons with space between them : ");
            greenBalloon = scan.nextInt();
            purpleBalloon = scan.nextInt();

            System.out.print("Enter number of participants : ");
            participants = scan.nextInt();

            firstScore = new int[participants];
            secondScore = new int[participants];
            for (int i = 0; i <= participants - 1; i++) {
                firstScore[i] = scan.nextInt();
                secondScore[i] = scan.nextInt();
            }

            for (int j = 0; j <= participants - 1; j++) {
                firstTotal += firstScore[j];
                secondTotal += secondScore[j];
            }

            if(greenBalloon <= purpleBalloon) {
                if((greenBalloon * firstTotal) < (greenBalloon * secondTotal)) {
                    result += (greenBalloon * secondTotal) + (purpleBalloon * firstTotal);
            }
                else {
                    result += (greenBalloon * firstTotal) + (purpleBalloon * secondTotal);
                }
            }
            else if(purpleBalloon < greenBalloon) {
                if((purpleBalloon * firstTotal) < (purpleBalloon * secondTotal)) {
                    result += (purpleBalloon * secondTotal) + (greenBalloon * firstTotal);
                }
                else {
                    result += (purpleBalloon * firstTotal) + (greenBalloon * secondTotal);
                }
            }
            System.out.print("The minimum cost is : ");
            System.out.println(result);
        }
    }
}
