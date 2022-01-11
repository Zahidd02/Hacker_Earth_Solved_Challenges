package AliAndHelpingInnocentPeopleProblem;

import java.util.ArrayList;
import java.util.Scanner;

public class AliAndHelpingInnocentPeople {
    public static void main(String[] args) {
        String input;
        Scanner scan = new Scanner(System.in);

        //System.out.println("Enter the tag : ");
        input = scan.nextLine();

        ArrayList<Character> vowels = new ArrayList<Character>();
        vowels.add('A');
        vowels.add('E');
        vowels.add('I');
        vowels.add('O');
        vowels.add('U');
        vowels.add('Y');

        int flag = 0;
        if(!vowels.contains(input.charAt(2)))
        for (int i = 0; i < input.length() - 1; i++) {
            if(i != 1 && i != 2 && i != 5 && i != 6) {
                int temp = Integer.parseInt(input.charAt(i)+"") + Integer.parseInt(input.charAt(i+1)+"");
                if(temp % 2 != 0) {
                    flag = 1;
                }
            }
        }
        else {
            flag = 1;
        }

        if (flag == 0) {
            System.out.println("valid");
        }
        else {
            System.out.println("invalid");
        }
    }
}