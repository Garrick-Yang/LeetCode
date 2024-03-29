package com.Yang.intToRoman_12;

public class Solution {
    public String intToRoman(int num) {
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        StringBuffer roman = new StringBuffer();
        for (int i = 0; i < values.length; i++) {
            int value = values[i];
            String symbol = symbols[i];

            while(num >= value){
                num -= value;
                roman.append(symbol);
            }

            if (num == 0) break;
        }

        return roman.toString();
    }

    public static void main(String[] args) {
        Solution roman = new Solution();
        String r = roman.intToRoman(1994);
        System.out.println(r);

    }
}



