package com.Yang.convert_6;

import java.awt.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        int num = scanner.nextInt();
        String output = Solution.convert(input,num);
        System.out.println(output);
    }
}
