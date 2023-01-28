package com.Yang.longestPalindrome_5;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = null;
        if (scanner.hasNextLine()){
            input = scanner.nextLine();
        }
//        String string = "awawa";
        String string_1 = Solution.longestPalindrome(input);
        System.out.println(string_1);
    }
}

