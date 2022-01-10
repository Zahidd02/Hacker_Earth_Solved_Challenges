package SevenSegmentDisplayProblem;

import java.math.BigInteger;
import java.util.Dictionary;
import java.util.Hashtable;
import java.util.Scanner;

public class SevenSegmentDisplay {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Enter number of test cases : ");
        int test = scan.nextInt();

        for (int t = 1; t <= test; t++) {

            BigInteger count = new BigInteger("0");
            String result = "";
            String strNum;
            Dictionary<Integer, Integer> dict = new Hashtable<Integer, Integer>();
            dict.put(0, 6);
            dict.put(1, 2);
            dict.put(2, 5);
            dict.put(3, 5);
            dict.put(4, 4);
            dict.put(5, 5);
            dict.put(6, 6);
            dict.put(7, 3);
            dict.put(8, 7);
            dict.put(9, 6);

            System.out.println("Enter the number : ");
            strNum = scan.next();

            for (int i = 0; i <= strNum.length()-1; i++) {
                int temp = Integer.parseInt(strNum.charAt(i) + "");
                count = count.add(BigInteger.valueOf(dict.get(temp)));
            }

            if(count.mod(BigInteger.valueOf(2)).equals(BigInteger.ZERO)) {
                while (count.compareTo(BigInteger.ZERO) != 0) {
                    result += 1;
                    count = count.subtract(BigInteger.TWO);
                }
            }
            else {
                result = "7";
                count = count.subtract(BigInteger.valueOf(3));
                while (count.compareTo(BigInteger.ZERO) != 0) {
                    result += 1;
                    count = count.subtract(BigInteger.TWO);
                }   
            }

            System.out.println(result);
        }
    }
}
