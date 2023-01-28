package com.Yang.reverse_7;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int input = scanner.nextInt();
        int out = Solution.reverse(input);
        System.out.println(out);
    }
}
