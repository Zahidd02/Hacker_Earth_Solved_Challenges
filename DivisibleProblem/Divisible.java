package DivisibleProblem;

import java.math.BigInteger;
import java.util.Scanner;

public class Divisible {
    public static void main(String[] args) {
        int num;
        String[] firstHalf;
        String[] secondHalf;
        String result = "";
        System.out.print("Enter (even) number of values in the array : ");
        Scanner scan = new Scanner(System.in);

        num = scan.nextInt();
        firstHalf = new String[num/2];
        secondHalf = new String[num/2];

        System.out.print("Enter values : ");
        for (int i = 0; i <= num / 2 - 1; i++) {
            firstHalf[i] = scan.next();
        }
        for (int i = 0; i <= num / 2 - 1; i++) {
            secondHalf[i] = scan.next();
        } 
    
        String temp;
        for (int k = 0; k <= firstHalf.length - 1; k++) {
            temp = firstHalf[k].substring(0, 1);
            result += temp;
        }
        int x;
        for (int i = 0; i <= secondHalf.length - 1; i++) {
            x = Integer.parseInt(secondHalf[i]);
            x %= 10;
            result += x;
        }

        BigInteger val = new BigInteger(result);
        BigInteger val2 = new BigInteger("11");

        if(val.mod(val2).equals(new BigInteger("0"))) {
            System.out.println("OUI");
        }
        else {
            System.out.println("NON");
        }
    }
}
