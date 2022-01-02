package ToggleStringProblem;

import java.util.Scanner;

public class ToggleString {
    public static void main(String[] args) {
        String original;
        String cap;
        String small;
        String newOutput = "";

        //System.out.print("Enter a Alphabetical string : ");
        Scanner x = new Scanner(System.in);
        String input = x.nextLine();

        for (int i = 0; i <= input.length()-1; i++) {
            original = "";
            cap = "";
            small = "";

            original += input.charAt(i);
            cap += original.toUpperCase();
            small += original.toLowerCase(); 
            
            if (original.equals(cap)) {
                newOutput += small;
            }
            else if(original.equals(small)) {
                newOutput += cap;
            }     
        }

        //System.out.print("New string with reversed characters : ");
        System.out.print(newOutput);
    }
}
